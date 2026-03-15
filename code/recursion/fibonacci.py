# Fibonacci (Recursive and Iterative)
#
# This program demonstrates two ways to compute Fibonacci numbers:
#
# 1. Recursive solution
# 2. Iterative (non-recursive) solution
#
#
# What is the Fibonacci Sequence?
#
# The Fibonacci sequence is a sequence of numbers where each number
# is the sum of the two previous numbers.
#
# Mathematical definition:
#
# fib(n) = fib(n-1) + fib(n-2)
#
#
# Starting values
#
# fib(0) = 0
# fib(1) = 1
#
#
# Example sequence
#
# n:      0  1  2  3  4  5  6
# fib(n): 0, 1, 1, 2, 3, 5, 8
#
#
# Recursive Insight
#
# The Fibonacci sequence can be defined recursively because each
# value depends on two smaller Fibonacci values.
#
# fib(n) = fib(n-1) + fib(n-2)
#
#
# Recursion Stack Example
#
# Suppose we compute:
#
# fib(5)
#
# The recursion expands like this:
#
#
# Going DOWN the call stack
#
# fib(5)
#   = fib(4) + fib(3)
#
# fib(4)
#   = fib(3) + fib(2)
#
# fib(3)
#   = fib(2) + fib(1)
#
# fib(2)
#   = fib(1) + fib(0)
#
# Base cases reached:
#
# fib(1) = 1
# fib(0) = 0
#
#
# Coming BACK UP the call stack
#
# fib(2)
#   = 1 + 0
#   = 1
#
# fib(3)
#   = 1 + 1
#   = 2
#
# fib(4)
#   = 2 + 1
#   = 3
#
# fib(5)
#   = 3 + 2
#   = 5
#
#
# Notice that some values are recomputed multiple times.
#
# Example:
#
# fib(3) is computed twice.
# fib(2) is computed three times.
#
# This is why naive recursive Fibonacci becomes slow for larger n.
#
#
# Iterative Insight
#
# Instead of recomputing Fibonacci numbers, we can build the
# sequence from the bottom up using a loop.
#
# The key idea is to track two consecutive Fibonacci numbers.
#
# Example:
#
# prev = fib(i)
# cur  = fib(i+1)
#
# From these two values we can compute the next Fibonacci number.
#
# next = prev + cur
#
# Then we shift forward in the sequence.
#
#
# Complexity Comparison
#
# Recursive solution
#
# Time Complexity:  O(2^n)
# Space Complexity: O(n)  (due to recursion stack)
#
#
# Iterative solution
#
# Time Complexity:  O(n)
# Space Complexity: O(1)


def fib_rec(n):
    """
    Recursive Fibonacci implementation.

    Uses the definition:

        fib(n) = fib(n-1) + fib(n-2)
    """

    # Base cases:
    # fib(0) = 0
    # fib(1) = 1
    if n <= 1:
        return n

    # Recursive case:
    # Compute Fibonacci numbers for the two smaller subproblems.
    return fib_rec(n - 1) + fib_rec(n - 2)


def fib(n):
    """
    Iterative Fibonacci implementation.

    Builds the sequence from the bottom up using a loop.
    """

    # Start with the first two Fibonacci numbers.
    prev = 0   # fib(0)
    cur = 1    # fib(1)

    # Temporary variable used to compute the next Fibonacci number.
    next = 0

    # Each iteration moves one step forward in the sequence.
    for _ in range(n):

        # Compute the next Fibonacci number.
        # next = fib(i+2)
        next = cur + prev

        # Shift the values forward.
        #
        # prev becomes the previous cur
        # cur becomes the newly computed Fibonacci number
        prev = cur
        cur = next

    # After n iterations, prev holds fib(n)
    return prev


if __name__ == "__main__":

    print("Recursive Fibonacci:")
    for i in range(10):
        print(fib_rec(i), end=" ")

    print("\n")

    print("Iterative Fibonacci:")
    for i in range(5):
        print(fib(i), end=" ")