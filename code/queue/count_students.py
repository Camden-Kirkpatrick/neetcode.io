# Number of Students Unable to Eat Lunch
#
# This program solves the "Number of Students Unable to Eat Lunch" problem.
#
# Students are standing in a queue waiting to take sandwiches from a stack.
#
# Each student prefers one type of sandwich:
#
# 0 -> circular sandwich
# 1 -> square sandwich
#
# Sandwiches are stacked in a specific order. Only the sandwich on
# top of the stack can be taken.
#
#
# Rules of the Process
#
# 1. The student at the front of the queue looks at the top sandwich.
#
# 2. If the student prefers that sandwich:
#
#       - the student takes the sandwich
#       - the student leaves the queue
#       - the sandwich is removed from the stack
#
# 3. If the student does NOT want that sandwich:
#
#       - the student goes to the back of the queue
#
#
# Example
#
# students   = [1, 0, 0, 1]
# sandwiches = [0, 1, 0, 1]
#
# Queue:
#
# front -> [1,0,0,1]
#
# Top sandwich = 0
#
# Student 1 refuses -> moves to back
#
# [0,0,1,1]
#
# Student 0 eats the sandwich
#
# [0,1,1]
#
#
# When Does the Process Stop?
#
# The process stops when the sandwich on top cannot be eaten by
# ANY remaining student.
#
# Example:
#
# students   = [1,1,1]
# sandwiches = [0]
#
# All students refuse the sandwich:
#
# [1,1,1] -> [1,1,1] -> [1,1,1]
#
# The queue will rotate forever.
#
# At this point we stop the process and the remaining students
# cannot eat.
#
#
# Two Approaches
#
# This file demonstrates two solutions:
#
# 1. Simulation using a queue (deque)
# 2. Optimal counting solution
#
#
# Simulation Solution
#
# This solution directly simulates the student queue.
#
# Data structure used:
#
# deque
#
# because it allows efficient queue operations:
#
# popleft() -> remove front student
# append()  -> send student to back
#
# We track how many students have refused the current sandwich.
#
# If every student refuses once, the process stops.
#
#
# Optimal Insight
#
# The key observation is that students NEVER change their sandwich
# preference.
#
# Rotating the queue does not change how many students want each
# sandwich type.
#
# Therefore the ORDER of students does not matter.
#
# Only the COUNTS matter.
#
#
# Instead of simulating the queue, we count how many students want
# each sandwich type.
#
# If the top sandwich has no students who want it, the process
# stops immediately.
#
#
# Complexity Comparison
#
# Simulation solution
#
# Time Complexity:  O(n)
# Space Complexity: O(n)
#
#
# Optimal counting solution
#
# Time Complexity:  O(n)
# Space Complexity: O(1)

from collections import deque


def count_students_simulation(students, sandwiches):
    """
    Simulation solution using a queue.

    We rotate students until someone eats the sandwich
    or everyone refuses the current sandwich.
    """

    # Convert the student list into a deque so we can efficiently
    # remove from the front and append to the back.
    students = deque(students)

    # i tracks the current sandwich on the stack (top of the stack)
    i = 0

    # refusals counts how many students in a row refused the
    # current sandwich.
    refusals = 0

    # Continue while:
    # 1. there are still students
    # 2. not every student has refused the current sandwich
    while students and refusals < len(students):

        # Check if the student at the front wants the top sandwich
        if students[0] == sandwiches[i]:

            # Student takes the sandwich and leaves the line
            students.popleft()

            # Move to the next sandwich in the stack
            i += 1

            # Reset refusals because the situation changed
            # (a sandwich was eaten and the queue changed)
            refusals = 0

        else:
            # Student refuses the sandwich.
            # Move the student from the front of the queue to the back.
            students.append(students.popleft())

            # Record that one more student refused this sandwich
            refusals += 1

    # Remaining students in the queue could not eat
    return len(students)


def count_students_optimal(students, sandwiches):
    """
    Optimal solution using counting instead of simulation.

    Since students never change their preference, the queue
    order is irrelevant. Only the number of students who want
    each sandwich type matters.
    """

    # count[0] = number of students who want circular sandwiches
    # count[1] = number of students who want square sandwiches
    count = [0, 0]

    # Count how many students want each sandwich type
    for s in students:
        count[s] += 1

    # Process sandwiches from top to bottom
    for s in sandwiches:

        # If no student wants this sandwich type,
        # the process stops immediately.
        if count[s] == 0:
            break

        # One student eats this sandwich
        count[s] -= 1

    # Remaining students are those who could not eat
    return count[0] + count[1]


if __name__ == "__main__":

    students = [1, 0, 0, 1, 1]
    sandwiches = [1, 0, 0, 0, 0]

    # Run both solutions to show they produce the same result
    print("Simulation solution:", count_students_simulation(students, sandwiches))
    print("Optimal solution:", count_students_optimal(students, sandwiches))