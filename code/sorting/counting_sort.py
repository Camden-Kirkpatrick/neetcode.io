# Counting Sort
#
# This program demonstrates a form of counting sort
# where the values in the array map directly to indices
# in a dynamically sized counting array.
#
# Instead of comparing elements, we count how many times
# each value appears, then reconstruct the sorted array.
#
#
# How This Works
#
# 1. Find the maximum value in the array to determine
#    how many buckets we need.
#
# 2. Create a "counts" array of size (max value + 1),
#    where each index represents a possible value.
#
#    Example:
#    counts[0] -> number of 0s
#    counts[1] -> number of 1s
#    counts[2] -> number of 2s
#    ...
#
# 3. Iterate through the input array and increment the
#    corresponding index in the counts array.
#
# 4. Rebuild the original array by writing each value
#    the number of times it appeared.
#
#
# Example
#
# Input:
# [7, 3, 2, 4, 5, 1, 2, 3]
#
# max = 7
#
# After counting:
# counts = [0, 1, 2, 2, 1, 1, 0, 1]
#
# Rebuilding:
# [1, 2, 2, 3, 3, 4, 5, 7]
#
#
# Key Idea
#
# The value of each element is used as an index into the
# counts array.
#
# This removes the need for comparisons and allows us
# to directly place elements in sorted order.
#
#
# Complexity
#
# Let n = number of elements
# Let k = range of values (max value)
#
# Counting step: O(n)
#
# Rebuild step:
# - loop over all k buckets
# - write each element once (n total writes)
# → O(n + k)
#
# Total Time: O(n + k)
#
# Space Complexity: O(k)
#
#
# Limitation
#
# This approach requires a bucket for every possible value
# from 0 to max(arr).
#
# If the maximum value is very large, the counts array
# becomes very large, even if the input size is small.
#
# Because of this, counting sort is only practical when:
# - values are non-negative integers
# - the range of values is small
#
# In most real-world cases, values are large or widely spread out,
# so this approach is rarely used compared to algorithms like quick sort.


def counting_sort(arr):
    maxx = max(arr)
    counts = [0] * (maxx + 1)

    for x in arr:
        counts[x] += 1

    i = 0
    for c in range(maxx + 1):
        while counts[c] > 0:
            arr[i] = c
            i += 1
            counts[c] -= 1



if __name__ == "__main__":
    arr = [7, 3, 2, 4, 5, 1, 2, 3]
    counting_sort(arr)
    print(arr)