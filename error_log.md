# FIT1058 Error Log

## Day 2 — Wed 3 Jun · Functions & Relations (Ch 2)

- **Q3 (equivalence relations):** chose (c), correct is (b). Mistake: (c) = {(1,1),(2,2),(3,3),(1,2),(2,3),(1,3)} is reflexive + transitive but **not symmetric** (has (1,2) but not (2,1)) — that's a partial order, not an equivalence relation. **Fix:** check symmetry first — every (a,b) needs its mirror (b,a). An equivalence relation must be reflexive AND symmetric AND transitive.

## Day 3 — Thu 4 Jun · Proofs I: Techniques (Ch 3)

- **Q2 (contradiction setup for √2):** chose (d), correct is (b). The "in lowest terms / not both even" assumption is the whole engine of the proof — that's what produces the contradiction (both a and b turn out even). It is never "irrelevant." **Fix:** to prove √2 irrational, assume √2 = a/b in lowest terms, then derive that 2 | a and 2 | b — contradicting lowest terms.
- **Q4 (contrapositive):** chose (c), correct is (a). Contrapositive of P⇒Q is ¬Q⇒¬P (negate BOTH and swap). Here P = "x+y irrational", Q = "x irr. or y irr." So ¬Q = "x rational AND y rational" (De Morgan turns OR into AND), ¬P = "x+y rational". Contrapositive = "if x and y both rational then x+y rational" = (a). Option (c) is the converse, not the contrapositive. **Fix:** contrapositive negates and flips; converse just flips. Don't confuse them.
- **Q5 (disproving a universal):** chose (a,b,c,e), correct is (a,b,e). (c) "prove the contrapositive of P(n)" *proves* P, it doesn't disprove the universal — so it's not a disproof method. **Fix:** to disprove ∀n P(n) you need ¬∀n P(n) = ∃n ¬P(n): one counterexample (a), many counterexamples (b), or a contradiction from assuming the universal (e).
- **Q6 (proof by cases):** chose (a,d), missed (b). Cases must be *exhaustive* but may *overlap* — overlap is allowed, mutual exclusivity is not required. **Fix:** the only hard rule is "cover every possibility"; overlapping cases are fine.
- **Q7 (contrapositive proof, 3n+2):** several issues — see notes. (1) Misstated the claim (it's "3n+2 odd ⇒ n odd", not even⇒even). (2) Wrong quantifier — it's "for all n", not "there exists". (3) Notation abuse: "2|n" means "2 divides n", it is NOT a number you can substitute; an even number is written n = 2k. (4) Algebra like "6|n+2 = 8|(n+1)" is invalid. (5) Labelled it contradiction but the task was contrapositive. **Fix / model:** Contrapositive of "3n+2 odd ⇒ n odd" is "n even ⇒ 3n+2 even." Assume n = 2k. Then 3n+2 = 6k+2 = 2(3k+1), which is even. Done.
