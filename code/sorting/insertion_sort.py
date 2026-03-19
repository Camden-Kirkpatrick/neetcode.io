# Insertion Sort
#
# This program demonstrates the Insertion Sort algorithm.
#
# Insertion sort builds a sorted portion of the array one
# element at a time by inserting each element into its
# correct position.
#
#
# How Insertion Sort Works
#
# The algorithm divides the array into two parts:
#
# 1. A sorted portion (left side)
# 2. An unsorted portion (right side)
#
# It repeatedly takes the next element from the unsorted
# portion and inserts it into the correct position in
# the sorted portion.
#
#
# Example
#
# [3, 2, 5, 4, 1]
#
# Step-by-step:
#
# Start:
# [3 | 2, 5, 4, 1]
#
# Insert 2 into sorted portion:
# [2, 3 | 5, 4, 1]
#
# Insert 5:
# [2, 3, 5 | 4, 1]
#
# Insert 4:
# [2, 3, 4, 5 | 1]
#
# Insert 1:
# [1, 2, 3, 4, 5]
#
#
# Key Idea
#
# Take the current element and shift larger elements
# in the sorted portion to the right to make space,
# then insert the element into the correct position.
#
#
# Complexity
#
# Another way to think about the runtime:
#
# For each element, we may need to compare it with all
# previous elements in the sorted portion.
#
# Example of maximum work:
#
# i = 1  -> compare with 1 element
# i = 2  -> compare with 2 elements
# i = 3  -> compare with 3 elements
# ...
# i = n-1 -> compare with n-1 elements
#
# Total work:
#
# 1 + 2 + 3 + ... + (n - 1)
#
# This equals:
#
# n(n - 1) / 2
#
# Worst Case Time Complexity: O(n^2)
#
# Best Case Time Complexity: O(n)
# (when the array is already sorted, no shifting occurs)
#
#
# Space Complexity
#
# Insertion sort is in-place and uses no extra memory.
#
# Space Complexity: O(1)


def insertion_sort(arr):
    # Traverse from the second element to the end
    for i in range(1, len(arr)):

        # Start comparing with the previous element
        j = i - 1

        # Store the current value to insert
        x = arr[i]

        # Shift elements greater than x to the right
        while j >= 0 and arr[j] > x:
            arr[j + 1] = arr[j]  # shift right
            j -= 1               # move left

        # Insert x into its correct position
        arr[j + 1] = x



if __name__ == "__main__":
    arr = []
    for i in range(10000):
        arr.append(i)

    arr.sort(reverse=True)

    insertion_sort(arr)
    print(arr)