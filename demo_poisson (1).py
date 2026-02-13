"""
demo_poisson.py

Finite Element Solution of Poisson's Equation using FEniCS.

- Δu = f  in Ω
- u = 0   on ∂Ω

Author: Krishna Vedula
"""

from fenics import *
import matplotlib.pyplot as plt

def solve_poisson(mesh_divisions=32):
    """
    Solve Poisson's equation on a unit square domain using FEniCS.

    Parameters
    ----------
    mesh_divisions : int
        Number of mesh subdivisions per axis.

    Returns
    -------
    u : Function
        FEniCS solution function.
    """

    # Create mesh and define function space
    mesh = UnitSquareMesh(mesh_divisions, mesh_divisions)
    V = FunctionSpace(mesh, "P", 1)

    # Define boundary condition: u = 0 on all boundaries
    bc = DirichletBC(V, Constant(0.0), "on_boundary")

    # Define source term f(x,y) = 1
    f = Constant(1.0)

    # Define variational problem
    u = TrialFunction(V)
    v = TestFunction(V)
    a = dot(grad(u), grad(v)) * dx
    L = f * v * dx

    # Compute solution
    u_solution = Function(V)
    solve(a == L, u_solution, bc)

    return u_solution, mesh

def plot_solution(u_solution, mesh):
    """
    Visualize the solution using Matplotlib.

    Parameters
    ----------
    u_solution : Function
        The Poisson equation solution.
    mesh : Mesh
        The mesh on which the solution is computed.
    """

    plt.figure()
    plot(u_solution)
    plt.title("FEM Solution of Poisson's Equation")
    plt.colorbar()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

def main():
    """
    Main function to run the Poisson solver.
    """

    u_solution, mesh = solve_poisson(mesh_divisions=40)
    plot_solution(u_solution, mesh)

if __name__ == "__main__":
    main()
