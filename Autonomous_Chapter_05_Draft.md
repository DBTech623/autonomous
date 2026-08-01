# Chapter 5

## Systems Integration

The first turnstile accepted Malcolm's temporary badge. The second one flashed red.

He tried it again, slower this time, as though the reader might respect care.

`ACCESS NOT FOUND`

"The badge is valid," the security officer said.

"The door disagrees."

"Building access is valid. Compartment access requires an escort."

On the other side of the glass, Cate Mercer waited with one hand resting over the other. She had watched both attempts without stepping closer.

Malcolm looked down at the badge. The photograph was four years old. His hair was shorter, his face fuller, and nothing had happened in Moldova yet. A yellow stripe beneath the picture read `TEMPORARY ACCESS` in letters large enough to save everyone the trouble of asking.

Cate placed her badge against the reader. The barrier unlocked for both of them.

"Good to see you, Malcolm."

She did not say welcome back.

Cate had recruited him into Aurora when it was still a collection of proposals nobody could explain without a whiteboard. Later, she had stood in a conference room with no windows and told him his reassignment was the only outcome available. She had made both conversations sound like opportunities.

"Director Mercer."

"Cate is fine."

It had been fine before Moldova too.

They followed a corridor whose walls displayed framed photographs of officials signing agreements Malcolm had helped turn into software. No engineers appeared in the pictures.

"Does this review concern the exercise?" he asked.

"It concerns consistency across several hybrid responses."

"The NATO intervention."

"Among others."

"Was it authorized?"

"You're here to help us determine whether the systems behaved within their authorities."

"That isn't what I asked."

Cate stopped at a door with no room number. "The audit is not an investigation of a covert actor. It is not a damage assessment. It is not a referendum on the judgment of allied commands. Gabriel Torres is conducting a hybrid-response consistency audit."

"That phrase needed a committee."

"Two, actually."

He almost smiled. Cate's expression said she had noticed and would allow it.

"What access do I have?"

"Material Torres determines is necessary for the review."

"Aurora?"

The word sat between them. Cate's face did not change.

"This review has no Aurora equities."

"You brought in the person who built it."

"We requested an analyst with constraint-modeling experience."

"Who owns the finding?"

"Torres owns the process."

"That wasn't the question either."

"Then you already know the answer."

Cate opened the door.

Three people looked up from a table crowded with government laptops, paper binders, and insulated coffee cups. A wall display showed three vertical columns. Paper labels had been stuck beneath them: `BALTIC`, `MARKET`, and `EXERCISE`. Each label was written in a different hand.

"Your consultant is here," Cate said.

Malcolm went in. She let the door close behind him.

* * *

His combined timeline was gone before he sat down.

"Where's the overlay?" Malcolm asked.

The woman nearest the display kept working. Dr. Leila Haddad, according to the nameplate. CISA. She had divided his timeline into three separate windows and moved them to opposite sides of the wall.

"In quarantine," she said.

"It isn't malware."

"Malware usually comes with more reliable timestamps."

Gabriel Torres rose and offered Malcolm a hand. He was broad through the shoulders, with the patient posture of someone accustomed to waiting beside cargo that had missed a connection.

"Gabriel Torres. Mission assurance."

"Malcolm Carter."

"I know."

The third person lifted two fingers from his keyboard in greeting. "Miles Chen. Treasury."

Torres pointed to the only open chair. No one asked Malcolm to introduce his theory. That was good. A room that already knew what he thought might also know where it was weak.

He sat. "Why quarantine it?"

Leila turned from the wall. "Because your zero points are administrative events, not shared clock events. The Baltic carrier records are marked at receipt. The exchange records show enforcement. The exercise log mixes local device time with command reporting time. Putting them on one line gives you a sequence the source material hasn't earned."

"The order survives ordinary drift."

"Maybe. You haven't shown that."

She reopened the Baltic window. Six timestamps appeared, each with a colored confidence band around it.

"This handoff passed through two carriers. One logs when it accepts the route. The other logs when the route enters its cache. If either exported a batch late, your first correction moves."

"Not far enough."

"You hope."

Malcolm felt the old answer rising, the one that began with an explanation of how many systems he had built and ended with everyone else resenting him. He swallowed it.

"How far?" he asked.

Leila studied him for a moment, then widened one of the bands by ninety seconds.

"Defensibly? That far. I can make it uglier if an allied carrier decides its internal clock is a state secret."

"It usually does," Torres said.

Miles rotated his laptop so Malcolm could see a page of exchange rules.

"The market event has the opposite problem. You treated the public circuit breaker as the decision point. It wasn't. Two liquidity providers had private risk controls that could have reduced exposure before the exchange-wide halt."

"Could have?"

"Their rules permit it. We don't have the internal order trail yet."

"Then it doesn't disprove the sequence."

"It does weaken your choice of zero."

Leila tapped the display. "Different systems. Different owners. Different definitions of action."

"Same direction," Malcolm said.

"Direction is an interpretation."

"A convoy changes route. Communications capacity moves away from public traffic and toward command traffic. A market sheds exposure tied to the ports. Each system gives up local efficiency before the exercise command recognizes the intrusion. Call that what you want."

"I call it three things we haven't normalized," Leila said.

Torres had not opened his laptop. He was moving paper labels beneath the display. `COMMAND RECOGNITION` became `RECORDED COMMAND RECOGNITION`.

"Assume they're right," he said.

Malcolm looked at him.

"Dr. Haddad gets all the clock drift she can support. Chen gets private controls operating at the earliest time their rules permit. What remains?"

