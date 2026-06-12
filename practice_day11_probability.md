# FIT1058 — Day 11 Practice · Discrete Probability I & II (Ch 9–10)

**Fri 12 Jun 2026 · 3 days to exam.** Attempt these cold, then reply with your answers (e.g. "Q1: c, Q2: a&d…") and I'll mark them. Answer key is in a separate file — don't peek.

Format mirrors the real paper: single-answer MCQs, select-all, and written work. Show working on the calculation questions — method marks matter.

---

### Warm-up (spaced repetition — Day 10 logic)

**W1.** Using named logical equivalences (no truth table), simplify
¬(p ∨ ¬q) ∨ (¬p ∧ ¬q)
to its simplest form. Name each rule you use (De Morgan, distributive, etc.).

---

### Part A — Multiple choice (single answer)

**Q1.** A fair six-sided die is rolled twice. Let the sample space be ordered pairs (i, j), all equally likely. What is Pr(sum = 7)?

- (a) 1/12
- (b) 5/36
- (c) 1/6
- (d) 7/36

**Q2.** Events A and B satisfy Pr(A) = 0.5, Pr(B) = 0.4, Pr(A ∩ B) = 0.2. What is Pr(A ∪ B)?

- (a) 0.9
- (b) 0.7
- (c) 0.8
- (d) 0.2

**Q3.** A test for a disease has sensitivity Pr(+ | D) = 0.95 and specificity Pr(− | ¬D) = 0.90. The disease prevalence is Pr(D) = 0.01. A person tests positive. Using Bayes' Theorem, Pr(D | +) is closest to:

- (a) 0.95
- (b) 0.50
- (c) 0.09
- (d) 0.01

**Q4.** X is a geometric random variable counting the number of independent Bernoulli trials up to and including the first success, with success probability p = 0.2 on each trial. The expected number of trials E(X) is:

- (a) 0.2
- (b) 5
- (c) 25
- (d) 1/25

**Q5.** Cosmic rays hit a CPU as a Poisson process with mean λ = 3 per hour. The probability that **zero** rays hit in a given hour is:

- (a) e⁻³ ≈ 0.050
- (b) 1 − e⁻³ ≈ 0.950
- (c) 3e⁻³ ≈ 0.149
- (d) 1/3

---

### Part B — Select all that apply

**Q6.** Two events A and B are **independent**. Which of the following must be true? (Select ALL that apply.)

- (a) Pr(A ∩ B) = Pr(A)·Pr(B)
- (b) Pr(A ∪ B) = Pr(A) + Pr(B)
- (c) Pr(A | B) = Pr(A), provided Pr(B) > 0
- (d) A and B are mutually exclusive
- (e) Pr(B | A) = Pr(B), provided Pr(A) > 0

**Q7.** Which of the following statements about **expectation** are correct? (Select ALL that apply.)

- (a) E(X + Y) = E(X) + E(Y) for any random variables X, Y (even if dependent)
- (b) E(aX + b) = a·E(X) + b for constants a, b
- (c) E(XY) = E(X)·E(Y) for any random variables X, Y
- (d) The expectation of a constant c is c
- (e) E(X) must be one of the values X can actually take

---

### Part C — Written / calculation (show full working)

**Q8.** A program is tested on 8 independent random inputs. Each input independently triggers a bug with probability p = 0.25. Let X be the number of inputs (out of 8) that trigger the bug.

(a) Name the distribution of X and state its parameters.
(b) Write the formula for Pr(X = k), then compute Pr(X = 2). Give a decimal to 3 d.p.
(c) Compute Pr(X ≥ 1), the probability that **at least one** input triggers the bug. (Hint: use the complement.)
(d) State E(X) and Var(X).

**Q9.** (Linearity of expectation — proof-style.) A fair six-sided die is rolled 10 times. Let S be the sum of the 10 results.

(a) Let Xᵢ be the result of the i-th roll. Write S in terms of the Xᵢ.
(b) Compute E(Xᵢ) for a single fair die.
(c) Using **linearity of expectation**, prove that E(S) = 35. Justify the step where you use linearity, and state explicitly whether the rolls need to be independent for this argument to work.

---

*When you reply with answers I'll mark them, explain anything you miss, and add slips to `error_log.md`. Tomorrow (Sat 13 Jun) is Graph Theory; Sun 14 Jun is your full timed mock.*
