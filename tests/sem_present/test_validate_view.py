from __future__ import annotations

import importlib.util
import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
VALIDATOR_PATH = REPO_ROOT / "skills" / "sem-present" / "scripts" / "validate_view.py"
FIXTURES = Path(__file__).resolve().parent / "fixtures"

SPEC = importlib.util.spec_from_file_location("validate_view", VALIDATOR_PATH)
assert SPEC and SPEC.loader
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


class ValidatorTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.workspace = Path(self.temporary.name)

    def copy_fixture(self, name: str = "minimal-success") -> Path:
        destination = self.workspace / name
        shutil.copytree(FIXTURES / name, destination)
        return destination

    def load_manifest(self, run: Path) -> dict:
        return json.loads((run / "view" / "manifest.json").read_text(encoding="utf-8"))

    def write_manifest(self, run: Path, manifest: dict, name: str = "manifest.json") -> Path:
        path = run / "view" / name
        path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
        return path

    def mutate(self, change, fixture: str = "minimal-success") -> tuple[Path, list[str]]:
        run = self.copy_fixture(fixture)
        manifest = self.load_manifest(run)
        change(manifest, run)
        self.write_manifest(run, manifest)
        return run, VALIDATOR.validate(run)

    def assertDiagnostic(self, diagnostics: list[str], fragment: str) -> None:
        self.assertTrue(
            any(fragment in diagnostic for diagnostic in diagnostics),
            f"expected diagnostic containing {fragment!r}, got:\n" + "\n".join(diagnostics),
        )


class PositiveBundleTests(ValidatorTestCase):
    def test_every_positive_fixture_passes_library_and_cli(self) -> None:
        for fixture in ("minimal-success", "active-partial"):
            with self.subTest(fixture=fixture):
                run = FIXTURES / fixture
                self.assertEqual([], VALIDATOR.validate(run))
                completed = subprocess.run(
                    [sys.executable, str(VALIDATOR_PATH), str(run)],
                    text=True,
                    capture_output=True,
                    check=False,
                )
                self.assertEqual(0, completed.returncode, completed.stderr)
                self.assertIn("valid: view/manifest.json", completed.stdout)

    def test_partial_and_active_bundle_needs_no_result(self) -> None:
        run = FIXTURES / "active-partial"
        self.assertEqual([], VALIDATOR.validate(run))

    def test_every_reference_manifest_example_passes(self) -> None:
        examples_path = REPO_ROOT / "skills" / "sem-present" / "references" / "example-manifests.md"
        examples = re.findall(r"```json\n(.*?)\n```", examples_path.read_text(encoding="utf-8"), re.DOTALL)
        self.assertEqual(3, len(examples))
        for index, source in enumerate(examples):
            with self.subTest(example=index + 1):
                run = self.workspace / f"reference-{index + 1}"
                (run / "view").mkdir(parents=True)
                manifest = json.loads(source)
                for artifact in manifest["artifacts"]:
                    artifact_path = run.joinpath(*artifact["path"].split("/"))
                    artifact_path.parent.mkdir(parents=True, exist_ok=True)
                    artifact_path.write_text(f"# {artifact['title']}\n", encoding="utf-8")
                self.write_manifest(run, manifest)
                (run / "view" / "notes.md").write_text("# View notes\n", encoding="utf-8")
                self.assertEqual([], VALIDATOR.validate(run))

    def test_unknown_and_nested_input_files_are_valid_when_inventoried(self) -> None:
        run = self.copy_fixture()
        (run / "inputs").mkdir()
        (run / "inputs" / "source note.txt").write_text("source\n", encoding="utf-8")
        (run / "misc.dat").write_bytes(b"\x00fixture")
        manifest = self.load_manifest(run)
        manifest["artifacts"].extend([
            {"id": "a-input", "path": "inputs/source note.txt", "mediaType": "text/plain", "role": "input", "title": "Source note"},
            {"id": "a-misc", "path": "misc.dat", "mediaType": "application/octet-stream", "role": "other", "title": "Unknown file"},
        ])
        self.write_manifest(run, manifest)
        self.assertEqual([], VALIDATOR.validate(run))

    def test_hidden_files_and_directories_are_ignored(self) -> None:
        run = self.copy_fixture()
        (run / ".DS_Store").write_text("noise", encoding="utf-8")
        (run / ".private").mkdir()
        (run / ".private" / "secret.md").write_text("secret", encoding="utf-8")
        (run / "applications" / ".draft").mkdir()
        (run / "applications" / ".draft" / "prompt.md").write_text("draft", encoding="utf-8")
        self.assertEqual([], VALIDATOR.validate(run))

    def test_safe_internal_file_symlink_is_inventoried(self) -> None:
        run = self.copy_fixture()
        (run / "inputs").mkdir()
        (run / "inputs" / "original.md").write_text("original\n", encoding="utf-8")
        (run / "inputs" / "alias.md").symlink_to("original.md")
        manifest = self.load_manifest(run)
        manifest["artifacts"].extend([
            {"id": "a-original", "path": "inputs/original.md", "mediaType": "text/markdown", "role": "input", "title": "Original"},
            {"id": "a-alias", "path": "inputs/alias.md", "mediaType": "text/markdown", "role": "input", "title": "Alias"},
        ])
        self.write_manifest(run, manifest)
        self.assertEqual([], VALIDATOR.validate(run))

    def test_safe_internal_application_directory_symlink_is_valid(self) -> None:
        run = self.copy_fixture()
        hidden_store = run / ".app-store"
        hidden_store.mkdir()
        shutil.move(str(run / "applications" / "001-answer"), hidden_store / "001-answer")
        (run / "applications" / "001-answer").symlink_to("../.app-store/001-answer", target_is_directory=True)
        self.assertEqual([], VALIDATOR.validate(run))

    def test_candidate_manifest_does_not_require_canonical_notes(self) -> None:
        run = self.copy_fixture()
        candidate = run / "view" / "manifest.test-generation.next.json"
        shutil.copy2(run / "view" / "manifest.json", candidate)
        (run / "view" / "notes.md").unlink()
        self.assertDiagnostic(VALIDATOR.validate(run), "view/notes.md")
        self.assertEqual([], VALIDATOR.validate(run, "view/manifest.test-generation.next.json"))

    def test_validation_never_modifies_run(self) -> None:
        run = self.copy_fixture()
        before = {path.relative_to(run): path.read_bytes() for path in run.rglob("*") if path.is_file()}
        self.assertEqual([], VALIDATOR.validate(run))
        after = {path.relative_to(run): path.read_bytes() for path in run.rglob("*") if path.is_file()}
        self.assertEqual(before, after)


