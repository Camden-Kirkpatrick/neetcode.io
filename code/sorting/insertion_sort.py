# Insertion Sort
#
# This program demonstrates the Insertion Sort algorithm.
#
# Insertion sort is a simple sorting algorithm that builds
# the sorted array one element at a time.
#
#
# How Insertion Sort Works
#
# The array is divided into two conceptual parts:
#
# Sorted portion | Unsorted portion
#
# Initially:
#
# The first element is considered sorted.
#
# Example:
#
# [3, 2, 5, 4, 1]
#
# ^
# sorted
#
#
# At each step:
#
# 1. Take the next element from the unsorted portion.
# 2. Compare it with elements in the sorted portion.
# 3. Move larger elements one position to the right.
# 4. Insert the element into the correct position.
#
#
# Example Walkthrough
#
# Initial array:
#
# [3, 2, 5, 4, 1]
#
#
# Pass 1
#
# i = 1
# Compare 2 with 3
#
# [3, 2, 5, 4, 1]
#  ^
#
# Swap them
#
# [2, 3, 5, 4, 1]
#
#
# Pass 2
#
# i = 2
# Compare 5 with 3
#
# 5 is already larger, so nothing changes.
#
# [2, 3, 5, 4, 1]
#
#
# Pass 3
#
# i = 3
# Compare 4 with 5
#
# [2, 3, 5, 4, 1]
#
# Swap
#
# [2, 3, 4, 5, 1]
#
#
# Pass 4
#
# i = 4
#
# Compare 1 with 5, 4, 3, 2
#
# Shift elements right until the correct spot is found.
#
# [1, 2, 3, 4, 5]
#
#
# Key Idea
#
# Each iteration inserts one element into the correct
# position of the sorted portion of the array.
#
#
# Complexity
#
# Another way to think about the runtime:
#
# The outer loop visits every element in the array once.
#
# For each element, we may need to compare it with every
# previous element in order to find the correct position
# in the sorted portion of the array.
#
# So the work can look like this in the worst case:
#
# element 1 → compare with 1 previous element
# element 2 → compare with 2 previous elements
# element 3 → compare with 3 previous elements
# ...
#
# Because we may scan many previous elements for each
# element in the array, the total work grows roughly like:
#
# n × n
#
# Worst Case Time Complexity: O(n²)
#
#
# Best Case (already sorted)
#
# If the array is already sorted, the inner loop never runs
# because each element is already greater than the one before it.
#
# Each iteration only performs one comparison.
#
# Best Case Time Complexity: O(n)
#
#
# Space Complexity
#
# Insertion sort sorts the array in place and does not allocate
# additional memory.
#
# Space Complexity: O(1)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i - 1

        while j >= 0 and arr[j + 1] < arr[j]:
            temp = arr[j + 1]
            arr[j + 1] = arr[j]
            arr[j] = temp
            j -= 1

    return arr



if __name__ == "__main__":
    arr = [3, 2, 5, 4, 1]
    sorted_arr = insertion_sort(arr)
    print(sorted_arr)