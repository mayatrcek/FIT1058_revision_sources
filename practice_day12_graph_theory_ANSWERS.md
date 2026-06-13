# FIT1058 — Day 12 ANSWER KEY · Graph Theory (Ch 11–12)

> Don't peek until you've attempted the set!

**Warm-ups**
- **W1.** P(both red) = (3/8)(2/7) = 6/56 = **3/28 ≈ 0.107**.
- **W2.** Closer to **9%**. Base rate is tiny (1/1000), so false positives swamp true positives. P(sick|+) ≈ (0.001·0.99)/(0.001·0.99 + 0.999·0.01) ≈ 0.00099/0.01098 ≈ **9%**.

**Part A**
- **Q1 — (b) 6.** Handshake lemma: edges = (sum of degrees)/2 = (4+3+2+2+1)/2 = 12/2 = **6**. (And the sequence is realisable as a simple graph, so (d) is wrong.)
- **Q2 — (b).** A tree on n vertices has exactly n−1 edges and is acyclic. (a) is false (n−1, not n); (c) false (trees ARE bipartite); (d) false (leaves have degree 1).
- **Q3 — (c) 5.** V − E + F = 2 → 6 − 9 + F = 2 → F = **5**.
- **Q4 — (a).** Euler tour (closed) exists iff connected and **every vertex has even degree**. Exactly two odd vertices → Euler *path* (open), not a closed tour.

**Part B**
- **Q5 — (a), (b), (d), (e).**
  - (a) True — Handshake Lemma.
  - (b) True — corollary of the Handshake Lemma (odd-degree vertices come in pairs).
  - (c) **False** — K₅ is the classic non-planar graph.
  - (d) True — bipartite ⇔ no odd cycle (König's characterisation).
  - (e) True — a tree has a unique path between any two vertices, so adding an edge closes exactly one cycle.
- **Q6 — (a), (b), (c), (e).**
  - (a) True — standard corollary of Euler's formula for simple connected planar graphs with V ≥ 3.
  - (b) True — K₅ has E = 10 > 9 = 3·5−6, so non-planar.
  - (c) True — if every vertex had degree ≥ 6 then 2E ≥ 6V → E ≥ 3V, contradicting E ≤ 3V−6.
  - (d) **False** — K₃,₃ has E = 9 and 3V−6 = 12, so it *satisfies* E ≤ 3V−6; the simple bound is NOT enough. You need the bipartite/girth-4 bound **E ≤ 2V−4** (= 8 < 9) to rule out K₃,₃.
  - (e) True (for simple connected planar graphs, V ≥ 3).

**Part C**

**Q7 — Handshake Lemma proof (model answer).**
*Claim:* In any graph G, the number of odd-degree vertices is even.
*Proof (direct, by counting).* Let G have vertex set V and edge set E. Each edge has two endpoints, so when we add up the degrees of all vertices, every edge is counted exactly twice:
  ∑_{v∈V} deg(v) = 2|E|.   (★)
So the total degree sum is even.
Partition V into O (odd-degree vertices) and N (even-degree vertices). Then
  ∑_{v∈O} deg(v) + ∑_{v∈N} deg(v) = 2|E|.
The second sum is a sum of even numbers, hence even. Subtracting it from the even total (★) leaves
  ∑_{v∈O} deg(v) = even.
But this is a sum of |O| odd numbers. A sum of odd numbers is even **iff** the count of them is even. Therefore |O| is even. ∎
*(Marking: identifies method, states ∑deg = 2|E|, splits into odd/even sets, concludes |O| even. Each line justified.)*

**Q8.**
- **(a) Impossible.** 9 people each of degree 3 → sum of degrees = 9×3 = 27, which is **odd**. But the degree sum must equal 2×(handshakes), an even number. Contradiction → no such graph (equivalently, you can't have an odd number — 9 — of odd-degree vertices). 
- **(b)** 10 people × degree 3 = 30 = sum of degrees = 2 × (handshakes), so handshakes = 30/2 = **15**.

---
*After marking, copy any mistakes into `error_log.md` with the correct method.*