class StructureTests(ValidatorTestCase):
    def test_invalid_json_is_path_specific(self) -> None:
        run = self.copy_fixture()
        (run / "view" / "manifest.json").write_text("{ nope", encoding="utf-8")
        diagnostics = VALIDATOR.validate(run)
        self.assertDiagnostic(diagnostics, "manifest: invalid JSON at line 1")

    def test_required_top_level_and_nested_fields(self) -> None:
        def change(manifest, _run):
            del manifest["edges"]
            del manifest["run"]["snapshot"]
            del manifest["nodes"][0]["panels"][0]["renderAs"]

        _run, diagnostics = self.mutate(change)
        self.assertDiagnostic(diagnostics, "manifest.edges: required field is missing")
        self.assertDiagnostic(diagnostics, "manifest.run.snapshot: required field is missing")
        self.assertDiagnostic(diagnostics, "manifest.nodes[0].panels[0].renderAs: required field is missing")

    def test_types_enums_version_and_timestamp(self) -> None:
        def change(manifest, _run):
            manifest["schemaVersion"] = "2.0"
            manifest["generatedAt"] = "yesterday"
            manifest["run"]["snapshot"] = "false"
            manifest["run"]["status"] = "complete"
            manifest["artifacts"][0]["role"] = "document"
            manifest["nodes"][0]["type"] = "widget"
            manifest["nodes"][0]["emphasis"] = "loud"
            manifest["edges"][0]["type"] = "data"

        _run, diagnostics = self.mutate(change)
        for fragment in (
            "manifest.schemaVersion", "manifest.generatedAt", "manifest.run.snapshot",
            "manifest.run.status", "manifest.artifacts[0].role", "manifest.nodes[0].type",
            "manifest.nodes[0].emphasis", "manifest.edges[0].type",
        ):
            self.assertDiagnostic(diagnostics, fragment)

    def test_timestamp_rejects_iso_forms_outside_rfc3339(self) -> None:
        def change(manifest, _run):
            manifest["generatedAt"] = "2026-07-19 15:30:00+00:00"

        _run, diagnostics = self.mutate(change)
        self.assertDiagnostic(diagnostics, "manifest.generatedAt")

    def test_run_snapshot_and_status_must_agree(self) -> None:
        cases = (
            ("succeeded", True, "non-terminal"),
            ("running", False, "terminal"),
            ("partial", True, "non-terminal"),
            ("unknown", False, "terminal"),
        )
        for index, (status, snapshot, expected) in enumerate(cases):
            with self.subTest(status=status, snapshot=snapshot):
                run = self.workspace / f"run-state-{index}"
                shutil.copytree(FIXTURES / "minimal-success", run)
                manifest = self.load_manifest(run)
                manifest["run"].update(status=status, snapshot=snapshot)
                self.write_manifest(run, manifest)
                self.assertDiagnostic(VALIDATOR.validate(run), expected)

    def test_each_run_state_partition_has_a_valid_pair(self) -> None:
        pairs = (
            ("unknown", True),
            ("pending", True),
            ("ready", True),
            ("running", True),
            ("succeeded", False),
            ("failed", False),
            ("blocked", False),
            ("partial", False),
        )
        for index, (status, snapshot) in enumerate(pairs):
            with self.subTest(status=status, snapshot=snapshot):
                fixture = "active-partial" if snapshot else "minimal-success"
                run = self.workspace / f"valid-run-state-{index}"
                shutil.copytree(FIXTURES / fixture, run)
                manifest = self.load_manifest(run)
                manifest["run"].update(status=status, snapshot=snapshot)
                self.write_manifest(run, manifest)
                self.assertEqual([], VALIDATOR.validate(run))

    def test_nonstandard_json_constants_and_invalid_utf8_are_rejected(self) -> None:
        run = self.copy_fixture()
        manifest_path = run / "view" / "manifest.json"
        source = manifest_path.read_text(encoding="utf-8")
        manifest_path.write_text(source.replace('"extensions": {}', '"extensions": {"example.org": NaN}'), encoding="utf-8")
        self.assertDiagnostic(VALIDATOR.validate(run), "manifest: invalid JSON")

        manifest_path.write_bytes(b"\xff")
        self.assertDiagnostic(VALIDATOR.validate(run), "manifest: invalid JSON")

    def test_duplicate_json_object_keys_are_rejected(self) -> None:
        run = self.copy_fixture()
        manifest_path = run / "view" / "manifest.json"
        source = manifest_path.read_text(encoding="utf-8")
        manifest_path.write_text(source.replace('"kind": "sem-run-view"', '"kind": "other", "kind": "sem-run-view"'), encoding="utf-8")
        self.assertDiagnostic(VALIDATOR.validate(run), "manifest: invalid JSON: duplicate object key 'kind'")

    def test_scoped_and_collection_id_uniqueness(self) -> None:
        def change(manifest, _run):
            manifest["artifacts"][1]["id"] = manifest["artifacts"][0]["id"]
            manifest["nodes"][1]["id"] = manifest["nodes"][0]["id"]
            manifest["edges"].append(dict(manifest["edges"][0]))
            manifest["groups"] = [
                {"id": "g", "title": "G", "type": "phase", "memberNodeIds": []},
                {"id": "g", "title": "G2", "type": "other", "memberNodeIds": []},
            ]
            manifest["nodes"][0]["panels"][1]["id"] = manifest["nodes"][0]["panels"][0]["id"]

        _run, diagnostics = self.mutate(change)
        for fragment in (
            "manifest.artifacts[1].id: duplicate ID", "manifest.nodes[1].id: duplicate ID",
            "manifest.edges[1].id: duplicate ID", "manifest.groups[1].id: duplicate ID",
            "manifest.nodes[0].panels[1].id: duplicate ID",
        ):
            self.assertDiagnostic(diagnostics, fragment)

    def test_selector_and_extension_shapes(self) -> None:
        def change(manifest, _run):
            manifest["nodes"][1]["panels"][0]["selector"] = {"kind": "lines", "occurrence": 0}
            manifest["extensions"] = {"not_namespaced": {}}

        _run, diagnostics = self.mutate(change)
        self.assertDiagnostic(diagnostics, "manifest.nodes[1].panels[0].selector.kind")
        self.assertDiagnostic(diagnostics, "manifest.extensions['not_namespaced']")

    def test_malformed_values_report_diagnostics_instead_of_crashing(self) -> None:
        def change(manifest, _run):
            manifest["artifacts"][0]["path"] = []
            manifest["nodes"][0]["id"] = []
            manifest["nodes"][0]["groupIds"] = []
            manifest["nodes"][1]["panels"][0]["selector"]["kind"] = []
            manifest["groups"] = [{"id": "g", "title": "G", "type": "phase", "memberNodeIds": []}]

        _run, diagnostics = self.mutate(change)
        self.assertDiagnostic(diagnostics, "manifest.artifacts[0].path: must be a string")
        self.assertDiagnostic(diagnostics, "manifest.nodes[0].id: must be a string")
        self.assertDiagnostic(diagnostics, "manifest.nodes[1].panels[0].selector.kind: must be a string")

    def test_cross_record_diagnostics_preserve_indexes_after_malformed_items(self) -> None:
        def change(manifest, _run):
            manifest["artifacts"].insert(0, None)
            manifest["artifacts"][1]["ownerNodeId"] = "missing"
            manifest["nodes"].insert(0, None)
            manifest["nodes"][1]["panels"][0]["artifactId"] = "missing"

        _run, diagnostics = self.mutate(change)
        self.assertDiagnostic(diagnostics, "manifest.artifacts[1].ownerNodeId")
        self.assertDiagnostic(diagnostics, "manifest.nodes[1].panels[0].artifactId")


