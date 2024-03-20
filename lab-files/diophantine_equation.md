# Diophantine Equation Solver

This Python module provides functions to solve Diophantine equations. A Diophantine equation is a polynomial equation, usually in two or more unknowns, such that only the integer solutions are sought or studied.

# Functions

`diophantine(a: int, b: int, c: int) -> tuple[float, float]`

This function solves the Diophantine equation $a*x + b*y = c$ where $a$, $b$, and $c$ are integers. It returns a tuple of two floats representing the solutions $x$ and $y$.

`diophantine_all_soln(a: int, b: int, c: int, n: int = 2) -> None`

This function finds all solutions of the Diophantine equation $a*x + b*y = c$ where $a$, $b$, and $c$ are integers. It prints n solutions to the console. If $n$ is not provided, it defaults to 2.

`extended_gcd(a: int, b: int) -> tuple[int, int, int]`

This function implements the Extended Euclidean Algorithm, which is used to find the greatest common divisor of $a$ and $b$, and to find the coefficients $x$ and $y$ of Bézout's identity, which are integers such that $d = a*x + b*y$. It returns a tuple of three integers representing $d$, $x$, and $y$.

# Usage
    
```python
d, x, y = extended_gcd(10, 6)
print(f"d: {d}, x: {x}, y: {y}")
# Output: d: 2, x: 1, y: -1
```

# Testing

This module includes doctests that can be run to verify its functionality. To run the tests, execute the module as a script:

```python diophantine_equation.py```

The tests are located in the docstrings of the functions. They provide examples of how to use the functions and verify that they produce the expected output.