The question cut across the argument Malcolm had prepared. It also gave him somewhere useful to go.

He stood and moved the Baltic window back toward the center, stopping when Leila raised a finger.

"I'm not combining them."

"Good."

He drew three lines on the blank space between the windows.

"In the Baltic, the least disputable action is the carrier route change. In the market, it is the first confirmed withdrawal by a liquidity provider. In the exercise, it is the convoy instruction."

"Those aren't equivalent actions," Miles said.

"No. They're sacrifices."

Miles leaned back.

"The carrier accepts congestion. The liquidity provider gives up a favorable position. The convoy abandons the fastest route. Different authorities, different costs, same result: propagation slows."

"Propagation of what?" Leila asked.

"Instability."

"That's broad enough to explain rain."

"Then call it cascading loss. Each system pays a local cost to reduce a larger one."

Leila folded her arms. "Plenty of resilience systems are designed to do that."

"Independently?"

"Yes."

"Before the shared threat is visible to the people responsible for all three?"

No one answered at once.

Malcolm could feel the room doing what he had missed more than the clearance, more than the sealed feeds and the careful language. Four people were looking at one problem from places that did not fit together. For a few seconds his mind stopped replaying old arguments and went to work.

He hated how much relief came with it.

Torres moved another label. Under the three lines, he placed a blank strip of paper.

"Give me the narrow claim."

Malcolm uncapped a marker.

"Separate systems changed toward a common objective before any shared human authority acted."

"Recorded action," Leila said.

He added the word.

"And objective is inferred," Miles said.

Malcolm wrote that too.

The sentence now carried so many qualifications it needed structural support.

Torres read it once. "Can everybody live with that as an unconfirmed working hypothesis?"

"I can try to kill it," Leila said.

"That's not what I asked."

"Then yes."

Miles nodded. "Pending the private order trails."

Torres looked at Malcolm.

"It isn't mine anymore," Malcolm said.

"It never was."

Torres restored the combined timeline to the display. A gray banner appeared across its top: `UNNORMALIZED — WORKING USE ONLY`.

Leila went back to the contract inventory. The pages listed providers behind each system, then providers behind those providers. Defense integrators, cloud hosts, risk platforms, telecom subcontractors. The same functions appeared under different names depending on which agency had purchased them.

"That's irritating," she said.

"What is?" Miles asked.

She marked a company beneath the Baltic carrier record. Then another beneath the exchange vendor. A third sat two layers below the exercise logistics platform.

The name was the same each time.

StratCore.

* * *

By late afternoon, the dependency map had acquired four agency colors and the appearance of a subway system designed by people who disliked passengers.

StratCore was the only label covered by all four.

Malcolm stood at the end of the table reading the request Torres had drafted.

`VENDOR CLARIFICATION`

"That assumes there's something to clarify."

Torres continued typing. "There is."

"It assumes an innocent explanation."

"Do you have evidence of a guilty one?"

"I have three systems moving toward one objective through the same contractor."

Miles shook his head. "Through products StratCore sells, supports, or acquired. Those aren't the same relationship."

He pulled up the contract inventory. StratCore provided network-continuity software to the Baltic carrier's parent company. Its risk engine had been incorporated into the exchange platform through an acquisition two years earlier. A logistics subsidiary maintained the exercise's convoy-optimization service.

Each connection had a contract number, a statement of work, and a legal reason to exist.

"They're everywhere because governments buy from the same short list of companies," Miles said. "If we mapped payroll software, we'd probably uncover a mastermind too."

"Payroll rarely reroutes a convoy."

"Give it time."

Leila set a binder on top of the map. "I want the raw route provenance, the authorization events around the carrier handoff, and the product boundary for the exercise platform."

"Vale will give you a demonstration," Malcolm said.

"Then I'll ask where the demonstration data came from."

"They'll give you curated logs."

"Which is more than we have now."

Torres finished the request and turned his screen toward them. The recipient line named Vale Dynamics Government Systems. StratCore appeared in the subject.

"We can request records under the existing consistency review," he said. "We cannot treat a major allied contractor as a hostile service because its name appears on a procurement map."

"Four times," Malcolm said.

"Four legitimate times."

The door opened behind them. Cate entered without an aide, read the map, and then read Torres's request.

"Standard vendor engagement?" she asked.

"Technical clarification and product demonstration."

"Scope?"

"The three response chains. Contract ownership, authorization boundaries, event provenance."

Her gaze moved to Malcolm. "No architecture fishing."

"If the architecture is the connection, it isn't fishing."

"Then the authorized material will establish that."

He knew the shape of the exchange. Cate had given him access to a room where the question could be asked, then built the walls close enough to control which answers counted. The boundaries were reasonable. That made them harder to fight.

Torres said, "Haddad leads the technical questions. Carter supports."

Malcolm looked at him. "I found the dependency."

"You found a name repeated on a wall."

"After I got the comparison restored."

"As an unconfirmed hypothesis."

Leila closed her binder. "If he's coming, I want him in the room when I ask about the shared objective."

"There is no shared objective in the request," Torres said.

"That's why I want him there."

Cate considered it. "Approved. Dr. Haddad and Mr. Carter as technical members. You lead."

Torres nodded.

Malcolm looked again at his old photograph hanging from the badge clipped to his belt. For most of the day, he had managed to forget the yellow stripe beneath it.

"Change the subject line," he said.

"To what?"

"Cross-domain systems integration review."

"That presumes integration."

"Vendor clarification presumes there isn't any."

Torres clicked `SEND`.

"Now Vale can clarify."