class ReferenceTests(ValidatorTestCase):
    def test_all_reference_kinds_are_checked(self) -> None:
        cases = {
            "owner": (lambda m: m["artifacts"][0].update(ownerNodeId="missing"), "manifest.artifacts[0].ownerNodeId"),
            "panel": (lambda m: m["nodes"][0]["panels"][0].update(artifactId="missing"), "manifest.nodes[0].panels[0].artifactId"),
            "edge-from": (lambda m: m["edges"][0].update({"from": "missing"}), "manifest.edges[0].from"),
            "edge-to": (lambda m: m["edges"][0].update(to="missing"), "manifest.edges[0].to"),
            "group-member": (lambda m: m["groups"].append({"id": "g", "title": "G", "type": "phase", "memberNodeIds": ["missing"]}), "manifest.groups[0].memberNodeIds[0]"),
            "group-parent": (lambda m: m["groups"].append({"id": "g", "title": "G", "type": "phase", "memberNodeIds": [], "parentGroupId": "missing"}), "manifest.groups[0].parentGroupId"),
            "node-group": (lambda m: m["nodes"][0].update(groupIds=["missing"]), "manifest.nodes[0].groupIds[0]"),
            "entry": (lambda m: m["presentation"].update(entryNodeIds=["missing"]), "manifest.presentation.entryNodeIds[0]"),
            "featured": (lambda m: m["presentation"].update(featuredNodeIds=["missing"]), "manifest.presentation.featuredNodeIds[0]"),
            "result": (lambda m: m["presentation"].update(resultNodeIds=["missing"]), "manifest.presentation.resultNodeIds[0]"),
            "warning-node": (lambda m: m["warnings"].append({"message": "x", "nodeIds": ["missing"]}), "manifest.warnings[0].nodeIds[0]"),
            "warning-artifact": (lambda m: m["warnings"].append({"message": "x", "artifactIds": ["missing"]}), "manifest.warnings[0].artifactIds[0]"),
        }
        for name, (change, location) in cases.items():
            with self.subTest(name=name):
                run = self.workspace / name
                shutil.copytree(FIXTURES / "minimal-success", run)
                manifest = self.load_manifest(run)
                change(manifest)
                self.write_manifest(run, manifest)
                self.assertDiagnostic(VALIDATOR.validate(run), location)


