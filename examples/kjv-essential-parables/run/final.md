# KJV Essential Structure: Twelve Parables

Status: **Succeeded** · [Program](program.md) · [Interpretation](interpretation.md) · [Run log](run.md)

## Results

### 1. Deterministic draw receipt and selected bundles

[Standalone result](applications/001-deterministic-draw/result.md)

### selectedEntries

1. Arendt — clear conceptual distinctions; plurality, action, and judgment as pressures; institutional conditions made morally visible.
2. James Baldwin — moral intimacy; witness joined to self-implication; lyrical clarity; social truth carried through human relation.
3. Emil Cioran — compressed metaphysical pessimism; paradox; exhaustion and negation treated as thought experiments.

### receipt

- Seed: `2026-08-01T12:34:43-0400`
- Extracted digit string: `202608011234430400`
- Digits, indexed from 1: `d[1..18] = [2, 0, 2, 6, 0, 8, 0, 1, 1, 2, 3, 4, 4, 3, 0, 4, 0, 0]`
- First selection:
  - Formula: `1 + ((sum(j * d[j], j = 1..18)) mod 16)`
  - Evaluated sum: `2 + 0 + 6 + 24 + 0 + 48 + 0 + 8 + 9 + 20 + 33 + 48 + 52 + 42 + 0 + 64 + 0 + 0 = 356`
  - Evaluated position: `1 + (356 mod 16) = 1 + 4 = 5`
  - Lookup: position 5 in the original 16-entry pool is source label `Arendt`.
  - Removal: remove original-pool entry 5, leaving original source positions `[1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]`.
- Second selection:
  - Formula: `1 + ((sum((j + 3) * d[j], j = 1..18)) mod 15)`
  - Evaluated sum: `sum(j * d[j]) + 3 * sum(d[j]) = 356 + 3 * 40 = 476`
  - Evaluated position: `1 + (476 mod 15) = 1 + 11 = 12`
  - Removal-aware lookup: position 12 in `[1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]` is original source position 13, label `James Baldwin`.
  - Removal: remove original-pool entry 13, leaving original source positions `[1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16]`.
- Third selection:
  - Formula: `1 + ((sum((j * j + 1) * d[j], j = 1..18)) mod 14)`
  - Evaluated sum: `4 + 0 + 20 + 102 + 0 + 296 + 0 + 65 + 82 + 202 + 366 + 580 + 680 + 591 + 0 + 1028 + 0 + 0 = 4016`
  - Evaluated position: `1 + (4016 mod 14) = 1 + 12 = 13`
  - Removal-aware lookup: position 13 in `[1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16]` is original source position 15, label `Emil Cioran`.
- Selected source labels in draw order: `[Arendt, James Baldwin, Emil Cioran]`

### 2. Major.minor outline

[Standalone result](applications/003-build-major-minor-outline/result.md)

The following is one coherent structural reading of the King James Bible, not a uniquely canonical outline.

## 1. Creation, Covenant, and Law

### 1.1 Creation, Ruin, and the Nations

**Scope:** Genesis from creation through Babel.  
**Central material:** God creates an ordered world and human beings in his image; human disobedience brings alienation and death; Cain, the flood, and Babel extend the pattern of sin, judgment, preservation, and dispersed nations.

### 1.2 The Patriarchs and the Covenant Promise

**Scope:** The stories of Abraham, Isaac, Jacob, and Joseph.  
**Central material:** God calls one family through whom blessing is promised to the nations, pledging land and descendants; faith, failure, providence, and reconciliation carry that family from Canaan into Egypt.

### 1.3 Exodus, Sinai, and the Wilderness

**Scope:** Exodus through Deuteronomy.  
**Central material:** God delivers Israel from slavery, establishes covenant at Sinai, orders worship and communal holiness through law and tabernacle, disciplines rebellion in the wilderness, and renews the covenant before entry into the land.

## 2. Israel in the Land: Kingdom, Wisdom, and Prophetic Witness

### 2.1 Conquest, Settlement, and the Age of the Judges

**Scope:** Joshua, Judges, and Ruth.  
**Central material:** Israel enters and apportions the promised land, then repeatedly falls into unfaithfulness, oppression, and rescue; Ruth offers a smaller story of loyal love, providence, and the family line leading toward David.

### 2.2 Monarchy, Division, Exile, and Return

**Scope:** Samuel through Esther, including the parallel royal record in Chronicles and the restoration accounts of Ezra and Nehemiah.  
**Central material:** Israel demands a king; David receives a dynastic promise; Solomon builds the temple; the kingdom divides and declines under idolatry and injustice; exile follows, yet a remnant returns to rebuild temple, city, and communal life under continuing foreign rule.

### 2.3 Prayer, Suffering, and the Search for Wisdom

**Scope:** Job, Psalms, Proverbs, Ecclesiastes, and the Song of Solomon.  
**Central material:** Israel's writings voice lament, praise, trust, royal hope, undeserved suffering, practical moral formation, life's apparent futility, reverence before God, and the delight and fidelity of human love.

### 2.4 Prophetic Judgment and Restorative Hope

**Scope:** Isaiah through Malachi.  
**Central material:** The prophets confront covenant breach, corrupt worship, exploitation, and reliance on worldly power; they interpret invasion and exile as judgment while announcing return, renewed hearts, a restored people, divine kingship, and hope focused through an anointed deliverer and the day of the Lord.

## 3. Jesus Christ and the Mission of the Early Church

### 3.1 The Gospel of the Kingdom in Jesus

**Scope:** Matthew, Mark, Luke, and John.  
**Central material:** Four complementary witnesses present Jesus as Israel's Messiah and God's Son, proclaiming the kingdom through teaching, parables, signs, mercy, and conflict, and bringing his mission to its climax in crucifixion, resurrection, and commission.

### 3.2 The Spirit-Empowered Witness from Jerusalem to Rome

**Scope:** Acts.  
**Central material:** The risen Jesus' followers receive the Holy Ghost, form a worshiping and sharing community, endure opposition, cross ethnic boundaries, and carry the gospel through the ministries of Peter, Paul, and others from Jerusalem into the wider Roman world.

## 4. Apostolic Formation and Consummation

### 4.1 Paul's Gospel and the Life of the Churches

**Scope:** Romans through Philemon.  
**Central material:** Paul's letters expound sin, grace, justification, union with Christ, life in the Spirit, resurrection, and the joining of Jew and Gentile, while addressing worship, ethics, suffering, leadership, reconciliation, and unity in particular congregations and coworkers.

### 4.2 Persevering Faith in the General Epistles

**Scope:** Hebrews through Jude.  
**Central material:** These writings call believers to endure by trusting Christ's sufficient priesthood, embodying faith in obedient action, resisting false teaching, practicing holy love, suffering faithfully, and holding to the apostolic hope.

