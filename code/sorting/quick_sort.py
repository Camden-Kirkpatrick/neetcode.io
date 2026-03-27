# Quick Sort
#
# This program demonstrates the Quick Sort algorithm.
#
# Quick sort is a divide-and-conquer sorting algorithm that
# works by selecting a pivot element and partitioning the
# array into two parts:
#
# - elements smaller than the pivot
# - elements greater than or equal to the pivot
#
# Then it recursively sorts those two parts.
#
#
# How Quick Sort Works
#
# 1. Choose a pivot element (in this implementation, the last element).
# 2. Rearrange the array so that:
#    - all elements smaller than the pivot are on the left
#    - all elements greater than or equal to the pivot are on the right
# 3. Place the pivot in its correct sorted position.
# 4. Recursively apply the same process to the left and right subarrays.
#
#
# Example
#
# [7, 4, 12, 1, 3]
#
# Choose pivot = 3
#
# Partition:
#
# [1, 3, 12, 7, 4]
#  ↑
# pivot is now in its correct position
#
# Left side:  [1]
# Right side: [12, 7, 4]
#
#
# Example Walkthrough
#
# Initial array:
#
# [7, 4, 12, 1, 3]
#
#
# First Partition (pivot = 3)
#
# Rearranged:
# [1, 3, 12, 7, 4]
#
# Now:
# pivot index = 1
#
# Left side:  [1]
# Right side: [12, 7, 4]
#
#
# Second Partition (right side, pivot = 4)
#
# [12, 7, 4] → [4, 7, 12]
#
# Now:
# pivot index = 2 (relative to original array)
#
# Left side:  []
# Right side: [7, 12]
#
#
# Continue recursively until all parts are sorted:
#
# Final result:
# [1, 3, 4, 7, 12]
#
#
# Key Idea
#
# Quick sort works by placing one element (the pivot)
# into its correct position each time.
#
# After partitioning:
# - everything to the left is smaller
# - everything to the right is larger
#
# So the pivot never needs to be moved again.
#
#
# Complexity
#
# Best / Average Case:
#
# Each partition splits the array roughly in half.
#
# This results in about log₂(n) levels of recursion.
#
# At each level, multiple partitions may occur, but the total
# number of elements processed across all partitions is at most n.
#
# This is because each element is compared once per level during partitioning.
#
# So the total work per level is O(n).
#
# Total work:
# n × log n
#
# Best Case Time Complexity:    O(n log n)
# Average Case Time Complexity: O(n log n)
#
#
# Worst Case:
#
# If the pivot is always the smallest or largest element
# (for example, already sorted array with bad pivot choice),
# the array becomes very unbalanced:
#
# n levels of recursion
# and each level does n work
#
# Worst Case Time Complexity: O(n²)
#
#
# Space Complexity
#
# Quick sort is an in-place algorithm because it does not
# require additional arrays for sorting.
#
# However, it uses recursion:
#
# - Best case recursion depth:  O(log n)
# - Worst case recursion depth: O(n)
#
# Space Complexity:
#
# Average Case: O(log n)
# Worst Case:   O(n)


def quick_sort(arr, start, end):
    # if start == end -> 1 element -> already sorted
    # if start > end -> there is nothing to the left or right of the pivot -> this side is empty
    if start >= end:
        return

    pivot = arr[end]
    left = start # pointer for left side

    # Partition: elements smaller than pivot on left side
    for i in range(start, end):
        if arr[i] < pivot:
            arr[left], arr[i] = arr[i], arr[left]
            left += 1

    # Move pivot in-between left & right sides (its sorted position)
    arr[end], arr[left] = arr[left], arr[end]
    
    
    # Quick sort left side
    quick_sort(arr, start, left - 1)

    # Quick sort right side
    quick_sort(arr, left + 1, end)



if __name__ == "__main__":
    arr = [7, 4, 12, 1, 3]
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)