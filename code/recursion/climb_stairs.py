# Climbing Stairs (Recursive and Iterative)
#
# This program demonstrates two ways to compute the number of
# distinct ways to climb a staircase:
#
# 1. Recursive solution
# 2. Iterative (non-recursive) solution
#
#
# Problem Description
#
# You are climbing a staircase with n steps.
#
# Each time you can climb either:
#
# 1 step
# or
# 2 steps
#
# The question is:
#
# "How many distinct ways are there to reach the top?"
#
#
# Example
#
# n = 4
#
# Possible ways to climb the staircase:
#
# 1 + 1 + 1 + 1
# 1 + 1 + 2
# 1 + 2 + 1
# 2 + 1 + 1
# 2 + 2
#
# Total = 5 ways
#
#
# Mathematical Insight
#
# To reach step n, the final move must be either:
#
# +1 step from step (n-1)
# +2 steps from step (n-2)
#
# Therefore:
#
# ways(n) = ways(n-1) + ways(n-2)
#
#
# Base Cases
#
# If there is 1 stair:
#
# ways(1) = 1
#
# If there are 2 stairs:
#
# ways(2) = 2
#
#
# Recursive Insight
#
# The staircase problem can be defined recursively because the
# number of ways to reach step n depends on two smaller staircases.
#
# ways(n) = ways(n-1) + ways(n-2)
#
#
# Recursion Stack Example
#
# Suppose we compute:
#
# climb(5)
#
#
# Going DOWN the call stack
#
# climb(5)
#   = climb(4) + climb(3)
#
# climb(4)
#   = climb(3) + climb(2)
#
# climb(3)
#   = climb(2) + climb(1)
#
# Base cases reached:
#
# climb(2) = 2
# climb(1) = 1
#
#
# Coming BACK UP the call stack
#
# climb(3)
#   = 2 + 1
#   = 3
#
# climb(4)
#   = 3 + 2
#   = 5
#
# climb(5)
#   = 5 + 3
#   = 8
#
#
# Notice that some values are recomputed multiple times.
#
# Example:
#
# climb(3) is computed twice
# climb(2) is computed three times
#
# This is why naive recursion becomes slow for larger n.
#
#
# Iterative Insight
#
# Instead of recomputing smaller problems repeatedly, we can build
# the answer from the bottom up.
#
# The key idea is to track the number of ways to reach the previous two steps.
#
# Let:
#
# prev2 = ways(i-2)
# prev1 = ways(i-1)
#
# Using these two values we compute:
#
# current = prev1 + prev2
#
# After computing the next value, we shift forward so that the
# two most recent values are always stored.
#
#
# Iterative Example
#
# Suppose n = 5
#
# Start with the known base cases:
#
# step 1 → 1 way
# step 2 → 2 ways
#
# prev2 = 1
# prev1 = 2
#
#
# Iteration 1 (compute step 3)
#
# current = prev1 + prev2
#         = 2 + 1
#         = 3
#
# Shift values forward:
#
# prev2 = 2
# prev1 = 3
#
#
# Iteration 2 (compute step 4)
#
# current = prev1 + prev2
#         = 3 + 2
#         = 5
#
# Shift values forward:
#
# prev2 = 3
# prev1 = 5
#
#
# Iteration 3 (compute step 5)
#
# current = prev1 + prev2
#         = 5 + 3
#         = 8
#
# Shift values forward:
#
# prev2 = 5
# prev1 = 8
#
#
# Final result
#
# ways(5) = 8
#
#
# Complexity Comparison
#
# Recursive solution
#
# Time Complexity:  O(2^n)
# Space Complexity: O(n)  (recursion stack)
#
#
# Iterative solution
#
# Time Complexity:  O(n)
# Space Complexity: O(1)
#
# Only the last two computed values are stored.


def climb_stairs_rec(n: int) -> int:
    """
    Recursive climbing stairs implementation.

    Uses the recurrence relation:

        ways(n) = ways(n-1) + ways(n-2)
    """

    # Base cases
    # If there are 1 or 2 stairs, the number of ways
    # to climb them equals n.
    if n <= 2:
        return n

    # Recursive case
    # Solve the two smaller subproblems.
    return climb_stairs_rec(n - 1) + climb_stairs_rec(n - 2)


def climb_stairs(n: int) -> int:
    """
    Iterative climbing stairs implementation.

    Builds the solution from the bottom up.
    """

    # Base cases
    if n <= 2:
        return n

    # prev2 represents ways(i-2)
    prev2 = 1

    # prev1 represents ways(i-1)
    prev1 = 2

    # Compute values from step 3 up to step n
    for _ in range(3, n + 1):

        # Compute the number of ways for the current step
        current = prev1 + prev2

        # Shift the window forward
        #
        # prev2 becomes the old prev1
        # prev1 becomes the newly computed value
        prev2 = prev1
        prev1 = current

    # prev1 now holds ways(n)
    return prev1


if __name__ == "__main__":

    print("Recursive Climb Stairs:")
    print(climb_stairs_rec(5))

    print("\nIterative Climb Stairs:")
    print(climb_stairs(5))