# FIT1058 — Day 4 Practice ANSWER KEY (Induction)

**Don't open until you've attempted the questions.**

---

## Q1 — (c) P(3)
The base case must be the smallest value in the claimed range. The claim is "for all n ≥ 3", so you anchor at n = 3.

## Q2 — (b)
The hypothesis fixes one arbitrary k and assumes the statement there, then the step derives the k+1 case. (a) assumes the whole result (circular). (c) runs the implication backwards. (d) assumes the very thing you must prove.

## Q3 — (a), (c), (d) are true.
- (a) ✓ The step is an implication, not a standalone proof of P(k+1).
- (b) ✗ The base case is essential; the implication chain needs a true starting point.
- (c) ✓ That is exactly the strong-induction hypothesis.
- (d) ✓ E.g. "n = n+1" satisfies P(k) ⇒ P(k+1) trivially-style chains can carry a false start; a false base means nothing is anchored.
- (e) ✗ Induction proves divisibility, inequalities, recurrences, structural claims, etc.

## Q4 — Sum of first n odd numbers = n²
**Base (n=1):** LHS = 1, RHS = 1² = 1. ✓
**Hypothesis:** Assume 1 + 3 + ⋯ + (2k−1) = k² for some k ≥ 1.
**Step (n=k+1):** Add the next odd number, 2(k+1)−1 = 2k+1:
  1 + 3 + ⋯ + (2k−1) + (2k+1) = k² + (2k+1)   [by hypothesis]
  = k² + 2k + 1 = (k+1)².  ✓
By induction the formula holds for all n ≥ 1. ∎

## Q5 — 6 | (7ⁿ − 1)
**Base (n=1):** 7¹ − 1 = 6, and 6 | 6. ✓
**Hypothesis:** Assume 6 | (7ᵏ − 1), i.e. 7ᵏ − 1 = 6m for some integer m, so 7ᵏ = 6m + 1.
**Step (n=k+1):**
  7ᵏ⁺¹ − 1 = 7·7ᵏ − 1 = 7(6m + 1) − 1 = 42m + 7 − 1 = 42m + 6 = 6(7m + 1).
Since 7m + 1 is an integer, 6 | (7ᵏ⁺¹ − 1). ✓
By induction, 6 | (7ⁿ − 1) for all n ≥ 1. ∎

## Q6 — 2ⁿ > n² for n ≥ 5
**Base (n=5):** 2⁵ = 32 > 25 = 5². ✓
**Hypothesis:** Assume 2ᵏ > k² for some k ≥ 5.
**Step (n=k+1):**
  2ᵏ⁺¹ = 2·2ᵏ > 2k²   [by hypothesis].
Now show 2k² ≥ (k+1)²: 2k² − (k+1)² = k² − 2k − 1 = (k−1)² − 2. For k ≥ 5, (k−1)² ≥ 16 > 2, so this is positive, hence 2k² > (k+1)².
Therefore 2ᵏ⁺¹ > 2k² > (k+1)². ✓
By induction, 2ⁿ > n² for all n ≥ 5. ∎

## Q7 — Postage with 4c and 5c stamps, amounts ≥ 12 (strong induction)
**Why strong induction:** the construction for amount n reuses the solution for n−4, so we need the result to hold for a smaller value that may be several steps back, not just n−1.

**Base cases (n = 12, 13, 14, 15):**
- 12 = 4+4+4
- 13 = 4+4+5
- 14 = 4+5+5
- 15 = 5+5+5
We need four consecutive base cases because the inductive step steps down by 4; this guarantees n−4 always lands on a value we've already established (≥ 12).

**Inductive step (n ≥ 16):** Assume every amount j with 12 ≤ j < n is formable. Since n ≥ 16, n − 4 ≥ 12, so by the (strong) hypothesis n − 4 is formable as some combination of 4c and 5c stamps. Add one more 4c stamp to get n. ✓

By strong induction, every amount ≥ 12 cents is formable. ∎

---
*Marking note: on the written proofs, full marks need (1) named method, (2) explicit base case checked, (3) clearly stated hypothesis, (4) the algebra/logic of the step shown, (5) a concluding line. Partial structure still earns method marks — always write the skeleton even if you stall.*
