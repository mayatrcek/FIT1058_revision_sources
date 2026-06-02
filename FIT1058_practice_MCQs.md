# FIT1058 — 20 Multiple-Choice Practice Questions

Based on the course notes (Chapters 1–12) and Practice Exam 1. Choose one answer (a–d) per question. Answer key is at the bottom — try them all first.

---

**Q1 (Sets).** A set has 5 elements. How many of its subsets contain one particular fixed element?
a) 5   b) 16   c) 24   d) 32

**Q2 (Sets).** Given |A|=12, |B|=10, |C|=8, |A∩B|=5, |A∩C|=4, |B∩C|=3, |A∩B∩C|=2, what is |A∪B∪C|?
a) 18   b) 20   c) 22   d) 24

**Q3 (Sets).** For finite sets A and B, which statement is **not** always true?
a) |A∪B| = |A| + |B| − |A∩B|
b) |A∪B| = |A| + |B|
c) A∩B ⊆ A
d) |A△B| = |A∪B| − |A∩B|

**Q4 (Functions).** How many injective (one-to-one) functions are there from a 3-element set to a 5-element set?
a) 15   b) 60   c) 125   d) 243

**Q5 (Functions).** Let f: A→B and g: B→C. Which statement is **always** true?
a) If g∘f is surjective, then f is surjective
b) If g∘f is injective, then f is injective
c) If g∘f is injective, then g is injective
d) f∘g = g∘f

**Q6 (Relations).** On A = {1,2,3,4,5,6}, define aRb iff a ≡ b (mod 3). Which best describes R?
a) Reflexive only
b) Symmetric but not transitive
c) An equivalence relation
d) Neither reflexive, symmetric, nor transitive

**Q7 (Proofs).** What is the cleanest technique to prove "if n² is even, then n is even"?
a) Direct proof
b) Contrapositive (or contradiction)
c) Induction
d) A single counterexample

**Q8 (Propositional Logic).** P ⇒ (Q ⇒ R) is logically equivalent to:
a) (P ∧ Q) ⇒ R
b) (P ∨ Q) ⇒ R
c) P ∧ Q ∧ R
d) (P ⇒ Q) ∧ R

**Q9 (Propositional Logic).** Which expression is a tautology (always true)?
a) P ∧ ¬P   b) P ∨ ¬P   c) P ⇒ ¬P   d) ¬(P ∨ ¬P)

**Q10 (Predicate Logic).** The negation of ∀x (P(x) ⇒ Q(x)) is:
a) ∀x (P(x) ⇒ ¬Q(x))
b) ∃x (P(x) ∧ ¬Q(x))
c) ∃x (¬P(x) ∧ Q(x))
d) ∀x (¬P(x) ∨ Q(x))

**Q11 (Sequences).** Let a₁ = 3 and aₙ = 2aₙ₋₁ + 1 for n ≥ 2. What is a₅?
a) 31   b) 47   c) 63   d) 127

**Q12 (Series).** What is 1 + 2 + 4 + 8 + … + 2¹⁰?
a) 1023   b) 2047   c) 2048   d) 4095

**Q13 (Growth / Big-O).** Let T(n) = 3 + 6 + 9 + … + 3n. What is the tightest Big-O for T(n)?
a) O(n)   b) O(n log n)   c) O(n²)   d) O(2ⁿ)

**Q14 (Number Theory).** What is gcd(42, 90)?
a) 2   b) 6   c) 12   d) 42

**Q15 (Number Theory).** What is φ(120) (Euler's totient function)?
a) 24   b) 32   c) 40   d) 48

**Q16 (Counting).** Eight distinct books are arranged on a shelf, but the 3 computer-science books must stay together (in a block). How many arrangements are possible?
a) 720   b) 2160   c) 4320   d) 40320

**Q17 (Counting).** How many ways can a committee of 3 be chosen from 10 people?
a) 30   b) 120   c) 720   d) 1000

**Q18 (Probability).** A key is secure with probability 0.7. A test classifies a secure key as "secure" with probability 0.9, and classifies an insecure key as "secure" with probability 0.2. What is the probability the test classifies a random key as "secure"?
a) 0.63   b) 0.69   c) 0.75   d) 0.90

**Q19 (Probability).** Three independent coins have P(heads) = 0.4, 0.6, and 0.9. What is the expected total number of heads?
a) 0.9   b) 1.5   c) 1.9   d) 2.7

**Q20 (Graph Theory).** A simple undirected graph has 8 vertices and 20 edges. What is the average degree of a vertex?
a) 2.5   b) 5   c) 8   d) 40

---

<details>
<summary>Answer key (click to reveal)</summary>

1: b — subsets containing a fixed element = 2⁴ = 16
2: b — 12+10+8 − 5−4−3 + 2 = 20
3: b — true only when A, B are disjoint
4: b — 5 × 4 × 3 = 60
5: b — injectivity of g∘f forces f to be injective
6: c — congruence mod 3 is reflexive, symmetric, transitive
7: b — contrapositive: "if n is odd, then n² is odd"
8: a — both equal ¬P ∨ ¬Q ∨ R
9: b — law of excluded middle
10: b — ¬∀x(…) = ∃x¬(…); ¬(P⇒Q) = P ∧ ¬Q
11: c — closed form aₙ = 2ⁿ⁺¹ − 1, so a₅ = 2⁶ − 1 = 63
12: b — geometric sum = 2¹¹ − 1 = 2047
13: c — 3·n(n+1)/2 = Θ(n²)
14: b — 90 = 2·42 + 6, 42 = 7·6, so gcd = 6
15: b — 120 = 2³·3·5, φ = 120·½·⅔·⅘ = 32
16: c — 6! × 3! = 720 × 6 = 4320
17: b — C(10,3) = 120
18: b — 0.7·0.9 + 0.3·0.2 = 0.63 + 0.06 = 0.69
19: c — 0.4 + 0.6 + 0.9 = 1.9 (linearity of expectation)
20: b — sum of degrees = 2·20 = 40; average = 40/8 = 5

</details>