### 4.3 Revelation, Judgment, and New Creation

**Scope:** Revelation.  
**Central material:** Symbolic visions unveil the risen Christ's rule amid persecuted churches, the conflict between divine sovereignty and idolatrous empire, final judgment over evil, the victory of the Lamb, and the descent of a renewed creation where God dwells with his people.

Terminal leaf count: 12

### Leaf 1.1 — Creation, Ruin, and the Nations

[Standalone result](applications/006-leaf-1-1-parable/result.md)

### The Stones We Carry

In the town of Lorn, every injury became a stone by morning.

A careless word might leave a pebble on the speaker’s sill. A betrayal could block a lane. When the council condemned a family, a wall rose before their house, though no mason had been paid and no quarry stood for fifty miles. The stones did not disappear when those who had caused them died. Children inherited the walls, along with the houses and the names.

No hammer could break them. But any person could lift one stone from any wall, and wherever that person carried it, the gap remained open. If the stone was set down, it flew back at once to its former place.

The council built shelves into its chambers so its members might rest their stones during meetings. They called this practical. “A town cannot govern with both hands occupied,” they said, and while they debated which streets deserved gates, the stones returned to the walls.

Others refused to touch stones they had not made. Among them was Mara the baker, whose grandfather’s ovens stood behind a wall raised before she was born.

“I did not accuse your family,” she told Tomas, whose doorway faced hers across the wall. “Why should my back answer for a dead man’s mouth?”

Tomas nodded. He had asked himself the same question. Yet each morning his daughter walked the long way to Mara’s ovens, where she was apprenticed, and each evening she returned after dark.

Some citizens carried stones proudly. They polished them, engraved them with the names of those they aided, and hired children to announce their approach. Their gaps were wide, though people learned to step aside when the bearers passed.

Some carried quietly until their shoulders bent. When urged to rest, they answered that the wall would close. Sometimes this sounded like courage. Sometimes it sounded like a threat.

Mara watched them all from her upper window. She knew which stones in the town were hers. There were seven: two from sharp words, one from a cheated measure, four from the winter when she had kept her ovens for those who could pay. She carried none of them. Knowledge, she believed, was at least cleaner than display.

Then Tomas’s daughter failed to arrive.

At sunset Mara found her on the far side of town, feverish beside the longest wall in Lorn. Tomas stood before it holding three stones already, unable to free another hand. The nearest gap was narrow. A person could pass through it, but not while carrying a child.

Mara placed her palms against the wall. The stone she chose bore no mark. It might have come from the council’s decree, or from Tomas’s grandfather, or from someone whose name neither family remembered.

“If I take it,” she said, “it will not become mine.”

“No,” Tomas said.

“But I will have to carry it.”

“Yes.”

She lifted. The stone was heavier than bread flour and warmer than flesh. Tomas carried his daughter through the widened place.

You may follow them, if you like. To do so, you must decide whether to pass through before Mara’s strength fails, or take the stone from her hands.

Beyond the wall, the lamps of Lorn were being lit. Mara stood in the opening, the stone against her breast, while on both sides of her the road disappeared into evening.

### Leaf 1.2 — The Patriarchs and the Covenant Promise

[Standalone result](applications/009-leaf-1-2-parable/result.md)

### The Lamp at Midnight

On the island of Vey, every flame died at midnight except the flame in the window of one house.

No one knew why. The house was neither oldest nor grandest. Its roof leaked, its shutters hung crooked, and its inhabitants—the Orra family—were famous for debts, reconciliations, and quarrels that began in the kitchen and ended in the street. Yet when the last bell sounded and ovens, beacons, and bedside lamps went black, the Orra flame remained.

For generations the family carried it through the island before dawn. At each door they touched wick to wick. In return, the Council excused their taxes and set two guards at their gate.

“The guards are not an honor,” said Mara Orra to her grandfather. “They are a wall around what everyone needs.”

Old Senn turned the brass key in his palm. He had once dropped the lamp during a winter crossing and still walked with a burn along his hand. “A wall also keeps the wind out.”

The family had rules: only an Orra might enter the lamp room; only Senn might trim the wick; no stranger’s vessel could touch its oil. These rules had preserved the flame through riots, storms, and one terrible year when Mara’s father sold places at the front of the line. The Council punished him, but the far villages remembered whose children had shivered while merchants’ halls blazed.

Mara began meeting those villagers beyond the gate. She lit their lamps first and taught them the roads between houses so they could carry the fire onward. Soon the morning circuit took half the time. The fishers called her generous. Senn called her careless, though softly, as if naming a fever.

Then refugees came from the southern shoals, bringing clay lamps shaped unlike any on Vey. The Council declared that the Orra flame belonged to island households recorded in the census. There was not enough time before dawn, the councillors said, to light every vessel carried in from the sea.

Senn obeyed. He had watched crowds crush a child against the gate years before. Order, to him, had faces too.

Mara disobeyed. She saw a woman sheltering an unlit lamp beneath her coat while her son warmed his hands over nothing. Mercy, to her, had faces too.

Their argument divided the house. One cousin warned that if everyone entered, the lamp room would become a marketplace. Another asked what use was a flame preserved from every hand and every breath. Mara’s mother said nothing. She scrubbed soot from the window until the people outside could see the family eating.

Perhaps you would have stood with Senn at the narrow door, counting vessels so no frightened crowd could extinguish the one fire left. Perhaps you would have stood with Mara at the gate, refusing to ask where cold hands were born. In either place, someone behind you would have mistaken your body for a barrier.

On the longest night, the refugees returned in silence. Senn waited inside with the lamp. Mara stood outside with the brass key. Between them, in the open doorway, the midnight wind moved the flame sideways without putting it out.

The woman from the shoals lifted her strange clay vessel. Senn raised one burned hand toward the door. Mara placed the key on the threshold, and no one yet had stooped to take it.

### Leaf 1.3 — Exodus, Sinai, and the Wilderness

[Standalone result](applications/012-leaf-1-3-parable/result.md)

### The Winter Keys

The town of Orra stood on the far side of a gorge, where its founders had fled after years in the quarries. The Warden of the Pass had opened the quarry gates and led them across a bridge no map had shown. Then he gave them one rule.

On the first night of snow, every key in Orra was to be placed in the iron socket at the center of the bridge. Until spring, no door could be locked. While all the keys remained there, the bridge would bear any weight. If even one was withheld, its stones began to loosen.

No one knew why. The Warden never crossed into town, and no messenger had seen his face.

For forty winters the people obeyed. Collectors went from house to house with a cedar bowl. At each threshold a clerk recorded the surrender, and a neighbor witnessed it. The keys were carried to the bridge in procession, bright as minnows in the bowl.

Mara's mother always gave hers gladly. She had been a girl in the quarries. "A locked door did not save us there," she said. "An open road did."