class InventoryAndPathTests(ValidatorTestCase):
    def test_missing_source_and_duplicate_inventory_path(self) -> None:
        def change(manifest, _run):
            manifest["artifacts"] = [artifact for artifact in manifest["artifacts"] if artifact["path"] != "run.md"]
            duplicate = dict(manifest["artifacts"][0])
            duplicate["id"] = "a-request-copy"
            manifest["artifacts"].append(duplicate)

        _run, diagnostics = self.mutate(change)
        self.assertDiagnostic(diagnostics, "source:run.md: missing artifact inventory record")
        self.assertDiagnostic(diagnostics, "duplicate inventory path 'request.md'")

    def test_present_application_files_must_be_inventoried(self) -> None:
        def change(_manifest, run):
            (run / "applications" / "001-answer" / "inputs").mkdir()
            (run / "applications" / "001-answer" / "inputs" / "topic.md").write_text("topic\n", encoding="utf-8")

        _run, diagnostics = self.mutate(change)
        self.assertDiagnostic(diagnostics, "source:applications/001-answer/inputs/topic.md")

    def test_unsafe_lexical_paths_are_rejected(self) -> None:
        paths = ("/tmp/file.md", "../file.md", "https://example.com/x", "inputs\\x.md", "inputs//x.md", "./request.md", "request.md/", "bad\0name.md")
        for index, path in enumerate(paths):
            with self.subTest(path=path):
                run = self.workspace / f"unsafe-{index}"
                shutil.copytree(FIXTURES / "minimal-success", run)
                manifest = self.load_manifest(run)
                manifest["artifacts"][0]["path"] = path
                self.write_manifest(run, manifest)
                self.assertDiagnostic(VALIDATOR.validate(run), "manifest.artifacts[0].path")

    def test_candidate_manifest_must_resolve_inside_run(self) -> None:
        run = self.copy_fixture()
        outside = self.workspace / "outside.json"
        shutil.copy2(run / "view" / "manifest.json", outside)
        candidate = run / "view" / "manifest.test-generation.next.json"
        candidate.symlink_to(outside)
        self.assertDiagnostic(VALIDATOR.validate(run, candidate), "manifest resolves outside the run root")

    def test_hidden_and_view_artifact_records_are_rejected(self) -> None:
        run = self.copy_fixture()
        (run / ".secret.md").write_text("secret", encoding="utf-8")
        manifest = self.load_manifest(run)
        manifest["artifacts"].extend([
            {"id": "a-hidden", "path": ".secret.md", "mediaType": "text/markdown", "role": "other", "title": "Hidden"},
            {"id": "a-view", "path": "view/notes.md", "mediaType": "text/markdown", "role": "other", "title": "Notes"},
        ])
        self.write_manifest(run, manifest)
        diagnostics = VALIDATOR.validate(run)
        self.assertDiagnostic(diagnostics, "manifest.artifacts[9].path: hidden files")
        self.assertDiagnostic(diagnostics, "manifest.artifacts[10].path: view/")

    def test_file_symlink_escape_is_rejected(self) -> None:
        run = self.copy_fixture()
        outside = self.workspace / "outside.md"
        outside.write_text("outside\n", encoding="utf-8")
        (run / "escape.md").symlink_to(outside)
        manifest = self.load_manifest(run)
        manifest["artifacts"].append({"id": "a-escape", "path": "escape.md", "mediaType": "text/markdown", "role": "other", "title": "Escape"})
        self.write_manifest(run, manifest)
        self.assertDiagnostic(VALIDATOR.validate(run), "manifest.artifacts[9].path: referenced file resolves outside")

    def test_missing_and_directory_artifact_targets_are_rejected(self) -> None:
        def change(manifest, _run):
            manifest["artifacts"][0]["path"] = "missing.md"
            manifest["artifacts"][1]["path"] = "applications"

        _run, diagnostics = self.mutate(change)
        self.assertDiagnostic(diagnostics, "manifest.artifacts[0].path: referenced file does not exist")
        self.assertDiagnostic(diagnostics, "manifest.artifacts[1].path: referenced artifact is not a regular file")


