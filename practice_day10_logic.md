# FIT1058 — Day 10 Practice · Propositional & Predicate Logic (Ch 4–5)

**Date:** Thu 11 Jun 2026 · 4 days to exam
**Topic:** truth tables & tautologies, logical equivalences (De Morgan, distributive, implication X⇒Y ≡ ¬X∨Y), contrapositive/converse/inverse, Boolean-algebra proofs *without* truth tables, quantifiers & negating quantified statements
**Format:** 5 MCQ (one is select-all) + 2 written questions. Attempt everything by hand before opening the answer key.

> Exam habit: on Boolean-algebra proofs, **name the rule on every line** (Distributive, De Morgan, Complement, Identity…). Naming the law is where the marks are. From your error log: don't confuse **contrapositive** (negate + swap) with **converse** (just swap).

---

## Warm-up (15 min) — 2 counting problems from Day 9 (spaced repetition)

**W1.** How many integers from 1 to 200 inclusive are divisible by **neither** 4 nor 6? (State the principle.)

**W2.** In how many ways can 7 distinct books be arranged on a shelf so that 2 particular books are **never** next to each other?

---

## Main set

**Q1 (Implication — equivalent form).** The statement $P \Rightarrow Q$ is logically equivalent to which of the following?
a) $P \land \neg Q$   b) $\neg P \lor Q$   c) $Q \Rightarrow P$   d) $\neg P \land Q$

**Q2 (Negating an implication).** Which expression is logically equivalent to $\neg(P \Rightarrow Q)$?
a) $\neg P \lor Q$   b) $P \land \neg Q$   c) $\neg P \land \neg Q$   d) $P \Rightarrow \neg Q$

**Q3 (Tautology).** Exactly one of the following is a **tautology** (true for every assignment). Which one?
a) $P \land \neg P$
b) $\big(P \land (P \Rightarrow Q)\big) \Rightarrow Q$
c) $P \Rightarrow (P \land Q)$
d) $(P \lor Q) \Rightarrow P$

**Q4 (Select all that apply).** Which of the following are logically equivalent to $P \Rightarrow Q$?
a) $\neg Q \Rightarrow \neg P$
b) $\neg P \lor Q$
c) $\neg(P \land \neg Q)$
d) $Q \Rightarrow P$
e) $\neg P \Rightarrow \neg Q$

**Q5 (Contrapositive vs converse vs inverse).** Consider the statement: *"If it rains, then the match is cancelled."* Which sentence is its **contrapositive**?
a) If the match is cancelled, then it rained.
b) If it does not rain, then the match is not cancelled.
c) If the match is not cancelled, then it did not rain.
d) If it rains, then the match is not cancelled.

**Q6 (Negating nested quantifiers).** Let $P(x,y)$ be a predicate. Which statement is logically equivalent to $\neg\, \forall x\, \exists y\; P(x,y)$?
a) $\forall x\, \exists y\; \neg P(x,y)$
b) $\exists x\, \forall y\; \neg P(x,y)$
c) $\exists x\, \exists y\; \neg P(x,y)$
d) $\forall x\, \forall y\; \neg P(x,y)$

**Q7 (Written — Boolean-algebra proof, NO truth table).** Prove the logical equivalence
$$\neg\big(P \lor (\neg P \land Q)\big) \;\equiv\; \neg P \land \neg Q.$$
Give one law per line and **name each law** you use (e.g. Distributive, Complement, Identity, De Morgan).

**Q8 (Written — predicate logic + negation).** Let the domain be all people. Define
$S(x)$: "$x$ is a student in FIT1058", and $\text{Solved}(x,y)$: "$x$ has solved problem $y$" (where $y$ ranges over all problems).

(i) Translate into predicate logic: *"Every student in FIT1058 has solved at least one problem."*
(ii) Write the **negation** in predicate logic, pushing $\neg$ all the way inward (no $\neg$ left in front of a quantifier).
(iii) State that negation as a plain-English sentence.

---

*When you're done, reply with your answers (e.g. "Q1 b, Q2 b, …") and I'll mark them and log any slips to `error_log.md`. The answer key is in a separate file — don't peek until you've attempted all 8.*