Their neighbor Iven kept a different memory. During the seventh winter, when every door stood open, someone had taken the medicine from his son's bedside. The boy survived, but only narrowly. Each year afterward, Iven laid his key in the bowl with both hands closed around it.

"A command may open one gate and still close another," he told the clerk.

"And a private lock may bring the bridge down on a hundred travelers," the clerk replied. She had carried a woman in labor across those stones during a blizzard. She did not speak harshly.

Mara's father was the town locksmith. On the morning before the forty-first snow, he showed Mara a small brass key sewn inside his coat. It opened the records house, where the deeds, births, debts, and pardons of Orra were kept.

"The collectors believe this key was melted years ago," he said. "If fire comes, someone must be able to enter. A rule for everyone requires someone outside it."

Mara looked through the window toward the bridge. A hairline crack had appeared beneath the iron socket. Surveyors blamed frost. The elders blamed Iven, who had at last refused the cedar bowl. Iven sat behind his locked door while townspeople gathered in the lane: some carrying food for him, some stones.

The council ordered Mara's father to make an instrument that would open Iven's door. He worked all afternoon, then left the instrument unfinished on his bench.

That night the crack widened. Beyond the gorge, three wagons waited with flour enough for the winter. The bridge held, but each gust shook pale dust from its joints.

If you had lived in Orra, perhaps you would have stood with Mara's mother, watching the road that had once delivered her. Perhaps you would have sat beside Iven, one hand on the medicine chest. Perhaps you would have thanked the clerk for counting what no single household could afford to forget.

Mara walked alone to the bridge with the hidden key in her palm. At the iron socket she found Iven already there, carrying his own key and the locksmith's unfinished instrument.

Neither spoke. Snow collected on the wagons across the gorge. Behind them, every door in Orra stood open except one.

Mara held the brass key over the socket. Iven laid the instrument on the parapet. Far below, the river moved in darkness, and between one bank and the other the bridge gave a low sound, almost like a voice beginning.

### Leaf 2.1 — Conquest, Settlement, and the Age of the Judges

[Standalone result](applications/015-leaf-2-1-parable/result.md)

# The Drum Under the Hall

In the town of Marrow, beneath the council hall, there was a drum no wider than a supper table. When it was struck, everyone who heard it knelt—friend, stranger, horseman, judge. No one knew who had stretched its pale hide or why its voice entered the knees before it entered the ear.

There was one further fact, learned slowly and never disputed. After the drum sounded, the children born in Marrow carried its rhythm beneath their own heartbeats. As they grew, they could hear in every conversation a place where someone might be made to kneel.

For seventy years the drum had been silent.

Then the Lord of Salt crossed the western ridge. His men emptied farms, marked doors for seizure, and sent word that Marrow must yield its granaries and twelve children each winter. At the eastern gate, families arrived with bedding on their backs and ash in their hair.

The council met above the buried drum. Tovin, keeper of the gate, laid his sword on the table. His sister Sela, who taught the town's children, laid beside it a slate on which a boy had written: A house is where no one is sent away.

“Open the chamber,” Tovin said. “One stroke, and the riders kneel. We need not kill them. We may take their weapons, feed them, and send them home walking.”

He spoke without relish. His own son had been taken in the first raid.

Sela touched the chalk sentence. “And afterward?”

“Afterward there will be children,” he said. “That is not a small thing.”

The miller, whose fields were already burning, agreed with him. She remembered the drum-born elders of her childhood: harsh people, some of them, but also the ones who had raised the flood wall, rationed grain fairly, and stood between debtors and the old magistrate. “A rhythm is not a command,” she said. “Children can be taught another dance.”

Sela looked through the high window toward the schoolyard. The pupils had divided themselves into riders and townsfolk. One child sat on the well cover beating a bucket. At every beat, half the children dropped laughing to their knees. Soon they were arguing over who might hold the stick.

That evening, two processions formed.

Tovin led the first down the council stairs. He carried no sword now. Behind him walked the miller, the bereaved, and those who had seen what the Salt men left in the farmhouses. They brought ropes for prisoners and bread for after. Their faces bore the grave tenderness of people preparing to do a thing they hoped would spare even their enemies.

Sela led the second toward the eastern gate. With her went several teachers, three councillors, and families carrying seed in their pockets. They meant to cross the bare hills, where there were no walls and no promise of welcome. Their tenderness was no less grave. They left lamps burning in their windows so the town would not seem abandoned to those who stayed.

You may choose which procession to follow, but you must leave the square before the western riders arrive. If you descend, someone will place the drumstick in your hands. If you go east, a tired child will ask you to carry her.

At midnight, the two groups could still see each other's lights: torches moving under the hall, lanterns climbing the hill. Then a wind rose from the west. In the chamber, the pale drumskin tightened. On the ridge, Sela stopped and turned, the child asleep against her shoulder.

Far below, Tovin lifted the stick.

### Leaf 2.2 — Monarchy, Division, Exile, and Return

[Standalone result](applications/018-leaf-2-2-parable/result.md)

### The Last Boundary Stone

In the city of Vey, no public building could be reopened until the governor pressed his silver seal into its lintel. Whenever he did, one of the ancient boundary stones sank into the earth and could not be found again.

The people had returned to roofs split by weather and streets where thorn trees grew. They did not love the governor, who lived in the undamaged tower and spoke their names with care but never their language. Still, winter came, and a sealed granary kept flour dry. A sealed school gathered children who had learned only the distances between camps. A sealed court gave two widows somewhere to dispute an orchard without knives.

After each ceremony, the surveyors walked the perimeter. Where a stone had vanished, the governor’s clerks drew the city line inward.

Lio repaired the buildings. His sister Sera kept the old map.

“A border that cannot shelter anyone is only a boast,” Lio told her as they carried beams into the school. He had buried a son in the first winter, when there was no infirmary and no roof held against rain. He worked gently, even when hurried, because he said haste was how ruin entered new walls.

“A roof that teaches us to forget who remains outside is another kind of weather,” Sera answered. She visited the families beyond each redrawn line and copied their births into the city register, though the clerks crossed them out. She never called the reopened halls false. She brought chalk to the school and grain to the granary. But on festival days she stood beside the old map, naming the vanished stones.

Years passed. The city became warm and articulate. Children recited laws beneath sound rafters. Bakers argued over flour allocations, which was a kind of peace. At every lintel the silver seal shone like a small, patient moon.

Only the infirmary remained in ruins.

Only one boundary stone remained above ground. It stood on the eastern road, beyond which smoke from distant cooking fires could be seen at dusk.

The governor arrived with his seal. Lio had laid fresh cedar over the infirmary door. Inside, clean beds waited, and beside them stood women carrying feverish children. Sera waited at the eastern stone with the old map folded under her arm. Beyond her, figures had gathered on the road, too far away for their faces to be known.

The council asked the siblings to speak.

