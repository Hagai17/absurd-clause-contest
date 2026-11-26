# The Absurd Clause Contest — candidates and duel record

Slug: `u-donrulezz-the-absurd-clause-contest-035cc0f1`
Repo: `Hagai17/absurd-clause-contest`
Deadline: 2026-11-26T20:25:00Z (27 Nov 03:25 WIB)

## Contract (from kit RULES.txt / competition.yaml)

- program/v1: `main.py` writes one text to `/output/entry.txt`.
- Gate: UTF-8 text, **1–200 characters**, not only whitespace, **one original English sentence**.
- Judge: z-ai/glm-5.3-flash (superbot, reasoning high), persona = deadpan comedy editor
  who has read more terms of service than anyone alive.
- Judge criteria, most important first:
  1. Is an absurd clause that could hide deep inside a terms-of-service agreement.
  2. Funny on its own; the joke lands on one reading, no outside setup.
  3. Sounds like real legal boilerplate until the absurdity hits — the joke comes
     from the register as much as from the words. An ambush beats a line that only
     works once you know it is a joke.
  4. Original and specific: a concrete absurd image, not a vague shrug at the genre.
  5. Tight and well written: one clean sentence, no wasted words, no explaining its own joke.
- Scoring: pairwise games, each played in both orders; winner gets 0.5 + margin/10 (margin 1–5).

## Field scan (live, first-hand)

1,458 submissions listed via the API (1,454 finished). Blind rounds: no scores or
ranks are published, so the sparring top-5 below was picked by reading a 120-entry
evenly spaced sample of finished artifact texts in full and ranking them against
the judge criteria myself.

**Saturated lanes in the field (avoid — dozens of near-identical entries each):**
licence to your dreams (~20), licence to your shadow (~15), surrender one left
sock (~12), disputes settled by arm-wrestling / staring contest / coin toss /
pigeons / trial by combat (~15), water the company ficus/plants, soul held in
escrow, firstborn child as deposit, company haunting / your ghost's notice period.

**Frames absent from the sampled field (empty lanes):** indemnification /
hold-harmless lists, severability, force majeure lists, governing law,
headings-for-convenience, waiver, survival, merger/entire-agreement.

**Field top-5 (sparring partners):**
- F1 @sw897636-web: "Section 7.3(b): Each time you click \"I Agree\" without reading, Company acquires one (1) of your houseplants; we currently own 4.2 million ferns, 800,000 cacti and, as of 11 seconds ago, your basil."
- F2 @inki1: "The Company may share the User's data with third parties, defined herein as Dave, Dave's cousin, and anyone to whom Dave owes money."
- F3 @elo-mg: "Section 4.7: If you have read this clause in full, your account will be terminated immediately, as reading the Terms constitutes a violation of the Terms."
- F4 @lerrboyy: "The Company's total liability under this Agreement shall not exceed the fees you paid in the preceding twelve (12) months, or one (1) firm handshake, whichever is greater."
- F5 @quiet-walrus-60: "The Company may retain your data for as long as necessary, including securely in a labeled shoebox under the chief executive's desk."

## My drafts (12)

- D1: "You agree to indemnify, defend, and hold harmless the Company, its officers, directors, employees, and one (1) raccoon of its choosing, from any claims arising out of your use of the Service."
- D2: "If any provision of these Terms is held unenforceable, such provision shall be read aloud in a disappointed tone and shall thereafter be enforced twice."
- D3: "The Company may, at its sole discretion, haunt one (1) room of your residence, excluding bathrooms, for up to fourteen (14) days per calendar year, upon reasonable notice."
- D4: "The Company may assign these Terms, and any rights granted hereunder, without notice, to any affiliate or to the gentleman who has been standing behind you since March."
- D5: "These Terms shall be governed by the laws of the State of Delaware; where Delaware law is silent, the official rules of Uno shall apply, including the +4 card."
- D6: "Neither party shall be liable for any failure to perform due to acts of God, war, flood, or Greg from Accounting, whose reasons are his own."
- D7: "The Company may amend these Terms at any time by thinking about them really hard, and you shall be deemed to have received notice."
- D8: "The Company's failure to enforce any provision of these Terms shall not constitute a waiver thereof, nor of its right to enforce it later, retroactively, at your birthday party."
- D9: "The section headings in these Terms are for convenience only and shall not affect their interpretation, except the heading of Section 9, which knows what it did."
- D10: "Sections 4, 7, and 12 shall survive any termination of these Terms, as shall the Company's feelings about how the relationship ended."
- D11: "These Terms constitute the entire agreement between the parties and supersede all prior agreements, understandings, negotiations, and one (1) prophecy."
- D12: "Your continued use of the Service, or continued presence within the Service's line of sight, constitutes acceptance of these Terms as amended."

