# FIT1058 — Day 9 Practice · Counting & Combinatorics II (Ch 8)

**Date:** Wed 10 Jun 2026 · 5 days to exam
**Topic:** Binomial Theorem, Pascal's identity, Inclusion–Exclusion for counting, Pigeonhole principle, stars-and-bars, "at least/at most" via complements
**Format:** mix of single-answer MCQ, one select-all, and two written questions (show full working). Attempt everything before opening the answer key.

> Exam habit: on counting questions **show your method** (which principle, why). On the pigeonhole/IE questions, state the principle by name — method marks matter even if arithmetic slips.

---

**Q1 (Binomial Theorem — single coefficient).** In the expansion of $(2x + 3)^5$, what is the coefficient of $x^3$?
a) 80   b) 360   c) 720   d) 1080

**Q2 (Sum of a binomial row).** What is $\displaystyle\sum_{k=0}^{10}\binom{10}{k}$?
a) 100   b) 512   c) 1024   d) 2048

**Q3 (Pascal's identity).** Which single binomial coefficient equals $\dbinom{9}{4} + \dbinom{9}{5}$?
a) $\binom{9}{9}$   b) $\binom{10}{4}$   c) $\binom{10}{5}$   d) $\binom{18}{9}$

**Q4 (Inclusion–Exclusion).** How many integers from 1 to 100 inclusive are divisible by **none** of 2, 3, or 5?
a) 20   b) 26   c) 30   d) 74

**Q5 (Pigeonhole — generalised).** What is the minimum number of people needed in a room to **guarantee** that at least 3 of them share the same birth month?
a) 13   b) 24   c) 25   d) 37

**Q6 (Stars and bars).** How many solutions in **non-negative integers** are there to
$$x_1 + x_2 + x_3 + x_4 = 12 \quad ?$$
a) 165   b) 220   c) 455   d) 4096

**Q7 (Select all that apply).** Which of the following expressions are equal to $\dbinom{8}{3}$?
a) $\binom{8}{5}$
b) $\dfrac{8!}{3!\,5!}$
c) $\binom{7}{2} + \binom{7}{3}$
d) $\dfrac{P(8,3)}{3!}$
e) $\binom{8}{2}$

**Q8 (Written — applied counting, show full working).** A standard deck has 52 cards: 13 ranks in each of 4 suits. A 5-card hand is dealt. How many 5-card hands contain **at least one** card of each of the four suits? State your principle and show every step. *(Hint: a 5-card hand covering all four suits has suit pattern 2-1-1-1 — one suit contributes two cards, the others one each.)*

**Q9 (Written proof — combinatorial argument).** Let $n$ and $r$ be integers with $1 \le r \le n$. Prove **Pascal's identity**
$$\binom{n}{r} = \binom{n-1}{r-1} + \binom{n-1}{r}$$
by a **combinatorial argument** (count one set two ways), not algebra. Clearly state the set you are counting and how you split it.

---

<details>
<summary>Answer key + worked solutions (click to reveal — try them first!)</summary>

**Q1 — c) 720.** Binomial Theorem: the term in $x^3$ is $\binom{5}{3}(2x)^3(3)^2 = 10 \cdot 8x^3 \cdot 9 = 720x^3$. The general term of $(a+b)^n$ is $\binom{n}{k}a^{n-k}b^k$; here $a=2x$, $b=3$, and $x^3$ needs the $(2x)^3$ piece, i.e. $k=2$ on the constant, $\binom{5}{2}=\binom{5}{3}=10$. Coefficient $= 10\cdot 2^3 \cdot 3^2 = \mathbf{720}$. (Distractor 1080 forgets the $2^3$; 80 keeps only $\binom{5}{3}\cdot 2^3$ and drops $3^2$.)

**Q2 — c) 1024.** $\sum_{k=0}^{n}\binom{n}{k} = 2^n$ (each element of an $n$-set is either in or out of a subset; total subsets $=2^n$). Here $2^{10} = \mathbf{1024}$.

**Q3 — c) $\binom{10}{5}$.** Pascal's identity: $\binom{n-1}{r-1}+\binom{n-1}{r}=\binom{n}{r}$. With $n=10$, $r=5$: $\binom{9}{4}+\binom{9}{5}=\binom{10}{5}=\mathbf{252}$. (The two lower indices, 4 and 5, must sum to the new upper index's role — they're $r-1$ and $r$.)