Lio touched the lintel. “The sick cannot sleep beneath a memory.”

Sera placed her palm on the stone. “Nor can a city become whole by making its wound illegal.”

No one cheered either of them. The mothers shifted the children on their shoulders. The builders lowered their eyes. Even the governor seemed tired of holding the silver weight.

You are among them now. There is room beside Lio under the cedar, and room beside Sera on the road. From either place you can hear a child coughing.

At sunset the governor raised the seal toward the lintel. Sera unfolded the map. Lio reached up, not for the seal, but for his sister’s free hand.

Between them, the last stone trembled in the dust.

### Leaf 2.3 — Prayer, Suffering, and the Search for Wisdom

[Standalone result](applications/021-leaf-2-3-parable/result.md)

### The Book Beside the Well

In the village of Oren, the well gave water only while every loss had a reason written beside it in the council's book.

No one knew why. The book had no lock, the well no chain. Yet whenever a line was left blank at sunset, the bucket returned dry at dawn.

So the village became practiced in reasons. A roof fell because its beams were green. A shepherd vanished because fog deceived him. When fever took three sisters, the physician wrote, *The summer was close and the body is a narrow house.* The phrasing comforted some and angered others, but the next morning there was water.

Mara kept the book. She had a patient hand and never wrote before visiting the bereaved. Her brother Enel tended the bell tower, and each noon he leaned from its highest window to wave at her in the square.

One windless morning, a stone dropped from the tower and killed Enel before the bell could strike.

The council gathered by noon. The mason found a split iron pin. "There is the cause," he said. He had warned the council about the pins in winter, but grain had been dear and iron dearer. The oldest councillor bowed his head. "Write neglect. Let the blame be ours."

Mara rested her palm on the empty line. "Neglect tells me why the stone fell," she said. "It does not tell me why it was permitted to fall on him."

The councillor answered without lifting his head. "No sentence can carry that weight. But the children will need water tomorrow."

At dusk the villagers came with jars. Some urged Mara to write *neglect*, because confession was better than excuse and thirst would not restore her brother. Some asked her to write *mystery*, because a small word could stand honestly where knowledge failed. The mason objected that mystery might wash guilt from human hands. Enel's widow said nothing for a long while. Then she asked Mara not to make the dead serve either the council's innocence or the village's courage.

Mara took up the pen.

If you had been there, perhaps you would have watched the nib rather than the widow. Most did. A few watched the well, as if its dark mouth were also waiting to learn what kind of truth they could afford.

Mara wrote: *The pin was split, the warning was deferred, and Enel stood beneath the stone.*

"That is an account," said the oldest councillor. "It is not a reason."

"It is all I can write without leaving him twice," Mara said.

The council did not close the book. No one ordered her to add another word. Instead they carried Enel through the square, and the mason walked beside the councillor, neither avoiding the other. Enel's widow held Mara's ink-stained hand.

Before dawn, the village formed a line at the well. The first bucket descended. Far below, it struck something with a sound that might have been water, or only stone answering stone.

No one pulled the rope.

### Leaf 2.4 — Prophetic Judgment and Restorative Hope

[Standalone result](applications/024-leaf-2-4-parable/result.md)

### The Stair Beneath the Tower

In the valley of Orra, the black wind came once in a lifetime. It entered the lungs of cattle, scoured bark from the orchards, and left human names difficult to remember.

There was one refuge. A stair would appear beneath the town's tower when the last stone of the tower had been removed. No one knew who had made this arrangement. The oldest songs began after it.

The tower was not merely high. Its lower rooms held the grain; its bell called children home through snow; its galleries housed the scales by which wool, salt, and mercy were measured. Envoys from the hill towns slept beneath its painted rafters, and the people said those towns kept their promises because they could see the tower from the passes.

So when a shepherd found black dust on the western lambs, the council did not begin with the roof.

"We have survived because we did not panic," said Mara, keeper of the grain keys. She had fed half the valley during the lean year and could name every household that still owed barley. "If we pull down the storehouse before the wind arrives, hunger will accomplish what the wind has not. Let us wait until certainty is no longer an insult to prudence."

Tovan the mason touched the wall. His grandfather had laid its upper courses. "A refuge bought by destroying the things that make us a people may shelter our breathing," he said, "but I do not know what else it shelters."

Yet Ansel, whose daughter had begun coughing black into a cloth, brought an iron lever at dawn.

The first stone he loosened bore, on its hidden face, the seal of a village drowned when Orra's millstream was diverted. The second had been cut with the crest of a defeated hill town. Behind the grain-room plaster they found children's tally marks, crossed out but still legible. Mara read the old accounts beside them and did not defend the numbers. Before sunset she opened the granary, canceled the barley debts, and sent wagons toward the families whose marks remained on the wall.

Some called this justice. Some called it emptying the valley before the wind could. Both helped load the wagons.

The envoys protested when their painted rooms were unroofed. Then one climbed the scaffolding and passed stones down with the others, saying treaties made under a visible tower might have to be remade where no town could overlook another. Another envoy rode home to close the pass.

You may stand where you like in the crowd: beside Mara, counting sacks against days; beside Ansel, counting breaths; beside Tovan, lowering the stone that carried his grandfather's mark. But if you remain until dusk, someone will put a rope in your hands.

For six days they dismantled the tower. As it shortened, distant farms disappeared from sight. The bell was lowered and lay mute in the square. The scales cracked. People who had never met without them argued over bread, then broke loaves by hand.

At last one foundation stone remained. The black wind had covered the western ridge. Beneath the stone's edge, a darkness no lamp had entered waited in the earth.

Mara held one end of the lever. Ansel held the other. Tovan knelt between them, his palm resting on the final stone as if feeling for a pulse.

From the northern road came the sound of wagons returning, though no one could yet see what they carried.

### Leaf 3.1 — The Gospel of the Kingdom in Jesus

[Standalone result](applications/027-leaf-3-1-parable/result.md)

### The Two Seats

In the river town of Hallow, judgment was given from a bench with two seats. The accused sat in the lower seat. The Keeper sat above him. Whatever sentence the Keeper spoke appeared first upon the Keeper's body: the welt, the hunger, the years of dimness, even the pallor of death. If the Keeper then stood, the sentence passed to the condemned. If he remained seated until the courthouse lamps went out, he bore it himself, and the accused walked free.

No one in Hallow remembered who had made the seats. No one tried to make others.

Mara kept the ferry with her younger brother, Oren. In winter they poled physicians across without charge, and in spring they carried children to the orchards. Their apprentice, Senn, slept beneath their roof and ate at their table.

One flood season Senn cut the ferry rope at night, hoping the untethered boat would be lost and its silver fittings blamed on river thieves. Oren heard the hull strike the quay and leapt aboard to save it. The current took both boat and brother. Senn sold the fittings downstream before dawn.

He confessed only when the empty ferry was found among the reeds.

