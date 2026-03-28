# Binary Search
#
# This program demonstrates the binary search algorithm,
# which efficiently finds a target value in a sorted array.
#
# Instead of checking every element, binary search repeatedly
# divides the search space in half.
#
#
# How This Works
#
# 1. Start with two pointers:
#    - low  (start of the array)
#    - high (end of the array)
#
# 2. Find the middle index:
#    mid = (low + high) // 2
#
# 3. Compare the middle value with the target:
#
#    - If target > arr[mid]:
#        search the right half (low = mid + 1)
#
#    - If target < arr[mid]:
#        search the left half (high = mid - 1)
#
#    - If target == arr[mid]:
#        we found the target
#
# 4. Repeat until:
#    - the target is found, or
#    - the search space becomes empty (low > high)
#
#
# Example
#
# Input:
# [1, 4, 7, 13, 16, 22, 39, 40]
#
# target = 39
#
# Step 1:
# low = 0, high = 7
# mid = 3 → arr[3] = 13 → go right
#
# Step 2:
# low = 4, high = 7
# mid = 5 → arr[5] = 22 → go right
#
# Step 3:
# low = 6, high = 7
# mid = 6 → arr[6] = 39 → found
#
#
# Key Idea
#
# Each step cuts the search space in half.
#
# Instead of checking every element (like linear search),
# binary search eliminates half of the remaining elements
# on each iteration.
#
#
# Complexity
#
# Let n = number of elements
#
# Each step reduces the search space:
# n → n/2 → n/4 → n/8 → ...
#
# This continues until only 1 element remains.
#
# Number of steps ≈ log₂(n)
#
# Total Time: O(log n)
#
# Space Complexity: O(1)
#
#
# Limitation
#
# Binary search only works on sorted arrays.
#
# If the array is not sorted, the algorithm will not work correctly.


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    # Continue searching while there is a valid range
    while low <= high:
        mid = (low + high) // 2  # middle index

        # If target is greater, ignore left half
        if target > arr[mid]:
            low = mid + 1

        # If target is smaller, ignore right half
        elif target < arr[mid]:
            high = mid - 1

        # Target found
        else:
            return mid
        
    # Target not found
    return -1


if __name__ == "__main__":
    arr = [1, 4, 7, 13, 16, 22, 39, 40]
    target = 39
    index = binary_search(arr, target)

    if index != -1:
        print(f"{target} found at index {index}")
    else:
        print(f"{target} not found")