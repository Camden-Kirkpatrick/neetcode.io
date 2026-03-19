# Merge Sort
#
# This program demonstrates the Merge Sort algorithm.
#
# Merge sort is a divide-and-conquer sorting algorithm that
# repeatedly splits the array into smaller halves, sorts those
# halves, and then merges them back together in sorted order.
#
#
# How Merge Sort Works
#
# The array is divided into smaller and smaller parts until
# each part contains only one element.
#
# A single element is already sorted by itself.
#
# Then:
#
# 1. Split the array into a left half and a right half.
# 2. Recursively sort the left half.
# 3. Recursively sort the right half.
# 4. Merge the two sorted halves back together.
#
#
# Example
#
# [4, 1, 8, 7, 5]
#
# Split into:
#
# [4, 1, 8]    [7, 5]
#
# Then split again until each subarray has one element:
#
# [4] [1] [8] [7] [5]
#
# Then merge back together in sorted order.
#
#
# Example Walkthrough
#
# Initial array:
#
# [4, 1, 8, 7, 5]
#
#
# Split Phase
#
# [4, 1, 8, 7, 5]
# → [4, 1, 8] and [7, 5]
#
# [4, 1, 8]
# → [4, 1] and [8]
#
# [4, 1]
# → [4] and [1]
#
# [7, 5]
# → [7] and [5]
#
# At this point, every subarray has one element,
# so they are all considered sorted.
#
#
# Merge Phase
#
# Merge [4] and [1]
# → [1, 4]
#
# Merge [1, 4] and [8]
# → [1, 4, 8]
#
# Merge [7] and [5]
# → [5, 7]
#
# Merge [1, 4, 8] and [5, 7]
# → [1, 4, 5, 7, 8]
#
#
# Key Idea
#
# Merge sort first breaks the problem into smaller pieces,
# then combines the sorted pieces into one final sorted array.
#
# The important part is that merging two already-sorted halves
# can be done efficiently by comparing the front elements of
# each half.
#
#
# Complexity
#
# Another way to think about the runtime:
#
# Each level of recursion processes every element in the array
# during the merge step.
#
# That means each level does about n total work.
#
# The number of levels depends on how many times the array can
# be split in half, which is about log₂(n).
#
# So the total work is:
#
# n × log n
#
# Worst Case Time Complexity: O(n log n)
#
# Best Case Time Complexity: O(n log n)
#
# Even if the array is already sorted, merge sort still splits
# the array and merges everything back together.
#
#
# Space Complexity
#
# This version of merge sort is not in place because it creates
# temporary left and right subarrays during merging.
#
# Space Complexity: O(n)


def merge(arr, low, mid, high):
    # Create temporary subarrays
    A = arr[low : mid + 1]      # Left half
    B = arr[mid + 1 : high + 1] # Right half

    # Pointers for A, B, and main array
    i = j = 0
    k = low
    m = len(A)
    n = len(B)

    # Merge elements back into arr in sorted order
    while i < m and j < n:
        if A[i] < B[j]:
            arr[k] = A[i]   # Take from left
            i += 1
        else:
            arr[k] = B[j]   # Take from right
            j += 1
        k += 1
        
    # Copy any remaining elements from A
    while i < m:
        arr[k] = A[i]
        i += 1
        k += 1

    # Copy any remaining elements from B
    while j < n:
        arr[k] = B[j]
        j += 1
        k += 1



def merge_sort(arr, low, high):
    # Base case: one element (already sorted)
    if low < high:
        # Find middle index
        mid = (low + high) // 2

        # Recursively sort left half
        merge_sort(arr, low, mid)

        # Recursively sort right half
        merge_sort(arr, mid + 1, high)

        # Merge the two sorted halves
        merge(arr, low, mid, high)



if __name__ == "__main__":
    arr = [4, 1, 8, 7, 5]
    low = 0
    high = len(arr) - 1

    print("Before Sorting:", arr)
    merge_sort(arr, low, high)
    print("After Sorting:", arr)