At the hearing, half the town stood behind Mara. They had searched the banks with her. They had watched her set one bowl too many at supper. The other half stood behind Senn's mother, who had come barefoot through the rain and held her son's old coat as if he were still small enough to fit inside it.

The Keeper listened. He named the theft, the deceit, the broken welcome, and the death. He did not call the flood an accident. Then he sentenced Senn to twelve years in the quarry.

At once gray dust filled the Keeper's lungs. His hands split along the palms. His back bent as though beneath a stone basket.

“Stand,” Mara said.

The Keeper's clerk reached to help him, but he waved her away.

Senn's mother said nothing. She looked at Mara, not at the Keeper. After a while she crossed the aisle and placed the old coat on the floor between them.

“Do not ask me to carry him,” Mara said.

“I have not,” said the mother.

Behind them, townspeople began their familiar arguments. Some said a sentence that stayed on the bench made language weightless and taught clever hands to gamble with other lives. Others said the bench was the one place where suffering could end without being denied. The quarry master, who had buried two sons of his own, said punishment was not vengeance; it was the shape a town gave to its refusal to forget. The physician answered that scars remembered perfectly and understood nothing.

Senn lifted his head. “Make him stand,” he said. Whether he spoke from remorse, pride, or terror, no one could tell.

The lamps burned lower.

You may enter that courthouse from either door. From the east, you will stand near Mara and see the river mud still dried on her boots. From the west, you will smell stone dust on the Keeper's breath. There is no gallery. Wherever you stand, someone will feel you behind them.

At the final lamp, the Keeper gripped the bench and began to rise.

Mara stepped forward. Senn's mother did also. Between them lay the little coat, darkening where rain from the roof had found its way through.

### Leaf 3.2 — The Spirit-Empowered Witness from Jerusalem to Rome

[Standalone result](applications/030-leaf-3-2-parable/result.md)

# The House That Turned in the Night

On the salt plain stood one house large enough for all who had been born within sight of it. Beyond its walls, the night wind lifted the ground in white sheets and could polish a fence post to a needle before morning.

The house had one peculiarity. Whenever a stranger slept beneath its roof, the rooms changed places before dawn.

No one knew why. A pantry might wake beside the chimney, a stair might end where a cradle had stood, a door might open only to a hand that had never held its latch. The house never lost a room, but afterward no one could live in it entirely by memory.

Mara kept the ring of keys. Her brother, Iven, whose lungs had been burned in a salt storm, slept three steps from the stove. Each evening she crossed those steps in darkness to bring him water. She could do it carrying a full cup without spilling a drop.

Late one winter, a traveler named Sorel came to the threshold with a small brass bell tied at his wrist. Behind him the wind had already erased the road. He asked for one night.

The household gathered in the long room. Toman the mason spoke first. He had rebuilt the north wall after the last turning and still favored one shoulder.

“A roof is not cruel because it must remain a roof,” he said. “We have children who know where to run when the lamps go out.”

Old Nera, who had entered as a stranger fifty years before, touched the lintel above her. “This was once the granary,” she said. “They gave me its warmest corner. In the morning, the keys no longer knew their keepers. We learned again.”

“And some did not,” Mara said. Her hand closed around the iron ring. During that old turning, her mother had opened a door expecting the courtyard and found the cellar steps. She had walked with a stick ever since.

Sorel listened from outside. The bell at his wrist made no sound; he held it still with his other hand.

They argued until the fire settled into red seams. Some said the house existed to keep out the wind. Some said a house that admitted only those already inside was merely a larger body. Neither saying quieted the other.

If you had been there, perhaps you would have noticed what they did not: that everyone spoke from a place another person had once surrendered. Or perhaps you would only have heard the salt worrying the shutters and pictured Iven waking far from the stove.

At last Mara carried the keys to the threshold. She looked at Sorel, then at the dark passage behind her. She removed one key—the smallest, worn bright by generations of thumbs—and placed it on the sill between them.

No one knew whether it opened the door.

Sorel released his bell. It sounded once in the wind. Behind Mara, Iven lit a lamp and waited; behind Sorel, the plain had become indistinguishable from the sky.

The key lay half in the house and half in the gathering salt.

### Leaf 4.1 — Paul's Gospel and the Life of the Churches

[Standalone result](applications/033-leaf-4-1-parable/result.md)

### The Gate at Dusk

The gate of Lorn would close at dusk only if every household had hung above its door a round iron key.

No one knew why. The gate had stood before the oldest house, and the keys before the oldest memory. When the last round key was lifted to its hook, the gate drew itself shut with a sound like a deep breath. Behind it, children slept without listening for wolves.

One autumn, Mara came over the northern pass carrying a forked brass key. She mended roofs, sat beside the fevered, and knew how to find water beneath shale. By first snow, half the village had eaten at her stove. The other half had lent her something and received it back repaired.

When she asked for an empty house near the well, the wardens brought her a round iron key.

“Hang this one,” they said. “Keep the other wherever you please.”

Mara turned the iron key in her palm. “The brass key opened my mother’s house and her mother’s before her. A key hidden in a drawer is not a key being kept.”

The wardens did not mock her. They had buried children in years when the gate remained open. Their eldest, Senn, showed her the claw marks still visible on the eastern lintel.

“We ask no one to forget,” he said. “Only to help us close what guards us all.”

Mara looked at the marks for a long time. “Then let me hang mine.”

They tried. At dusk the gate shuddered but did not move.

Some villagers proposed that Mara remain forever a guest. They promised her food, work, and a place nearest the fire. A guest, however, could not speak when wells were divided or roofs assigned. A guest might be cherished and still be sent away.

Others offered to melt her brass key and cast it round. The village smith, who loved Mara, said he could preserve every shaving. Mara answered that memory kept in a pouch was not the same thing as a door that might yet be opened.

Then the midwife Anja took down her own iron key.

“If hers may not hang,” she said, “mine will not.”

Senn stood beneath Anja’s empty hook. “You can afford courage because others keep the wall for you.”

“Perhaps,” Anja said. “And perhaps you can afford certainty because others pay for it.”

That evening the gate remained open. The villagers lit fires along the road. Senn organized watches and took the coldest hour himself. Mara stood beside him with a spear she did not know how to use.

At midnight a wolf appeared beyond the last fire, watched them, and vanished. No one slept.

By morning, three more keys had come down. By noon, two went back up. Those who restored them were not cowards; they had heard their children crying from exhaustion. Those who left their hooks bare were not careless; they had seen Mara holding a lamp while Senn’s youngest slept against her shoulder.

Now you must enter Lorn before the light fails, because the northern wind has begun. You may pass beneath the gate and trust the wall. You may remain outside beside Mara’s small fire. Or you may take the empty house near the well, where two hooks have been driven above the door.

