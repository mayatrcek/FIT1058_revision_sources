# FIT1058 — 30-Question Mixed MCQ Mock (All Topics, Ch 1–12)

**Date:** Sat 13 June 2026 · **Exam:** Mon 15 June
**Format:** single-answer multiple choice, "Select one:" (a–d), matching the practice-exam style.
Attempt cold, no notes. Reply with your answers (e.g. "Q1: b, Q2: d…") and I'll mark them. Answer key is in a separate file.

> Typing tip (as in the real paper): use `^` for exponents and `_` for subscripts — e.g. `2^(n+1)`, `a_n`.

---

## Sets (Ch 1)

**Q1.** Given U = {1, 2, …, 10}, A = {1, 3, 5, 7, 9}, B = {2, 3, 5, 7}, C = {1, 2, 5, 8, 9}. Which expression equals **{3, 7}**?

- a. A ∩ B
- b. (A ∩ B) \ C
- c. A \ B
- d. A ∩ B ∩ C

**Q2.** For nonempty, finite sets A and B, which of the following is **not always true**?

- a. |A ∪ B| + |A ∩ B| = |A| + |B|
- b. |A △ B| = |A ∪ B| − |A ∩ B|
- c. |A ∩ B| = |A| if and only if A ⊆ B
- d. |A ∪ B| = |A| + |B|

**Q3.** Let A and B be subsets of a universal set U. Which statement about A △ B (symmetric difference) is **always true**?

- a. A △ B = (A ∩ B)‾
- b. A △ B = (A‾ ∩ B) ∪ (A ∩ B‾)
- c. A △ B = (A ∪ B)‾
- d. A △ B = (A‾ ∩ B‾) ∪ (A ∩ B)

---

## Functions & Relations (Ch 2)

**Q4.** Let f : A → B and g : B → C be functions. Which of the following is **always true**?

- a. If g ∘ f is surjective, then f is surjective.
- b. If g ∘ f is injective, then f is injective.
- c. If f is surjective and g is injective, then g ∘ f is bijective.
- d. If g ∘ f is bijective, then both f and g are bijective.

**Q5.** On the set {1, 2, 3}, which of the following relations is an **equivalence relation**?

- a. {(1,1), (2,2), (3,3), (1,2), (2,3), (1,3)}
- b. {(1,1), (2,2), (3,3), (1,2), (2,1)}
- c. {(1,1), (2,2), (1,2), (2,1)}
- d. {(1,1), (2,2), (3,3), (1,2), (2,1), (1,3)}

**Q6.** How many **injective** functions are there from a 3-element set to a 5-element set?

- a. 5³ = 125
- b. 5 · 4 · 3 = 60
- c. 3⁵ = 243
- d. C(5, 3) = 10

---

## Proofs & Induction (Ch 3)

**Q7.** To prove "if n² is even then n is even" by **contrapositive**, you should:

- a. assume n² is even and n is odd, and derive a contradiction
- b. assume n is odd, and show n² is odd
- c. assume n is even, and show n² is even
- d. assume n² is odd, and show n is odd

**Q8.** Which statement correctly describes the standard proof that √2 is irrational?

- a. Assume √2 = a/b in lowest terms, then derive that a and b are both even — a contradiction.
- b. Assume √2 is irrational, then derive a contradiction.
- c. The "lowest terms" assumption is not needed for the proof.
- d. Check every rational a/b individually and show none equals √2.

**Q9.** When proving ∑_{i=1}^{n} i = n(n+1)/2 by induction, the inductive step assumes the result for n = k and must reach which target for n = k + 1?

- a. (k+1)(k+2)/2
- b. k(k+1)/2 + 1
- c. (k+1)(k+1)/2
- d. k(k+2)/2

---

## Sequences & Series (Ch 6)

**Q10.** The sequence is defined by a₁ = 3 and a_n = 2·a_{n−1} + 1 for n ≥ 2. Which is a correct closed form?

- a. 2^(n+1) − 1
- b. 2^n − 1
- c. 2^n + 1
- d. 3 · 2^(n−1)

**Q11.** What is ∑_{k=1}^{n} 2^k (note: the sum starts at k = 1)?

- a. 2^(n+1) − 1
- b. 2^(n+1) − 2
- c. 2^n − 1
- d. 2^n − 2

---