**Q4 — b) 26.** Inclusion–Exclusion. Let $A_d$ = multiples of $d$ in $[1,100]$, so $|A_d|=\lfloor 100/d\rfloor$.
$|A_2{\cup}A_3{\cup}A_5| = |A_2|+|A_3|+|A_5| - |A_6|-|A_{10}|-|A_{15}| + |A_{30}|$
$= 50+33+20 - 16-10-6 + 3 = 74.$
Divisible by **none** $= 100 - 74 = \mathbf{26}$. (74 is the trap — that's "at least one", not "none".)

**Q5 — c) 25.** Generalised pigeonhole: to force $\lceil k/n\rceil \ge 3$ with $n=12$ months you need $k$ such that the worst case (2 per month $= 24$) is exceeded. $2\cdot 12 + 1 = \mathbf{25}$. With 24 people you *could* have exactly 2 in every month and no trio; the 25th forces a third somewhere.

**Q6 — c) 455.** Stars and bars: non-negative integer solutions of $x_1+\dots+x_k=n$ number $\binom{n+k-1}{k-1}$. Here $n=12$, $k=4$: $\binom{12+4-1}{4-1}=\binom{15}{3}=\mathbf{455}$. (Distractor 165 $=\binom{11}{3}$ is the *positive* count $x_i\ge 1$; 4096 $=4^{12}$ wrongly treats it as functions.)

**Q7 — a, b, c, d.** All equal $\binom{8}{3}=56$:
- (a) $\binom{8}{5}=\binom{8}{3}=56$ ✓ (symmetry, Day 8's identity).
- (b) $\frac{8!}{3!5!}=56$ ✓ (the definition).
- (c) $\binom{7}{2}+\binom{7}{3}=21+35=56$ ✓ (Pascal's identity).
- (d) $\frac{P(8,3)}{3!}=\frac{336}{6}=56$ ✓ ("choose then divide out the order").
- (e) $\binom{8}{2}=28$ ✗ — not equal.

**Q8 — 685,464 hands.** Principle: multiplication principle within a case, summed over the choice of which suit "doubles".
- A 5-card hand using all four suits must have one suit appearing twice and the other three once (pattern 2-1-1-1).
- Choose which suit is the doubled one: $\binom{4}{1}=4$ ways.
- That suit contributes 2 of its 13 cards: $\binom{13}{2}=78$.
- Each of the other three suits contributes 1 of its 13: $\binom{13}{1}^3 = 13^3 = 2197$.
- Total $= 4 \times 78 \times 2197 = \mathbf{685{,}464}$.

(Sanity scale-check: total 5-card hands $=\binom{52}{5}=2{,}598{,}960$, so ≈26% cover all four suits — plausible.)

**Q9 — Combinatorial proof of Pascal's identity.**

*Claim:* For $1\le r\le n$, $\binom{n}{r}=\binom{n-1}{r-1}+\binom{n-1}{r}$.

*Proof.* Let $S=\{1,2,\dots,n\}$, an $n$-element set. By definition the left side $\binom{n}{r}$ counts the $r$-element subsets of $S$. We count the same collection a second way.

Fix a distinguished element, say $n$. Every $r$-element subset $A\subseteq S$ falls into exactly one of two disjoint cases:

- **Case 1: $n\in A$.** Then $A$ consists of $n$ together with $r-1$ elements chosen from the remaining $n-1$ elements $\{1,\dots,n-1\}$. There are $\binom{n-1}{r-1}$ such subsets.
- **Case 2: $n\notin A$.** Then all $r$ elements of $A$ come from $\{1,\dots,n-1\}$, giving $\binom{n-1}{r}$ such subsets.

The two cases are mutually exclusive (a subset either contains $n$ or it doesn't) and exhaustive (every $r$-subset is in one of them). By the addition principle, the total number of $r$-subsets is
$$\binom{n}{r}=\binom{n-1}{r-1}+\binom{n-1}{r}. \qquad\blacksquare$$

*Why this earns full marks:* it names the method (count one set two ways), defines the set, splits it into cases that are clearly disjoint and exhaustive, and invokes the addition principle by name — rather than just manipulating factorials.

</details>

---

*When done, log any misses in `error_log.md` with the correct method, then reply here with your answers for marking.*
