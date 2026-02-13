# Numerical Analysis of Poisson Equation using FEniCS

This repository contains an example implementation of the Finite Element Method (FEM) for solving the Poisson equation on a 2D unit square using **FEniCS**.

## 📌 Problem Statement

We solve the Poisson equation:

\[
-\Delta u = f \quad \text{in} \ \Omega
\]
\[
u = 0 \quad \text{on} \ \partial\Omega
\]

where `f(x, y) = 1` and `Ω` is the unit square.

## 🧠 Approach

- Construct a mesh on the unit square
- Define a function space with Lagrange elements
- Apply Dirichlet boundary conditions
- Solve the variational form using FEniCS
- Visualize the solution using `matplotlib`

## 🚀 Usage

### Requirements

Install dependencies:

```bash
pip install fenics matplotlib