## Number Theory (Ch 7)

**Q12.** Using the Euclidean Algorithm, gcd(252, 198) = ?

- a. 6
- b. 9
- c. 18
- d. 36

**Q13.** Given 120 = 2³ · 3 · 5, the value of Euler's totient φ(120) is:

- a. 24
- b. 32
- c. 40
- d. 48

**Q14.** Which statement is true about the integer 14?

- a. 14 has no primitive roots because it is even.
- b. 14 has no primitive roots because it is not prime.
- c. 14 has primitive roots because it is of the form 2p, where p is an odd prime.
- d. 14 has primitive roots because φ(14) = 6, which is even.

**Q15.** The modular inverse of 3 modulo 7 (i.e. the x with 3x ≡ 1 (mod 7)) is:

- a. 2
- b. 4
- c. 5
- d. 6

---

## Counting & Combinatorics (Ch 8)

**Q16.** How many distinct arrangements are there of the letters of the word **BANANA**?

- a. 720
- b. 360
- c. 120
- d. 60

**Q17.** In how many ways can a committee of 3 be chosen from 10 people (order does not matter)?

- a. 720
- b. 120
- c. 30
- d. 1000

**Q18.** How many 5-letter strings can be formed from a 26-letter alphabet if **no letter is repeated**?

- a. 26⁵
- b. 26 · 25 · 24 · 23 · 22
- c. C(26, 5)
- d. 5²⁶

**Q19.** What is the minimum number of people required to **guarantee** that at least two share the same birth month (pigeonhole)?

- a. 12
- b. 13
- c. 7
- d. 24

---

## Logic (Ch 4–5)

**Q20.** The implication P ⇒ Q is logically equivalent to:

- a. ¬P ∨ Q
- b. P ∨ ¬Q
- c. ¬P ∧ Q
- d. P ∧ ¬Q

**Q21.** The negation of ∀x (P(x) ⇒ Q(x)) is logically equivalent to:

- a. ∀x (P(x) ∧ ¬Q(x))
- b. ∃x (P(x) ∧ ¬Q(x))
- c. ∃x (¬P(x) ∨ Q(x))
- d. ∀x (¬P(x) ⇒ ¬Q(x))

**Q22.** Which is the **contrapositive** of "If it rains, then the ground is wet"?

- a. If the ground is wet, then it rained.
- b. If it does not rain, then the ground is not wet.
- c. If the ground is not wet, then it did not rain.
- d. It rains and the ground is not wet.

---

## Discrete Probability (Ch 9–10)

**Q23.** A fair six-sided die is rolled once. What is P(even | the result is greater than 3)?

- a. 1/2
- b. 2/3
- c. 1/3
- d. 1/6

**Q24.** Two fair coins are flipped. What is P(at least one head)?

- a. 1/2
- b. 1/4
- c. 3/4
- d. 2/3

**Q25.** A disease affects 1% of a population. A test has 90% sensitivity (true-positive rate) and a 5% false-positive rate. By Bayes' theorem, P(disease | positive test) is closest to:

- a. 90%
- b. 50%
- c. 15%
- d. 1%

---

## Graph Theory (Ch 11–12)

**Q26.** A simple graph has degree sequence (3, 3, 3, 3). How many edges does it have?

- a. 3
- b. 4
- c. 6
- d. 12

**Q27.** A connected planar graph is drawn with 8 vertices and 12 edges. By Euler's formula (V − E + F = 2), how many faces does the drawing have?

- a. 4
- b. 5
- c. 6
- d. 8

**Q28.** Which of the following statements is **always true**?

- a. Every tree with n vertices has exactly n − 1 edges.
- b. Every connected graph has an Euler tour.
- c. The complete graph K₅ is planar.
- d. Every bipartite graph contains an odd cycle.

**Q29.** A connected graph has an **Euler tour** (a closed walk using every edge exactly once) if and only if:

- a. every vertex has even degree
- b. exactly two vertices have odd degree
- c. it is a tree
- d. it has a Hamiltonian cycle

---

## Mixed (Ch 1 / foundations)

**Q30.** How many elements are in the power set of a set with 4 elements?

- a. 8
- b. 16
- c. 4
- d. 24

---

*Send me your answers and I'll mark them, then log any errors into `error_log.md`. Aim for ~1 minute per question to simulate exam pace.*