class ApplicationTests(ValidatorTestCase):
    def test_missing_application_node(self) -> None:
        def change(manifest, _run):
            manifest["nodes"] = [manifest["nodes"][0]]
            manifest["edges"] = []
            manifest["presentation"] = {"entryNodeIds": ["n-request"], "featuredNodeIds": [], "resultNodeIds": ["n-request"]}
            for artifact in manifest["artifacts"]:
                artifact.pop("ownerNodeId", None)

        _run, diagnostics = self.mutate(change)
        self.assertDiagnostic(diagnostics, "applications/001-answer: runtime application directory has no application node")

    def test_duplicate_application_mapping(self) -> None:
        def change(manifest, _run):
            duplicate = json.loads(json.dumps(manifest["nodes"][1]))
            duplicate["id"] = "n-answer-copy"
            manifest["nodes"].append(duplicate)

        _run, diagnostics = self.mutate(change)
        self.assertDiagnostic(diagnostics, "duplicate application mapping for 'applications/001-answer'")

    def test_application_directory_must_be_exact(self) -> None:
        def change(manifest, run):
            (run / "applications" / "001-answer" / "nested").mkdir()
            manifest["nodes"][1]["application"]["directory"] = "applications/001-answer/nested"

        _run, diagnostics = self.mutate(change)
        self.assertDiagnostic(diagnostics, "manifest.nodes[1].application.directory: must name exactly applications/<application-id>")

    def test_application_directory_symlink_escape_is_rejected(self) -> None:
        run = self.copy_fixture()
        outside = self.workspace / "outside-app"
        outside.mkdir()
        (run / "applications" / "002-escape").symlink_to(outside, target_is_directory=True)
        manifest = self.load_manifest(run)
        node = json.loads(json.dumps(manifest["nodes"][1]))
        node["id"] = "n-escape"
        node["status"] = "running"
        node["application"]["directory"] = "applications/002-escape"
        node["panels"] = []
        manifest["nodes"].append(node)
        self.write_manifest(run, manifest)
        diagnostics = VALIDATOR.validate(run)
        self.assertDiagnostic(diagnostics, "applications/002-escape: application directory resolves outside")
        self.assertDiagnostic(diagnostics, "manifest.nodes[2].application.directory: referenced directory resolves outside")

    def test_application_metadata_on_other_node_still_obeys_containment(self) -> None:
        def change(manifest, _run):
            manifest["nodes"][0]["application"] = {"directory": "applications/missing"}

        _run, diagnostics = self.mutate(change)
        self.assertDiagnostic(diagnostics, "manifest.nodes[0].application.directory: referenced directory does not exist")

    def test_succeeded_application_requires_canonical_result(self) -> None:
        run = self.copy_fixture()
        (run / "applications" / "001-answer" / "result.md").unlink()
        manifest = self.load_manifest(run)
        manifest["artifacts"] = [artifact for artifact in manifest["artifacts"] if artifact["id"] != "a-result"]
        manifest["nodes"][1]["panels"] = [panel for panel in manifest["nodes"][1]["panels"] if panel["id"] != "result"]
        self.write_manifest(run, manifest)
        self.assertDiagnostic(VALIDATOR.validate(run), "manifest.nodes[1].status: succeeded application has no canonical")

    def test_canonical_result_requires_succeeded_application(self) -> None:
        def change(manifest, _run):
            manifest["nodes"][1]["status"] = "failed"
            manifest["run"]["status"] = "partial"

        _run, diagnostics = self.mutate(change)
        self.assertDiagnostic(diagnostics, "manifest.nodes[1].status: application with a canonical result.md")

    def test_application_node_requires_status(self) -> None:
        def change(manifest, _run):
            del manifest["nodes"][1]["status"]

        _run, diagnostics = self.mutate(change)
        self.assertDiagnostic(diagnostics, "manifest.nodes[1].status: required for an application node")
        self.assertDiagnostic(diagnostics, "application with a canonical result.md must have status 'succeeded'")


