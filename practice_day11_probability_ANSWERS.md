# FIT1058 — Day 11 ANSWER KEY · Discrete Probability (Ch 9–10)

> Don't open until you've attempted `practice_day11_probability.md`.

**W1.** ¬(p ∨ ¬q) ∨ (¬p ∧ ¬q)
= (¬p ∧ q) ∨ (¬p ∧ ¬q)  [De Morgan + double negation on first bracket]
= ¬p ∧ (q ∨ ¬q)  [distributive, factoring out ¬p]
= ¬p ∧ T  [complement/negation law: q ∨ ¬q = T]
= **¬p**  [identity law]

**Q1. (c) 1/6.** Sum = 7 has 6 ordered outcomes {(1,6),(2,5),(3,4),(4,3),(5,2),(6,1)} out of 36, = 6/36 = 1/6. (Note (b) 5/36 is the count for sum = 6 or 8 — a classic trap.)

**Q2. (b) 0.7.** Inclusion–exclusion: Pr(A∪B) = 0.5 + 0.4 − 0.2 = 0.7.

**Q3. (c) ≈ 0.09.** Bayes: Pr(D|+) = (0.95·0.01) / (0.95·0.01 + 0.10·0.99) = 0.0095 / 0.1085 = **0.0876**. The base rate is so low that most positives are false positives — this is the key Bayes intuition.

**Q4. (b) 5.** Geometric distribution (trials up to & including first success): E(X) = 1/p = 1/0.2 = 5.

**Q5. (a) e⁻³ ≈ 0.050.** Poisson Pr(X=0) = e^(−λ)·λ⁰/0! = e⁻³ ≈ 0.0498.

**Q6. (a), (c), (e).**
- (a) ✓ definition of independence.
- (b) ✗ general addition rule is Pr(A)+Pr(B)−Pr(A∩B); only holds without the last term if mutually exclusive, not if independent.
- (c) ✓ and (e) ✓ are equivalent restatements of independence (conditioning doesn't change the probability).
- (d) ✗ independence ≠ mutual exclusivity — in fact for events of positive probability they're incompatible (see error log Day note: mutually exclusive means Pr(A∩B)=0, independence means Pr(A∩B)=Pr(A)Pr(B)>0).

**Q7. (a), (b), (d).**
- (a) ✓ linearity of expectation holds even for dependent variables.
- (b) ✓ special case of linearity with a constant.
- (c) ✗ E(XY)=E(X)E(Y) requires **independence**, not true in general.
- (d) ✓ expectation of a constant is itself.
- (e) ✗ E(X) need not be an attainable value (e.g. E = 3.5 for a die).

**Q8.**
(a) X ~ Binomial(n = 8, p = 0.25).
(b) Pr(X=k) = C(8,k)·(0.25)^k·(0.75)^(8−k). Pr(X=2) = C(8,2)·0.25²·0.75⁶ = 28·0.0625·0.177979 = **0.311 (3 d.p.)**.
(c) Pr(X≥1) = 1 − Pr(X=0) = 1 − 0.75⁸ = 1 − 0.100113 = **0.900 (3 d.p.)**.
(d) E(X) = np = 8·0.25 = **2**. Var(X) = np(1−p) = 8·0.25·0.75 = **1.5**.

**Q9.**
(a) S = X₁ + X₂ + … + X₁₀.
(b) E(Xᵢ) = (1+2+3+4+5+6)/6 = 21/6 = **3.5**.
(c) By linearity of expectation, E(S) = E(X₁+…+X₁₀) = E(X₁)+…+E(X₁₀) = 10 × 3.5 = **35**.
Justification: linearity says E(∑Xᵢ) = ∑E(Xᵢ) **always** — it does **not** require the Xᵢ to be independent. (Independence would only be needed for a product/variance argument like Var(S)=∑Var(Xᵢ), not for the sum of expectations.) ∎

---
*Common slips to watch (tie-ins to your error log): (1) confusing mutually exclusive with independent — Q6d; (2) Bayes base-rate neglect — Q3; (3) assuming E(XY)=E(X)E(Y) without independence — Q7c.*
