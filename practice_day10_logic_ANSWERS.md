# FIT1058 — Day 10 ANSWER KEY · Propositional & Predicate Logic

*Don't open until you've attempted all questions in `practice_day10_logic.md`.*

---

## Warm-up

**W1.** Inclusion–Exclusion. ⌊200/4⌋ = 50 divisible by 4; ⌊200/6⌋ = 33 divisible by 6; lcm(4,6) = 12, ⌊200/12⌋ = 16 divisible by both. Divisible by 4 **or** 6 = 50 + 33 − 16 = 67. Divisible by **neither** = 200 − 67 = **133**.

**W2.** Total arrangements 7! = 5040. Treat the 2 books as a block: 6! × 2 = 720 × 2 = 1440 with them together. Never adjacent = 5040 − 1440 = **3600**.

---

## Main set

**Q1 — b)** $\neg P \lor Q$. (Definition of implication. (a) is $\neg(P\Rightarrow Q)$; (c) is the converse.)

**Q2 — b)** $P \land \neg Q$. ($\neg(P\Rightarrow Q) = \neg(\neg P \lor Q) = P \land \neg Q$ by De Morgan.)

**Q3 — b)** $\big(P \land (P \Rightarrow Q)\big) \Rightarrow Q$ — this is **modus ponens**, always true. (a) is a contradiction; (c) fails when P=T, Q=F; (d) fails when P=F, Q=T.

**Q4 — a, b, c.**
- a) contrapositive — equivalent ✓
- b) definition of implication ✓
- c) $\neg(P \land \neg Q) = \neg P \lor Q$ by De Morgan ✓
- d) converse — **not** equivalent ✗
- e) inverse — **not** equivalent ✗

**Q5 — c)** "If the match is not cancelled, then it did not rain." Contrapositive of $P\Rightarrow Q$ is $\neg Q \Rightarrow \neg P$: negate both and swap. (a) = converse, (b) = inverse.

**Q6 — b)** $\exists x\, \forall y\; \neg P(x,y)$. Negation flips each quantifier ($\forall\to\exists$, $\exists\to\forall$) and negates the predicate: $\neg\forall x\,\exists y\,P = \exists x\,\neg\exists y\,P = \exists x\,\forall y\,\neg P$.

**Q7 — model proof (name each law):**
$$
\begin{aligned}
\neg\big(P \lor (\neg P \land Q)\big)
&= \neg\big((P \lor \neg P) \land (P \lor Q)\big) && \text{Distributive} \\
&= \neg\big(T \land (P \lor Q)\big) && \text{Complement } (P \lor \neg P = T)\\
&= \neg(P \lor Q) && \text{Identity } (T \land X = X)\\
&= \neg P \land \neg Q && \text{De Morgan} \qquad\blacksquare
\end{aligned}
$$
*(Alternative: absorption-style — $P \lor (\neg P \land Q) = P \lor Q$ directly by the "absorption/distributive" identity, then De Morgan. Either is fine as long as each step is named.)*

**Q8 — model answer:**

(i) $\forall x\,\big(S(x) \Rightarrow \exists y\; \text{Solved}(x,y)\big)$

(ii) Negation, pushed inward:
$$
\neg\,\forall x\,\big(S(x) \Rightarrow \exists y\,\text{Solved}(x,y)\big)
= \exists x\,\neg\big(S(x) \Rightarrow \exists y\,\text{Solved}(x,y)\big)
= \exists x\,\big(S(x) \land \neg\exists y\,\text{Solved}(x,y)\big)
= \exists x\,\big(S(x) \land \forall y\,\neg\text{Solved}(x,y)\big).
$$
Key moves: $\neg\forall \to \exists\neg$; then $\neg(A\Rightarrow B) = A \land \neg B$; then $\neg\exists y \to \forall y\,\neg$.

(iii) Plain English: **"There is a student in FIT1058 who has not solved any problem"** (i.e. some FIT1058 student has solved no problem at all).

---

### Marking guide
- /8 on the MCQs (Q4 all-or-nothing: a, b, c).
- Q7: 1 mark per correctly named law (4 laws). Losing marks here = revise the law names, not the algebra.
- Q8: 1 mark translation, 2 marks negation (each quantifier flip + the $A\land\neg B$ step), 1 mark English. Watch the implication→conjunction step — that's the classic slip.
