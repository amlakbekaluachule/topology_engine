# Topology Engine

Topology Engine is a computational playground for algebraic topology.  
It models topological spaces, loops, and homotopy using **exact algebraic structures**, not numerical approximation.

The project translates textbook definitions into executable objects.

---

## What this project does

TopoPlay allows you to:

- Define simple topological spaces (graphs, surfaces)
- Represent loops as algebraic objects
- Compute homotopy classes via word reduction
- Work with fundamental groups \( \pi_1 \)
- Model basic covering spaces
- Experiment with surfaces of arbitrary genus

All reasoning follows standard mathematical definitions.

---

## Mathematical model

### Loops and homotopy

A loop based at a point is represented as a word in generators of the fundamental group.

Two loops are homotopic if their reduced words are equal:

\[
\gamma_1 \simeq \gamma_2 \quad \Longleftrightarrow \quad [\gamma_1] = [\gamma_2] \in \pi_1(X)
\]

Homotopy is implemented as **algebraic word reduction**.

---

### Free groups

For a wedge of \( n \) circles:

\[
\pi_1\!\left(\bigvee_{i=1}^{n} S^1\right) \cong F_n
\]

TopoPlay implements:
- generators
- inverses
- concatenation
- reduction by cancellation

Reduction rule:
\[
g g^{-1} = e
\]

Word reduction is deterministic and exact.

---

### Surfaces

An orientable surface of genus \( g \) is modeled using generators:

\[
a_1, b_1, \dots, a_g, b_g
\]

with defining relation:

\[
\prod_{i=1}^{g} [a_i, b_i] = e
\]

where the commutator is defined by:

\[
[a, b] = a b a^{-1} b^{-1}
\]

This relation is constructed explicitly and used to test null-homotopy.

---

### Fundamental group examples

Circle:
\[
\pi_1(S^1) \cong \mathbb{Z}
\]

Wedge of two circles:
\[
\pi_1(S^1 \vee S^1) \cong F_2
\]

Torus:
\[
\pi_1(T^2) = \langle a, b \mid a b a^{-1} b^{-1} = e \rangle
\]