At sunset, Senn arrives carrying the round iron key. Mara arrives carrying the forked brass one. Neither reaches for a hook.

Between them, the gate begins its long breath.

### Leaf 4.2 — Persevering Faith in the General Epistles

[Standalone result](applications/036-leaf-4-2-parable/result.md)

### The Walking Lamp

In the village of Ansel, the winter lamp could not be extinguished, but it gave light only while someone carried it.

No one knew why. Set upon the council table, its blue flame remained perfect, yet the room went black. Lift it and take one step, and the rafters sprang into view. Walk with it into the snow, and the road shone as far as the next bend.

Each winter the council appointed bearers to circle the village from dusk until dawn. The route passed the shepherds’ huts, the sickhouse, and the northern wall where the wind could peel a mitten from a hand. Families left soup at their doors. Children woke to the moving light and knew the roofs had not vanished in the dark.

Sela and her brother Orrin carried the third watch together. She held the lamp; he walked beside her with oil they had never needed and a staff he often did. When the wind knocked Sela down, Orrin shielded the flame, though it required no shielding. When Orrin’s old wound opened, she shortened her stride, though the council bell was already calling them late.

One year the nights grew cruel, and two teachings divided Ansel.

The Resters said the lamp’s flame was the village’s security, not the bearers’ feet. They brought the lamp into the warm council chamber and sat around it in darkness. Their eldest had lost three sons on the northern wall; no one could call his caution cowardice. “If the flame is truly unfailing,” he said, “we need not make widows to assist it.”

The Milekeepers answered that light belonged to those who earned it. They recorded every circuit in a silver book and wore their frostbitten fingers uncovered. Their leader had carried medicine through a blizzard when all others refused; no one could call her severity empty. “Let the village see,” she said, “whose steps have purchased the morning.”

The council altered the routes, then altered them back. Doors went unvisited while arguments continued. The Resters accused the walkers of distrusting the flame. The Milekeepers accused the seated of loving darkness. Meanwhile the lamp burned flawlessly on the table and illuminated nothing.

On the longest night, Orrin could not rise from bed. Sela came to him with the lamp.

“Leave it,” he said. “It will burn.”

“Come with me,” she said. “I cannot carry you and it.”

He laughed once, without gladness. “Then we have finally learned what the flame is worth.”

Sela stood in the doorway. Behind her, the snow had covered both the official road and the forbidden shortcut. Ahead, in the room, her brother’s face was invisible. She took one step toward him, and light crossed the blankets. She took one step toward the road, and the sickhouse bell appeared through the storm.

You may say which step was first. The people of Ansel never agreed.

At dawn they found Orrin’s staff planted at the threshold. Beside it were two sets of footprints filling slowly with snow, and farther on, where the northern road bent out of sight, the small blue light was still moving.

### Leaf 4.3 — Revelation, Judgment, and New Creation

[Standalone result](applications/039-leaf-4-3-parable/result.md)

### The Wall That Listened

The sea-wall of Orra had one bronze face set into its eastern gate. At the first storm of winter, every citizen was required to pass before it and press both palms to its cheeks. If all did so, the wall held until spring. If one pair of hands was withheld, a crack opened opposite that person’s street.

No mason could explain this. The Governor could not explain it either, though his own face was stamped on every coin and resembled the face in the wall.

For sixty-three winters, the people of Netmakers’ Street had touched the bronze. They did not love the Governor. They loved their low houses, the smokehouses, the school with salt whitening its windows, and the old people who could no longer climb to the uplands.

In the sixty-fourth year, Sela the cooper said she would not go.

Her brother Marin found her planing a barrel stave while their mother slept beside the stove.

“Your hands are not yours alone,” he said. “Not in winter.”

Sela turned the pale curl of wood around one finger. “That is what he means us to say to one another.”

Marin had three children and a wife whose lungs filled easily with water. He had also hidden two fugitives beneath his fish cart the previous summer. He was not a coward, and Sela knew it. He knelt beside her bench and asked whether their mother could survive the hill road.

“No,” Sela said.

Between them lay the whole argument, breathing softly by the stove.

Word of Sela’s refusal spread. Some neighbors cursed her; others quietly carried blankets uphill. The schoolmistress announced that she would touch the face twice, if excess devotion could mend another’s absence. Old Teven, who had lost sons in the Governor’s mines, said he would stand behind Sela but would not let her choose the flooded rooms of children who had made no vow.

Then the Breakers came by night. They proposed to seize the Governor’s guards and chain them inside the threatened crack.

“Let the wall drink its masters,” their captain said.

For one fierce moment Sela saw justice shining there. Then she saw the youngest guard at the gate, who still had flour on his sleeve from his father’s bakery.

“No chains,” she said.

The captain laughed. “Then keep your clean hands and drown with them.”

The appointed morning came black with rain. One by one, the people entered the gatehouse. Some touched the bronze with tears. Some spat afterward. Some touched it tenderly, believing walls deserved gratitude whatever face they wore. Marin placed his palms against the cold cheeks and thought of the fugitives under his cart. Whether this made his hands faithful or false, he could not tell.

Now it is your turn in the line. Behind you, children cough beneath woolen hoods. Ahead, Sela stands with her hands closed. Beyond the gate, the Breakers wait without chains, though no one knows what they carry under their cloaks.

The bell sounds. Far out past the harbor, where sea and sky have erased their border, a white line appears. It may be the first wave of the storm. It may be morning.

Sela opens her hands.

## What happened

A fresh no-history compiler turned the natural-language request into a finite pure-text program, which the runner then interpreted and executed. Applications 001 and 003 ran concurrently: 001 performed the timestamp-seeded deterministic draw of three entries without replacement, selecting Arendt, James Baldwin, and Emil Cioran with an auditable receipt, while 003 attempted the major.minor outline. Application 002 then blended the three selected bundles into one anonymous craft-mechanism brief; writer labels were not passed to the parable workers.

The first outline result was rejected after exact-count validation found 13 terminal leaves, above the hard cap of 12. That malformed attempt was preserved unchanged, and the single allowed mechanical retry produced the accepted 12-leaf outline. The runner dynamically expanded those leaves, in order, into 12 independent three-application chains: a local heart-question adapter, one question-forge pass, and one parable application. Within each chain the applications ran sequentially; across chains, ready applications ran concurrently in staged batches. Structural projection passed only each forge report's `## The forged question` text into its corresponding parable, together with the shared anonymous craft brief.

The runner validated result envelopes and the accepted outline's leaf count, and checked each parable's length and absence of source labels. All 39 semantic applications ultimately succeeded, and the final run status is **Succeeded**. The program also proposed branch-local failure behavior and blocking rules, but those hypothetical leaf failures did not occur; only the outline's documented mechanical retry was exercised.

No external Bible text was retrieved, quoted, or read from a workspace source; the applications operated on the corpus reference named in the request. Fresh-worker prompts and narrow read/write contracts created behavioral shared-workspace boundaries, not an operating-system filesystem sandbox.

