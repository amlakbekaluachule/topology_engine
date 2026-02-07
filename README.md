# Topology Engine

Topology Engine is a computational playground for basic algebraic topology.  
It models topological spaces, loops, and homotopy using exact algebraic structures rather than numerical simulation.

The project focuses on turning standard definitions from topology into executable objects.

---

## What this project does

TopoPlay allows you to:

- Define simple topological spaces (graphs, surfaces)
- Represent loops as algebraic objects
- Compute homotopy classes via word reduction
- Work with fundamental groups π₁
- Model basic covering spaces
- Experiment with surfaces of arbitrary genus

All reasoning is definition-driven. Every operation corresponds directly to a standard result from topology.

---

## Mathematical model

### Loops and homotopy

A loop based at a point is represented as a word in generators of the fundamental group.

Two loops are homotopic if their reduced words are equal.

γ₁ ≃ γ₂  ⇔  [γ₁] = [γ₂] in π₁

Homotopy is implemented as algebraic word reduction.

---

### Free groups

For a wedge of n circles:

π₁(∨ₙ S¹) ≅ Fₙ

TopoPlay implements:
- generators
- inverses
- concatenation
- reduction by cancellation (gg⁻¹ = e)

Word reduction is deterministic and exact.

---

### Surfaces

An orientable surface of genus g is modeled with generators:

a₁, b₁, …, a_g, b_g

with defining relation:

∏ᵢ [aᵢ, bᵢ] = e

where:

[a, b] = aba⁻¹b⁻¹

This relation is constructed explicitly and used to test null-homotopy.

---

### Fundamental group examples

Circle:
π₁(S¹) ≅ ℤ

Wedge of two circles:
π₁(S¹ ∨ S¹) ≅ F₂

Torus:
π₁(T²) = ⟨a, b | aba⁻¹b⁻¹ = e⟩
