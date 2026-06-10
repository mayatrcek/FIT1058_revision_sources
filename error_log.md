# FIT1058 Error Log

## Day 2 — Wed 3 Jun · Functions & Relations (Ch 2)

- **Q3 (equivalence relations):** chose (c), correct is (b). Mistake: (c) = {(1,1),(2,2),(3,3),(1,2),(2,3),(1,3)} is reflexive + transitive but **not symmetric** (has (1,2) but not (2,1)) — that's a partial order, not an equivalence relation. **Fix:** check symmetry first — every (a,b) needs its mirror (b,a). An equivalence relation must be reflexive AND symmetric AND transitive.

## Day 3 — Thu 4 Jun · Proofs I: Techniques (Ch 3)

- **Q2 (contradiction setup for √2):** chose (d), correct is (b). The "in lowest terms / not both even" assumption is the whole engine of the proof — that's what produces the contradiction (both a and b turn out even). It is never "irrelevant." **Fix:** to prove √2 irrational, assume √2 = a/b in lowest terms, then derive that 2 | a and 2 | b — contradicting lowest terms.
- **Q4 (contrapositive):** chose (c), correct is (a). Contrapositive of P⇒Q is ¬Q⇒¬P (negate BOTH and swap). Here P = "x+y irrational", Q = "x irr. or y irr." So ¬Q = "x rational AND y rational" (De Morgan turns OR into AND), ¬P = "x+y rational". Contrapositive = "if x and y both rational then x+y rational" = (a). Option (c) is the converse, not the contrapositive. **Fix:** contrapositive negates and flips; converse just flips. Don't confuse them.
- **Q5 (disproving a universal):** chose (a,b,c,e), correct is (a,b,e). (c) "prove the contrapositive of P(n)" *proves* P, it doesn't disprove the universal — so it's not a disproof method. **Fix:** to disprove ∀n P(n) you need ¬∀n P(n) = ∃n ¬P(n): one counterexample (a), many counterexamples (b), or a contradiction from assuming the universal (e).
- **Q6 (proof by cases):** chose (a,d), missed (b). Cases must be *exhaustive* but may *overlap* — overlap is allowed, mutual exclusivity is not required. **Fix:** the only hard rule is "cover every possibility"; overlapping cases are fine.
- **Q7 (contrapositive proof, 3n+2):** several issues — see notes. (1) Misstated the claim (it's "3n+2 odd ⇒ n odd", not even⇒even). (2) Wrong quantifier — it's "for all n", not "there exists". (3) Notation abuse: "2|n" means "2 divides n", it is NOT a number you can substitute; an even number is written n = 2k. (4) Algebra like "6|n+2 = 8|(n+1)" is invalid. (5) Labelled it contradiction but the task was contrapositive. **Fix / model:** Contrapositive of "3n+2 odd ⇒ n odd" is "n even ⇒ 3n+2 even." Assume n = 2k. Then 3n+2 = 6k+2 = 2(3k+1), which is even. Done.

## Day 5 — Sat 6 Jun · Sequences & Series (Ch 6)

- **Q4 (Big-O of a series):** chose (a) Θ(n), correct is (c) Θ(n²). Mistake: read "+3 each term" as linear. But the series 3+6+…+3n is a *sum* of n terms, = 3·n(n+1)/2, which is quadratic. **Fix:** summing a linear (arithmetic) sequence gives a **quadratic** total. A sum of n terms whose average size is ~n is Θ(n²), not Θ(n).
- **Q3 (geometric sum closed form):** chose (b) 2ⁿ⁺¹−1, correct is (c) 2ⁿ⁺¹−2. Mistake: the standard identity 2⁰+2¹+…+2ⁿ = 2ⁿ⁺¹−1 starts at 2⁰, but Q3's sum starts at **2¹**. Dropping the 2⁰=1 term shifts the constant: (2ⁿ⁺¹−1)−1 = 2ⁿ⁺¹−2. **Fix:** always check **where a geometric sum starts**. Sanity check with small n (n=1: 2¹=2, and 2²−2=2 ✓).
- **Q8 (induction, ∑ i·2ⁱ) — step slip:** when splitting off the last term, the (k+1)th term is **(k+1)·2ᵏ⁺¹** (the full i·2ⁱ pattern at i=k+1), not just "(k+1)". **Fix / method:** (1) split off (k+1)·2ᵏ⁺¹; (2) apply IH; (3) factor out the common 2ᵏ⁺¹: [(k−1)+(k+1)]·2ᵏ⁺¹+2 = 2k·2ᵏ⁺¹+2 = k·2ᵏ⁺²+2. Also: write the **target** (set n=k+1 in the formula) before manipulating, and in the base case **show both sides equal** — don't just write "holds."

### Wins today (no error, keep doing)
- Q6 recurrence → closed form: correct (3n−1) via y=mx+c intuition (m = common difference d).
- Q7: derived the general sum formula 5n(n+1)/2, not just the number — strong.
