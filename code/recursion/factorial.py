# Factorial (Recursive and Iterative)
#
# This program demonstrates two ways to compute the factorial
# of a number:
#
# 1. Recursive solution
# 2. Iterative (non-recursive) solution
#
#
# What is a Factorial?
#
# The factorial of a number n is the product of all positive
# integers from 1 up to n.
#
# Mathematical definition:
#
# n! = n × (n-1) × (n-2) × ... × 2 × 1
#
#
# Example
#
# 5! = 5 × 4 × 3 × 2 × 1 = 120
#
#
# Special Case
#
# By definition:
#
# 0! = 1
# 1! = 1
#
# These values act as the stopping condition in the recursive solution.
#
#
# Recursive Insight
#
# The factorial function can be defined recursively because
# the problem naturally refers to a smaller version of itself.
#
# n! = n × (n-1)!
#
#
# Recursion Stack Example
#
# Suppose we compute:
#
# factorial(5)
#
# The function calls will go deeper until reaching the base case.
#
#
# Going DOWN the call stack
#
# factorial(5)
#   = 5 * factorial(4)
#
# factorial(4)
#   = 4 * factorial(3)
#
# factorial(3)
#   = 3 * factorial(2)
#
# factorial(2)
#   = 2 * factorial(1)
#
# factorial(1)
#   = 1     ← Base case reached
#
#
# Coming BACK UP the call stack
#
# factorial(2)
#   = 2 * 1
#   = 2
#
# factorial(3)
#   = 3 * 2
#   = 6
#
# factorial(4)
#   = 4 * 6
#   = 24
#
# factorial(5)
#   = 5 * 24
#   = 120
#
#
# The recursive calls build a stack of pending multiplications.
# Once the base case returns, the results are computed while
# the stack unwinds.
#
#
# Iterative Insight
#
# The factorial can also be computed using a loop that multiplies
# numbers from n down to 1.
#
#
# Complexity Comparison
#
# Recursive solution
#
# Time Complexity:  O(n)
# Space Complexity: O(n)  (due to recursion call stack)
#
#
# Iterative solution
#
# Time Complexity:  O(n)
# Space Complexity: O(1)


def factorial_rec(n):
    """
    Recursive factorial implementation.

    Uses the mathematical definition:

        n! = n * (n-1)!
    """

    # Base case:
    # If n is 0 or 1, the factorial is 1.
    if n <= 1:
        return 1

    # Recursive case:
    # Multiply n by the factorial of the smaller problem.
    return n * factorial_rec(n - 1)


def factorial(n):
    """
    Iterative factorial implementation.

    Computes the factorial using a loop instead of recursion.
    """

    # Start with result = 1 because multiplying by 1
    # does not change the product.
    result = 1

    # Continue multiplying while n > 1
    while n > 1:
        result *= n
        n -= 1

    return result


if __name__ == "__main__":

    print("Recursive factorial:")
    for i in range(10):
        print(f"{i}! =", factorial_rec(i))

    print("\n")

    print("Non-recursive factorial:")
    for i in range(10):
        print(f"{i}! =", factorial(i))