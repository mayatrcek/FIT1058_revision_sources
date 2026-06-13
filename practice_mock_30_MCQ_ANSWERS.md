# FIT1058 — 30-Question Mock · ANSWER KEY + brief explanations

> Attempt the set first! Each note gives the method, not just the letter.

**Sets**
- **Q1 — b.** A ∩ B = {3, 5, 7}. C contains 5, so (A ∩ B) \ C = {3, 7}. (a = {3,5,7}; c = A\B = {1,9}; d = {5}.)
- **Q2 — d.** |A ∪ B| = |A| + |B| only when A and B are disjoint; in general |A ∪ B| = |A| + |B| − |A ∩ B| (inclusion–exclusion). (a), (b), (c) are always true.
- **Q3 — b.** A △ B = (A \ B) ∪ (B \ A) = (A ∩ B‾) ∪ (A‾ ∩ B). Option (d) is the *complement* of A △ B; (a) and (c) are unrelated.

**Functions & Relations**
- **Q4 — b.** If g ∘ f is injective then f must be injective (but g need not be). (a) needs g surjective; (c) and (d) don't follow.
- **Q5 — b.** {(1,1),(2,2),(3,3),(1,2),(2,1)} is reflexive, symmetric and transitive. (a) isn't symmetric — missing (2,1) etc. (the partial-order trap from your error log); (c) isn't reflexive (no (3,3)); (d) isn't symmetric (has (1,3), no (3,1)).
- **Q6 — b.** Injective count = falling factorial 5 · 4 · 3 = 60. (a) = total functions; (d) = combinations.

**Proofs & Induction**
- **Q7 — b.** Contrapositive of "n² even ⇒ n even" is "n odd ⇒ n² odd." Assume n odd, show n² odd. (a) describes contradiction, not contrapositive.
- **Q8 — a.** Assume √2 = a/b in lowest terms; derive 2 | a then 2 | b, contradicting "lowest terms." The lowest-terms assumption is the engine of the proof (your Day 3 error-log point).
- **Q9 — a.** Set n = k + 1 in the formula: (k+1)(k+2)/2. (Always write the target before manipulating.)

**Sequences & Series**
- **Q10 — a.** a₁=3, a₂=7, a₃=15, a₄=31 = 2^(n+1) − 1. Check n=1: 2² − 1 = 3 ✓.
- **Q11 — b.** Sum starts at 2¹, so 2¹+…+2ⁿ = (2^(n+1) − 1) − 1 = **2^(n+1) − 2**. Sanity: n=1 gives 2, and 2² − 2 = 2 ✓. (The "where does it start" trap.)

**Number Theory**
- **Q12 — c.** 252 = 1·198 + 54; 198 = 3·54 + 36; 54 = 1·36 + 18; 36 = 2·18 + 0 → gcd = **18**.
- **Q13 — b.** φ(120) = 120 · (1−1/2)(1−1/3)(1−1/5) = 120 · 1/2 · 2/3 · 4/5 = **32**.
- **Q14 — c.** 14 = 2·7 is of the form 2p with p = 7 an odd prime, so it has primitive roots. (d) is true arithmetic but not the reason; even-ness alone (a) doesn't forbid primitive roots — 2 and 4 have them.
- **Q15 — c.** 3·5 = 15 ≡ 1 (mod 7), so 3⁻¹ ≡ **5**.

**Counting & Combinatorics**
- **Q16 — d.** BANANA = 6 letters with 3 A's, 2 N's, 1 B: 6!/(3!·2!·1!) = 720/12 = **60**.
- **Q17 — b.** C(10,3) = 120. (Order doesn't matter → combination.)
- **Q18 — b.** No repeats → 26·25·24·23·22. (a) allows repeats; (c) doesn't count orderings.
- **Q19 — b.** 12 months are the pigeonholes; 12 people could each take a different month, so you need **13** to force a repeat.

**Logic**
- **Q20 — a.** P ⇒ Q ≡ ¬P ∨ Q (material implication).
- **Q21 — b.** ¬∀x(P⇒Q) ≡ ∃x¬(P⇒Q) ≡ ∃x(P ∧ ¬Q). (Negating an implication gives AND, not OR — De Morgan.)
- **Q22 — c.** Contrapositive negates both parts and swaps: "If the ground is not wet, then it did not rain." (a) = converse, (b) = inverse, (d) = negation.

**Probability**
- **Q23 — b.** Condition on {4,5,6}; evens there are {4,6}: 2/3.
- **Q24 — c.** P(at least one head) = 1 − P(no heads) = 1 − 1/4 = **3/4**.
- **Q25 — c.** P = (0.9·0.01)/(0.9·0.01 + 0.05·0.99) = 0.009/0.0585 ≈ 0.154 ≈ **15%** — base-rate effect again (cf. your fraud question). Weight every branch by its conditional rate.

**Graph Theory**
- **Q26 — c.** Sum of degrees = 12 = 2·edges → **6** edges (Handshake Lemma).
- **Q27 — c.** 8 − 12 + F = 2 → F = **6**.
- **Q28 — a.** A tree on n vertices always has n − 1 edges. (b) needs all even degrees; (c) K₅ is non-planar; (d) bipartite graphs have NO odd cycles.
- **Q29 — a.** Closed Euler tour ⇔ connected and every vertex even degree. Exactly two odd → Euler *path*, not closed tour.

**Mixed**
- **Q30 — b.** |P(S)| = 2ⁿ = 2⁴ = **16**.

---
### Quick score guide
- **27–30:** exam-ready — do a light review of any slip.
- **22–26:** solid; drill the specific topics you missed.
- **< 22:** prioritise those chapters tomorrow in the mock, and re-read `error_log.md`.

*Log every miss into `error_log.md` with the correct method — that file is your highest-value last-day revision.*