class ResultsAndGroupsTests(ValidatorTestCase):
    def test_succeeded_run_requires_result_root(self) -> None:
        def change(manifest, _run):
            manifest["presentation"]["resultNodeIds"] = []

        _run, diagnostics = self.mutate(change)
        self.assertDiagnostic(diagnostics, "manifest.presentation.resultNodeIds: a succeeded run")

    def test_returned_application_requires_its_result_panel(self) -> None:
        def change(manifest, _run):
            manifest["nodes"][1]["panels"] = [
                panel for panel in manifest["nodes"][1]["panels"] if panel["role"] != "result"
            ]

        _run, diagnostics = self.mutate(change)
        self.assertDiagnostic(diagnostics, "returned application must expose canonical accepted content")

    def test_non_result_node_type_cannot_be_returned(self) -> None:
        def change(manifest, _run):
            manifest["presentation"]["resultNodeIds"] = ["n-request"]

        _run, diagnostics = self.mutate(change)
        self.assertDiagnostic(diagnostics, "returned node must have type 'application' or 'result'")

    def test_structural_result_node_requires_an_accepted_result_panel(self) -> None:
        run = self.copy_fixture()
        manifest = self.load_manifest(run)
        manifest["nodes"].append({
            "id": "n-collection",
            "type": "result",
            "title": "Returned collection",
            "emphasis": "primary",
            "panels": [],
        })
        manifest["presentation"]["resultNodeIds"] = ["n-collection"]
        self.write_manifest(run, manifest)
        self.assertDiagnostic(
            VALIDATOR.validate(run),
            "returned result node must expose canonical accepted content",
        )

        manifest["nodes"][-1]["panels"] = [{
            "id": "final",
            "label": "Returned collection",
            "artifactId": "a-final",
            "role": "result",
            "renderAs": "markdown",
        }]
        self.write_manifest(run, manifest)
        self.assertEqual([], VALIDATOR.validate(run))

    def test_attempt_cannot_masquerade_as_accepted_result(self) -> None:
        run = self.copy_fixture()
        attempts = run / "applications" / "001-answer" / "attempts"
        attempts.mkdir()
        (attempts / "001-failure.md").write_text("failed\n", encoding="utf-8")
        manifest = self.load_manifest(run)
        manifest["artifacts"].append({"id": "a-attempt", "path": "applications/001-answer/attempts/001-failure.md", "mediaType": "text/markdown", "role": "attempt", "title": "Rejected attempt"})
        manifest["nodes"][1]["panels"][0]["artifactId"] = "a-attempt"
        self.write_manifest(run, manifest)
        self.assertDiagnostic(VALIDATOR.validate(run), "manifest.nodes[1].panels[0].artifactId: result panel must not reference")

    def test_ordinary_artifact_cannot_masquerade_as_accepted_result(self) -> None:
        def change(manifest, _run):
            manifest["nodes"][1]["panels"][0]["artifactId"] = "a-request"

        _run, diagnostics = self.mutate(change)
        self.assertDiagnostic(diagnostics, "manifest.nodes[1].panels[0].artifactId: result panel must reference a canonical accepted result artifact")

    def test_application_result_panel_must_reference_its_own_result(self) -> None:
        run = self.copy_fixture()
        other = run / "applications" / "002-other"
        other.mkdir()
        for name in ("prompt.md", "result.md", "status.md"):
            (other / name).write_text(f"# {name}\n", encoding="utf-8")
        manifest = self.load_manifest(run)
        manifest["artifacts"].extend([
            {"id": "a-other-prompt", "path": "applications/002-other/prompt.md", "mediaType": "text/markdown", "role": "application-prompt", "title": "Other prompt"},
            {"id": "a-other-result", "path": "applications/002-other/result.md", "mediaType": "text/markdown", "role": "application-result", "title": "Other result"},
            {"id": "a-other-status", "path": "applications/002-other/status.md", "mediaType": "text/markdown", "role": "application-status", "title": "Other status"},
        ])
        other_node = json.loads(json.dumps(manifest["nodes"][1]))
        other_node["id"] = "n-other"
        other_node["application"]["directory"] = "applications/002-other"
        other_node["panels"] = []
        manifest["nodes"].append(other_node)
        manifest["nodes"][1]["panels"][0]["artifactId"] = "a-other-result"
        self.write_manifest(run, manifest)
        self.assertDiagnostic(
            VALIDATOR.validate(run),
            "manifest.nodes[1].panels[0].artifactId: application result panel must reference its own canonical result.md",
        )

    def test_cli_escapes_unencodable_diagnostics_and_exits_nonzero(self) -> None:
        run = self.copy_fixture()
        manifest = self.load_manifest(run)
        manifest["artifacts"][0]["path"] = "\ud800"
        self.write_manifest(run, manifest)
        completed = subprocess.run(
            [sys.executable, str(VALIDATOR_PATH), str(run)],
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(1, completed.returncode)
        self.assertIn("manifest.artifacts[0].path", completed.stderr)
        self.assertIn(r"artifact:\ud800", completed.stderr)

    def test_attempt_and_canonical_result_roles_are_enforced(self) -> None:
        run = self.copy_fixture()
        attempts = run / "applications" / "001-answer" / "attempts"
        attempts.mkdir()
        (attempts / "001-failure.md").write_text("failed\n", encoding="utf-8")
        manifest = self.load_manifest(run)
        manifest["artifacts"][6]["role"] = "attempt"
        manifest["artifacts"].append({"id": "a-attempt", "path": "applications/001-answer/attempts/001-failure.md", "mediaType": "text/markdown", "role": "application-result", "title": "Wrong"})
        self.write_manifest(run, manifest)
        diagnostics = VALIDATOR.validate(run)
        self.assertDiagnostic(diagnostics, "manifest.artifacts[6].role: canonical application result.md")
        self.assertDiagnostic(diagnostics, "manifest.artifacts[9].role: files under application attempts/")

    def test_group_parent_cycle_is_rejected(self) -> None:
        def change(manifest, _run):
            manifest["groups"] = [
                {"id": "g-one", "title": "One", "type": "phase", "memberNodeIds": [], "parentGroupId": "g-two"},
                {"id": "g-two", "title": "Two", "type": "phase", "memberNodeIds": [], "parentGroupId": "g-one"},
            ]

        _run, diagnostics = self.mutate(change)
        self.assertDiagnostic(diagnostics, "manifest.groups: parentGroupId cycle")

    def test_deep_acyclic_group_chain_is_valid(self) -> None:
        run = self.copy_fixture()
        manifest = self.load_manifest(run)
        manifest["groups"] = [
            {
                "id": f"g-{index}",
                "title": f"Group {index}",
                "type": "phase",
                "memberNodeIds": [],
                **({"parentGroupId": f"g-{index - 1}"} if index else {}),
            }
            for index in range(2000)
        ]
        self.write_manifest(run, manifest)
        self.assertEqual([], VALIDATOR.validate(run))

    def test_deep_group_cycle_returns_a_diagnostic(self) -> None:
        run = self.copy_fixture()
        manifest = self.load_manifest(run)
        manifest["groups"] = [
            {
                "id": f"g-{index}",
                "title": f"Group {index}",
                "type": "phase",
                "memberNodeIds": [],
                "parentGroupId": f"g-{index - 1}" if index else "g-1999",
            }
            for index in range(2000)
        ]
        self.write_manifest(run, manifest)
        self.assertDiagnostic(VALIDATOR.validate(run), "manifest.groups: parentGroupId cycle")

    def test_reverse_group_membership_must_agree(self) -> None:
        def change(manifest, _run):
            manifest["groups"] = [{"id": "g", "title": "Answers", "type": "phase", "memberNodeIds": ["n-answer"]}]
            manifest["nodes"][1]["groupIds"] = []

        _run, diagnostics = self.mutate(change)
        self.assertDiagnostic(diagnostics, "manifest.nodes[1].groupIds: reverse membership")

    def test_matching_reverse_group_membership_passes(self) -> None:
        run = self.copy_fixture()
        manifest = self.load_manifest(run)
        manifest["groups"] = [{"id": "g", "title": "Answers", "type": "phase", "memberNodeIds": ["n-answer"]}]
        manifest["nodes"][1]["groupIds"] = ["g"]
        self.write_manifest(run, manifest)
        self.assertEqual([], VALIDATOR.validate(run))

    def test_canonical_notes_are_required_and_symlink_safe(self) -> None:
        run = self.copy_fixture()
        notes = run / "view" / "notes.md"
        notes.unlink()
        self.assertDiagnostic(VALIDATOR.validate(run), "view/notes.md: canonical bundle requires")

        outside = self.workspace / "outside-notes.md"
        outside.write_text("outside\n", encoding="utf-8")
        notes.symlink_to(outside)
        self.assertDiagnostic(VALIDATOR.validate(run), "view/notes.md: notes.md resolves outside")


if __name__ == "__main__":
    unittest.main()