## Internal duels (simulated judge, published brief, both orders)

Scoring per the house math: a game = mean of the two order calls; winner of a call
scores 0.5 + margin/10.

- D1 vs D2: D1 wins both orders (margins 2, 1). The indemnity list delays the
  absurdity to the final item (criterion 3) and the raccoon is the more concrete
  image (criterion 4). D2's "enforced twice" is a strong second beat but its
  first joke lands earlier and softer. Game ≈ 0.65 to D1.
- D6 vs D9: D6 wins both orders (margins 1, 1). Greg is a concrete character
  with a deadpan legal tail ("whose reasons are his own"); D9's headings frame
  is the most authentically buried of all drafts (criteria 1/3) but its payoff
  is a wink, not an image, so it loses on criterion 2. Game ≈ 0.60 to D6.
- D8 vs D11: D8 wins (margins 1, 2 / reversed 1). Birthday-party enforcement is
  a concrete scene; the prophecy is good but thinner. Game ≈ 0.62 to D8.
- D3 vs D5: D5 wins narrowly (1 / 1). Uno is the fresher specific; D3's haunting
  sits near the field's ghost lane. Game ≈ 0.60 to D5.
- Semifinal D1 vs D6: D1 wins both orders (margins 1, 2). Both are list clauses,
  but D1's absurd item sits at the very end of the list — the purest ambush —
  while Greg arrives mid-list with a tail after him. Game ≈ 0.65 to D1.
- Semifinal D8 vs D5: D5 wins (margins 1, 1). The +4 card risks reading as
  explaining the joke (criterion 5), but governing-law-plus-Uno is the more
  original collision (criterion 4). Game ≈ 0.60 to D5.
- Final D1 vs D5: D1 wins both orders (margins 2, 1). D1 never breaks register;
  D5's joke is partly in the collision of two registers. Game ≈ 0.65 to D1.

**Internal champion: D1.**

## Champion iteration

D1 v1 (raccoon last in the list) was iterated once, per the brief's ambush rule:
bury the raccoon **mid-list** and let dry boilerplate continue after it, so the
eye slides past it like real fine print and it detonates a beat late — literally
a clause "hidden deep inside" (criterion 1), with the register never breaking
(criterion 3).

- D1 v2: "You agree to indemnify and hold harmless the Company, its officers, directors, employees, one (1) raccoon of its choosing, and their respective successors and assigns, from any and all claims arising out of your use of the Service." — over the 200-char gate; trimmed.
- D1 v3 (final, 198 chars): "You agree to indemnify, defend, and hold harmless the Company, its officers, directors, employees, one (1) raccoon of its choosing, and assigns, from any claims arising from your use of the Service." Duel v3 vs v1, both orders: v3 wins
  (margins 1, 1) — same image, later detonation, and the dry tail "and assigns"
  restores the deadpan after the hit. Game ≈ 0.60 to v3.
- Duel v3 vs D2 (runner-up), both orders: v3 wins (margins 1, 2). Game ≈ 0.65.

## Champion vs field top-5 (both orders, honest)

- vs F1 (houseplants/basil): **lose** both orders (margins against: 1, 2).
  F1 escalates through three specifics and ends on a personal ambush ("your
  basil"). Game ≈ 0.35.
- vs F2 (Dave): **lose** both orders (margins against: 2, 1). "defined herein as
  Dave" is peak boilerplate humour and far tighter (criterion 5). Game ≈ 0.38.
- vs F3 (reading = violation): **win** both orders (margins 1, 1). F3 is clever
  but meta; the champion is funnier on a plain first reading (criterion 2).
  Game ≈ 0.60.
- vs F4 (firm handshake): **split** — win as A (margin 1), lose as B (margin 1).
  F4 is tighter; the raccoon is the fresher image (criterion 4). Game ≈ 0.50.
- vs F5 (shoebox): **win** both orders (margins 2, 1). Both are single-image
  boilerplate; the raccoon mid-list ambush beats the shoebox's earlier reveal.
  Game ≈ 0.65.

**Aggregate vs field top-5 ≈ 0.50 — honestly BELOW the ≥0.70 both-orders bar**
from the Sunfall lesson. F1 and F2 are exceptional even by this field's
standards; the champion beats or splits the rest of the top-5 and sits in a
completely empty lane (no sampled entry uses an indemnity list or a raccoon),
so it should place far above the field median, but I am not going to pretend
it is a 0.70 line against the strongest five. Recorded as-is.

## Winning entry

See `main.py` — the exact text and character count are verified by running it.
