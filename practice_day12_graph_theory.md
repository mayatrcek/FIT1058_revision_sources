# FIT1058 — Day 12 Practice · Graph Theory I & II (Ch 11–12)

**Date:** Sat 13 June 2026 · **Exam:** Mon 15 June (2 days to go)
**Format:** mix of single-answer MCQ, select-all, and written proof — same as the real paper.
Attempt these cold (no notes), then reply with your answers and I'll mark them. Answer key is kept separate.

---

### Warm-up (do first, ~15 min) — spaced repetition from Day 11 (Probability)
- **W1.** A bag has 3 red and 5 blue balls. You draw 2 without replacement. What is P(both red)?
- **W2.** A test is 99% accurate for a disease present in 1 in 1000 people. Given a positive result, is P(actually sick) closer to 99% or to 9%? (One line of reasoning — this is Bayes.)

---

## Part A — Multiple choice (choose ONE)

**Q1.** A simple graph has degree sequence (4, 3, 2, 2, 1). How many edges does it have?

- (a) 5
- (b) 6
- (c) 12
- (d) This degree sequence is impossible for a simple graph

**Q2.** Which of the following must be true for *every* tree with n ≥ 1 vertices?

- (a) It has exactly n edges
- (b) It has exactly n − 1 edges and contains no cycle
- (c) It is always planar but never bipartite
- (d) Every vertex has degree at least 2

**Q3.** A connected planar graph is drawn in the plane with 6 vertices and 9 edges. By Euler's formula (V − E + F = 2), how many faces does the drawing have (including the unbounded outer face)?

- (a) 3
- (b) 4
- (c) 5
- (d) 7

**Q4.** A connected graph has an **Euler tour** (a closed walk using every edge exactly once) if and only if:

- (a) it has no vertices of odd degree
- (b) it has exactly two vertices of odd degree
- (c) every vertex has even degree *and* the graph is a tree
- (d) it has a Hamiltonian cycle

---

## Part B — Select ALL that apply

**Q5.** Which of the following statements are **true**? (Select all.)

- (a) In any graph, the sum of all vertex degrees equals twice the number of edges.
- (b) Every graph has an even number of odd-degree vertices.
- (c) The complete graph K₅ is planar.
- (d) A graph is bipartite if and only if it contains no odd-length cycle.
- (e) Adding one edge to a tree (between two existing vertices) always creates exactly one cycle.

**Q6.** Let G be a simple connected planar graph with V ≥ 3 vertices and E edges. Which of the following are valid consequences of Euler's formula? (Select all.)

- (a) E ≤ 3V − 6
- (b) K₅ is non-planar because it would need E ≤ 3·5 − 6 = 9 but has E = 10
- (c) Every planar graph has a vertex of degree ≤ 5
- (d) K₃,₃ is non-planar, and the bound E ≤ 3V − 6 alone is enough to prove it
- (e) A planar graph can have at most 3V − 6 edges regardless of V

---

## Part C — Written / proof (show full working — method marks matter)

**Q7. (Handshake Lemma — full proof.)**
Prove the following statement carefully, justifying each step:

> *In any graph G, the number of vertices of odd degree is even.*

State your method, define your variables, and lay the argument out line by line. (Hint: start from the sum of all degrees and split the vertices into odd-degree and even-degree groups.)

**Q8. (Counting + reasoning — write a short justification, not just a number.)**
At a party, 9 people each shake hands with exactly 3 others.

- (a) Is this situation possible? Justify using the Handshake Lemma.
- (b) If instead 10 people each shake hands with exactly 3 others, how many handshakes occur in total? Show the calculation.

---

*When you're done, send me your answers (e.g. "Q1: b, Q5: a,b,d…") and your full written proofs for Q7–Q8, and I'll mark them and log any errors.*