## Failures and blocked work

None.

Application 003's first malformed 13-leaf attempt was preserved and then succeeded on its single mechanical retry. This does not make the run Partial.

## Complete artifact index

### Run-level records

- [Natural-language request](request.md)
- [Compiler prompt](compiler-prompt.md)
- [Compiled Sem program](program.md)
- [Compile notes](compile-notes.md)
- [Runtime interpretation](interpretation.md)
- [Run log and application states](run.md)
- [Finalizer handoff prompt](finalizer-prompt.md)

### Application trace

- [Application 001 · deterministic draw · worker prompt](applications/001-deterministic-draw/prompt.md)
- [Application 001 · deterministic draw · result](applications/001-deterministic-draw/result.md)
- [Application 001 · deterministic draw · status](applications/001-deterministic-draw/status.md)
- [Application 002 · blend craft mechanisms · worker prompt](applications/002-blend-craft-mechanisms/prompt.md)
- [Application 002 · blend craft mechanisms · result](applications/002-blend-craft-mechanisms/result.md)
- [Application 002 · blend craft mechanisms · status](applications/002-blend-craft-mechanisms/status.md)
- [Application 003 · build major minor outline · rejected attempt 1](applications/003-build-major-minor-outline/attempts/001-failure.md)
- [Application 003 · build major minor outline · retry prompt 2](applications/003-build-major-minor-outline/attempts/002-prompt.md)
- [Application 003 · build major minor outline · worker prompt](applications/003-build-major-minor-outline/prompt.md)
- [Application 003 · build major minor outline · result](applications/003-build-major-minor-outline/result.md)
- [Application 003 · build major minor outline · status](applications/003-build-major-minor-outline/status.md)
- [Application 004 · leaf 1 1 heart · worker prompt](applications/004-leaf-1-1-heart/prompt.md)
- [Application 004 · leaf 1 1 heart · result](applications/004-leaf-1-1-heart/result.md)
- [Application 004 · leaf 1 1 heart · status](applications/004-leaf-1-1-heart/status.md)
- [Application 005 · leaf 1 1 forge · worker prompt](applications/005-leaf-1-1-forge/prompt.md)
- [Application 005 · leaf 1 1 forge · result](applications/005-leaf-1-1-forge/result.md)
- [Application 005 · leaf 1 1 forge · status](applications/005-leaf-1-1-forge/status.md)
- [Application 006 · leaf 1 1 parable · worker prompt](applications/006-leaf-1-1-parable/prompt.md)
- [Application 006 · leaf 1 1 parable · result](applications/006-leaf-1-1-parable/result.md)
- [Application 006 · leaf 1 1 parable · status](applications/006-leaf-1-1-parable/status.md)
- [Application 007 · leaf 1 2 heart · worker prompt](applications/007-leaf-1-2-heart/prompt.md)
- [Application 007 · leaf 1 2 heart · result](applications/007-leaf-1-2-heart/result.md)
- [Application 007 · leaf 1 2 heart · status](applications/007-leaf-1-2-heart/status.md)
- [Application 008 · leaf 1 2 forge · worker prompt](applications/008-leaf-1-2-forge/prompt.md)
- [Application 008 · leaf 1 2 forge · result](applications/008-leaf-1-2-forge/result.md)
- [Application 008 · leaf 1 2 forge · status](applications/008-leaf-1-2-forge/status.md)
- [Application 009 · leaf 1 2 parable · worker prompt](applications/009-leaf-1-2-parable/prompt.md)
- [Application 009 · leaf 1 2 parable · result](applications/009-leaf-1-2-parable/result.md)
- [Application 009 · leaf 1 2 parable · status](applications/009-leaf-1-2-parable/status.md)
- [Application 010 · leaf 1 3 heart · worker prompt](applications/010-leaf-1-3-heart/prompt.md)
- [Application 010 · leaf 1 3 heart · result](applications/010-leaf-1-3-heart/result.md)
- [Application 010 · leaf 1 3 heart · status](applications/010-leaf-1-3-heart/status.md)
- [Application 011 · leaf 1 3 forge · worker prompt](applications/011-leaf-1-3-forge/prompt.md)
- [Application 011 · leaf 1 3 forge · result](applications/011-leaf-1-3-forge/result.md)
- [Application 011 · leaf 1 3 forge · status](applications/011-leaf-1-3-forge/status.md)
- [Application 012 · leaf 1 3 parable · worker prompt](applications/012-leaf-1-3-parable/prompt.md)
- [Application 012 · leaf 1 3 parable · result](applications/012-leaf-1-3-parable/result.md)
- [Application 012 · leaf 1 3 parable · status](applications/012-leaf-1-3-parable/status.md)
- [Application 013 · leaf 2 1 heart · worker prompt](applications/013-leaf-2-1-heart/prompt.md)
- [Application 013 · leaf 2 1 heart · result](applications/013-leaf-2-1-heart/result.md)
- [Application 013 · leaf 2 1 heart · status](applications/013-leaf-2-1-heart/status.md)
- [Application 014 · leaf 2 1 forge · worker prompt](applications/014-leaf-2-1-forge/prompt.md)
- [Application 014 · leaf 2 1 forge · result](applications/014-leaf-2-1-forge/result.md)
- [Application 014 · leaf 2 1 forge · status](applications/014-leaf-2-1-forge/status.md)
- [Application 015 · leaf 2 1 parable · worker prompt](applications/015-leaf-2-1-parable/prompt.md)
- [Application 015 · leaf 2 1 parable · result](applications/015-leaf-2-1-parable/result.md)
- [Application 015 · leaf 2 1 parable · status](applications/015-leaf-2-1-parable/status.md)
- [Application 016 · leaf 2 2 heart · worker prompt](applications/016-leaf-2-2-heart/prompt.md)
- [Application 016 · leaf 2 2 heart · result](applications/016-leaf-2-2-heart/result.md)
- [Application 016 · leaf 2 2 heart · status](applications/016-leaf-2-2-heart/status.md)
- [Application 017 · leaf 2 2 forge · worker prompt](applications/017-leaf-2-2-forge/prompt.md)
- [Application 017 · leaf 2 2 forge · result](applications/017-leaf-2-2-forge/result.md)
- [Application 017 · leaf 2 2 forge · status](applications/017-leaf-2-2-forge/status.md)
- [Application 018 · leaf 2 2 parable · worker prompt](applications/018-leaf-2-2-parable/prompt.md)
- [Application 018 · leaf 2 2 parable · result](applications/018-leaf-2-2-parable/result.md)
- [Application 018 · leaf 2 2 parable · status](applications/018-leaf-2-2-parable/status.md)
- [Application 019 · leaf 2 3 heart · worker prompt](applications/019-leaf-2-3-heart/prompt.md)
- [Application 019 · leaf 2 3 heart · result](applications/019-leaf-2-3-heart/result.md)
- [Application 019 · leaf 2 3 heart · status](applications/019-leaf-2-3-heart/status.md)
- [Application 020 · leaf 2 3 forge · worker prompt](applications/020-leaf-2-3-forge/prompt.md)
- [Application 020 · leaf 2 3 forge · result](applications/020-leaf-2-3-forge/result.md)
- [Application 020 · leaf 2 3 forge · status](applications/020-leaf-2-3-forge/status.md)
- [Application 021 · leaf 2 3 parable · worker prompt](applications/021-leaf-2-3-parable/prompt.md)
- [Application 021 · leaf 2 3 parable · result](applications/021-leaf-2-3-parable/result.md)
- [Application 021 · leaf 2 3 parable · status](applications/021-leaf-2-3-parable/status.md)
- [Application 022 · leaf 2 4 heart · worker prompt](applications/022-leaf-2-4-heart/prompt.md)
- [Application 022 · leaf 2 4 heart · result](applications/022-leaf-2-4-heart/result.md)
- [Application 022 · leaf 2 4 heart · status](applications/022-leaf-2-4-heart/status.md)
- [Application 023 · leaf 2 4 forge · worker prompt](applications/023-leaf-2-4-forge/prompt.md)
- [Application 023 · leaf 2 4 forge · result](applications/023-leaf-2-4-forge/result.md)
- [Application 023 · leaf 2 4 forge · status](applications/023-leaf-2-4-forge/status.md)
- [Application 024 · leaf 2 4 parable · worker prompt](applications/024-leaf-2-4-parable/prompt.md)
- [Application 024 · leaf 2 4 parable · result](applications/024-leaf-2-4-parable/result.md)
- [Application 024 · leaf 2 4 parable · status](applications/024-leaf-2-4-parable/status.md)
- [Application 025 · leaf 3 1 heart · worker prompt](applications/025-leaf-3-1-heart/prompt.md)
- [Application 025 · leaf 3 1 heart · result](applications/025-leaf-3-1-heart/result.md)
- [Application 025 · leaf 3 1 heart · status](applications/025-leaf-3-1-heart/status.md)
- [Application 026 · leaf 3 1 forge · worker prompt](applications/026-leaf-3-1-forge/prompt.md)
- [Application 026 · leaf 3 1 forge · result](applications/026-leaf-3-1-forge/result.md)
- [Application 026 · leaf 3 1 forge · status](applications/026-leaf-3-1-forge/status.md)
- [Application 027 · leaf 3 1 parable · worker prompt](applications/027-leaf-3-1-parable/prompt.md)
- [Application 027 · leaf 3 1 parable · result](applications/027-leaf-3-1-parable/result.md)
- [Application 027 · leaf 3 1 parable · status](applications/027-leaf-3-1-parable/status.md)
- [Application 028 · leaf 3 2 heart · worker prompt](applications/028-leaf-3-2-heart/prompt.md)
- [Application 028 · leaf 3 2 heart · result](applications/028-leaf-3-2-heart/result.md)
- [Application 028 · leaf 3 2 heart · status](applications/028-leaf-3-2-heart/status.md)
- [Application 029 · leaf 3 2 forge · worker prompt](applications/029-leaf-3-2-forge/prompt.md)
- [Application 029 · leaf 3 2 forge · result](applications/029-leaf-3-2-forge/result.md)
- [Application 029 · leaf 3 2 forge · status](applications/029-leaf-3-2-forge/status.md)
- [Application 030 · leaf 3 2 parable · worker prompt](applications/030-leaf-3-2-parable/prompt.md)
- [Application 030 · leaf 3 2 parable · result](applications/030-leaf-3-2-parable/result.md)
- [Application 030 · leaf 3 2 parable · status](applications/030-leaf-3-2-parable/status.md)
- [Application 031 · leaf 4 1 heart · worker prompt](applications/031-leaf-4-1-heart/prompt.md)
- [Application 031 · leaf 4 1 heart · result](applications/031-leaf-4-1-heart/result.md)
- [Application 031 · leaf 4 1 heart · status](applications/031-leaf-4-1-heart/status.md)
- [Application 032 · leaf 4 1 forge · worker prompt](applications/032-leaf-4-1-forge/prompt.md)
- [Application 032 · leaf 4 1 forge · result](applications/032-leaf-4-1-forge/result.md)
- [Application 032 · leaf 4 1 forge · status](applications/032-leaf-4-1-forge/status.md)
- [Application 033 · leaf 4 1 parable · worker prompt](applications/033-leaf-4-1-parable/prompt.md)
- [Application 033 · leaf 4 1 parable · result](applications/033-leaf-4-1-parable/result.md)
- [Application 033 · leaf 4 1 parable · status](applications/033-leaf-4-1-parable/status.md)
- [Application 034 · leaf 4 2 heart · worker prompt](applications/034-leaf-4-2-heart/prompt.md)
- [Application 034 · leaf 4 2 heart · result](applications/034-leaf-4-2-heart/result.md)
- [Application 034 · leaf 4 2 heart · status](applications/034-leaf-4-2-heart/status.md)
- [Application 035 · leaf 4 2 forge · worker prompt](applications/035-leaf-4-2-forge/prompt.md)
- [Application 035 · leaf 4 2 forge · result](applications/035-leaf-4-2-forge/result.md)
- [Application 035 · leaf 4 2 forge · status](applications/035-leaf-4-2-forge/status.md)
- [Application 036 · leaf 4 2 parable · worker prompt](applications/036-leaf-4-2-parable/prompt.md)
- [Application 036 · leaf 4 2 parable · result](applications/036-leaf-4-2-parable/result.md)
- [Application 036 · leaf 4 2 parable · status](applications/036-leaf-4-2-parable/status.md)
- [Application 037 · leaf 4 3 heart · worker prompt](applications/037-leaf-4-3-heart/prompt.md)
- [Application 037 · leaf 4 3 heart · result](applications/037-leaf-4-3-heart/result.md)
- [Application 037 · leaf 4 3 heart · status](applications/037-leaf-4-3-heart/status.md)
- [Application 038 · leaf 4 3 forge · worker prompt](applications/038-leaf-4-3-forge/prompt.md)
- [Application 038 · leaf 4 3 forge · result](applications/038-leaf-4-3-forge/result.md)
- [Application 038 · leaf 4 3 forge · status](applications/038-leaf-4-3-forge/status.md)
- [Application 039 · leaf 4 3 parable · worker prompt](applications/039-leaf-4-3-parable/prompt.md)
- [Application 039 · leaf 4 3 parable · result](applications/039-leaf-4-3-parable/result.md)
- [Application 039 · leaf 4 3 parable · status](applications/039-leaf-4-3-parable/status.md)
