# FIT1058 — Day 4 Practice: Proofs II, Induction (Ch 3)

**Date:** Fri 5 June 2026 · 10 days to exam
**Instructions:** Attempt all 7. The real paper mixes single-answer MCQs, select-all, and full written proofs — so write the proofs out **completely** (state the method, base case, hypothesis, step). Reply with your answers and I'll mark them. Answer key is in a separate file (`practice_day04_induction_ANSWERS.md`) — don't peek until you've attempted everything.

---

## Q1 — MCQ (base case)
You want to prove a statement P(n) holds for all integers n ≥ 3. Which is the correct **base case**?

- (a) P(0)
- (b) P(1)
- (c) P(3)
- (d) P(n+1)

---

## Q2 — MCQ (the inductive hypothesis)
In a proof that 6 | (7ⁿ − 1) for all n ≥ 1, the inductive hypothesis is:

- (a) Assume 6 | (7ⁿ − 1) for **all** n ≥ 1.
- (b) Assume 6 | (7ᵏ − 1) for some fixed k ≥ 1, then show 6 | (7ᵏ⁺¹ − 1).
- (c) Assume 6 | (7ᵏ⁺¹ − 1) and deduce 6 | (7ᵏ − 1).
- (d) Assume 6 | (7ᵏ − 1) and 6 | (7ᵏ⁺¹ − 1).

---

## Q3 — Select all that apply (valid reasoning)
Which of the following are **true** about proof by induction? (Choose all correct.)

- (a) The inductive step proves the implication P(k) ⇒ P(k+1), not P(k+1) on its own.
- (b) Without a verified base case, the inductive step alone proves the statement.
- (c) Strong induction lets you assume P(j) for all j with base ≤ j ≤ k when proving P(k+1).
- (d) If P(k) ⇒ P(k+1) holds but the base case is false, the statement may still be false for all n.
- (e) Induction can only prove statements about summation formulas.

---

## Q4 — Written proof (summation)
Prove by induction that for all integers n ≥ 1:

  1 + 3 + 5 + ⋯ + (2n − 1) = n²

Write the full proof (base case, hypothesis, inductive step).

---

## Q5 — Written proof (divisibility) ★
Prove by induction that for all integers n ≥ 1:

  6 divides (7ⁿ − 1)

Show your algebra in the inductive step explicitly.

---

## Q6 — Written proof (inequality) ★
Prove by induction that for all integers n ≥ 5:

  2ⁿ > n²

(Hint: in the step you'll need 2k² ≥ (k+1)² for k ≥ 5 — justify it.)

---

## Q7 — Written proof (strong induction) ★
Using **strong** induction, prove that every integer amount of postage of **12 cents or more** can be formed using only **4-cent** and **5-cent** stamps.

State clearly which base cases you need and why strong (not weak) induction is the right tool here.

---

*When you've attempted these, send me your answers (even partial) and I'll mark them and log any mistakes to `error_log.md`.*
