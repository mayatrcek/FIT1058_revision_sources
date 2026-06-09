# FIT1058 — Day 8 Practice · Counting & Combinatorics I (Ch 8)

**Date:** Tue 9 Jun 2026 · 6 days to exam
**Topic:** addition/multiplication principles, permutations, combinations, choose-then-arrange vs just-choose
**Format:** mix of single-answer MCQ, one select-all, and two written questions (show full working). Attempt everything before opening the answer key.

> Exam habit: on counting questions, **show your method** (which principle, why permutation vs combination) — method marks matter even if the arithmetic slips.

---

**Q1 (Multiplication principle).** How many bit strings of length 8 start with a `1` and end with `00`?
a) 8   b) 32   c) 64   d) 128

**Q2 (Permutations).** A school has 8 distinct trophies and a display rail with room for 5, arranged in a row. How many different displays are possible?
a) 56   b) 336   c) 6720   d) 40320

**Q3 (Combinations).** A pizza shop offers 12 toppings. How many ways can you choose exactly 4 *different* toppings (order irrelevant)?
a) 24   b) 495   c) 11880   d) 20736

**Q4 (Permutations with a block).** Seven friends sit in a row of 7 seats. Two of them, Ali and Bo, insist on sitting next to each other. How many seating arrangements are possible?
a) 720   b) 1440   c) 5040   d) 10080

**Q5 (Select all that apply).** A club of 10 people must pick a **President, Vice-President, and Secretary** (three distinct named roles, one person per role). Which of the following expressions correctly count the number of ways?
a) P(10, 3)
b) 10 × 9 × 8
c) C(10, 3) × 3!
d) C(10, 3)
e) 10! / 7!

**Q6 ("Apart" via complement).** Six distinct books are placed in a row on a shelf. In how many arrangements are two particular books (a matched dictionary pair) **not** next to each other?
a) 240   b) 480   c) 600   d) 1440

**Q7 (Written — show full working).** A committee of 4 is to be formed from a group of **7 men and 5 women**. How many possible committees contain **at least one woman**? State the principle you use and show every step.

**Q8 (Written proof — combinatorial argument).** Let n and r be integers with 0 ≤ r ≤ n. Prove that
$$\binom{n}{r} = \binom{n}{n-r}.$$
Give a **combinatorial proof** (a counting/bijection argument), not just algebra. Clearly state what set you are counting in two ways.

---

<details>
<summary>Answer key + worked solutions (click to reveal — try them first!)</summary>

**Q1 — b) 32.** Position 1 is fixed as `1`; positions 7–8 are fixed as `00`. The remaining 5 positions (2–6) are free: 2⁵ = **32**. (Multiplication principle: 1×2×2×2×2×2×1×1.)

**Q2 — c) 6720.** Order matters and no repetition → permutation P(8,5) = 8×7×6×5×4 = **6720**. (Distractor 40320 = 8!, distractor 56 = C(8,2).)

**Q3 — b) 495.** Order doesn't matter → combination C(12,4) = (12×11×10×9)/(4×3×2×1) = 11880/24 = **495**. (Distractor 11880 = P(12,4) forgets to divide by 4!.)

**Q4 — b) 1440.** "Together" = glue Ali+Bo into one block → arrange 6 objects = 6! = 720, then arrange the two inside the block = 2! = 2. Total 6!·2! = 720×2 = **1440**.

**Q5 — a, b, c, e.** All equal 720, the number of ordered selections of 3 from 10:
- (a) P(10,3) = 720 ✓
- (b) 10×9×8 = 720 ✓ (multiplication principle directly)
- (c) C(10,3)×3! = 120×6 = 720 ✓ ("choose the 3 people, then arrange them into the 3 roles")
- (e) 10!/7! = P(10,3) = 720 ✓
- (d) C(10,3) = 120 ✗ — this only *chooses* the trio, it does not assign the distinct roles, so it undercounts by a factor of 3!.

Takeaway: distinct named roles ⇒ order matters ⇒ permutation. C(10,3) alone is the "just choose" answer and is wrong here.

**Q6 — b) 480.** Use the complement. Total arrangements = 6! = 720. Arrangements with the two books **together** = 5!·2! = 120×2 = 240. Not together = 720 − 240 = **480**.

**Q7 — 460.** Principle: complement (easier than summing cases).
- Total committees of 4 from 12 people: C(12,4) = 495.
- Committees with **no women** (all 4 from the 7 men): C(7,4) = 35.
- At least one woman = total − none = 495 − 35 = **460**.

(Check by direct cases — exactly 1,2,3, or 4 women:
C(5,1)C(7,3) + C(5,2)C(7,2) + C(5,3)C(7,1) + C(5,4)C(7,0)
= 5·35 + 10·21 + 10·7 + 5·1 = 175 + 210 + 70 + 5 = 460. ✓)

**Q8 — Combinatorial proof of C(n,r) = C(n,n−r).**

*Claim:* For 0 ≤ r ≤ n, the number of r-element subsets of an n-element set equals the number of (n−r)-element subsets.

*Proof.* Let S be a set with |S| = n. By definition, the left side $\binom{n}{r}$ counts the r-element subsets of S, and the right side $\binom{n}{n-r}$ counts the (n−r)-element subsets of S.

Define a map φ that sends each subset A ⊆ S to its complement φ(A) = S \ A. If |A| = r, then |S \ A| = n − r, so φ takes r-element subsets to (n−r)-element subsets.

φ is a **bijection** between the family of r-subsets and the family of (n−r)-subsets:
- *Injective:* if S \ A = S \ B then A = B (taking complements again).
- *Surjective:* any (n−r)-subset B is hit by A = S \ B, since φ(S \ B) = S \ (S \ B) = B, and |S \ B| = r.

Because a bijection exists between the two families, they have the same size. Therefore $\binom{n}{r} = \binom{n}{n-r}$. ∎

*Why this earns full marks:* it names the method (count one set two ways / build a bijection), defines the objects, and verifies the map is both injective and surjective rather than just asserting "they pair up."

</details>

---

*When done, log any misses in `error_log.md` with the correct method, then reply here with your answers for marking.*
