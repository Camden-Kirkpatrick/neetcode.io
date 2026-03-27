# Bucket Sort (Counting Sort for Small Known Range)
#
# This program demonstrates a simple form of bucket sort,
# where the values in the array directly map to indices
# in a separate counting array.
#
# Instead of comparing elements, we count how many times
# each value appears, then reconstruct the sorted array.
#
#
# How This Works
#
# 1. Create a "counts" array where each index represents
#    a possible value in the input.
#
#    Example:
#    counts[0] -> number of 0s
#    counts[1] -> number of 1s
#    counts[2] -> number of 2s
#
# 2. Iterate through the input array and increment the
#    corresponding index in the counts array.
#
# 3. Rebuild the original array by writing each value
#    the number of times it appeared.
#
#
# Example
#
# Input:
# [2, 1, 1, 0, 2]
#
# After counting:
# counts = [1, 2, 2]
#
# Rebuilding:
# [0, 1, 1, 2, 2]
#
#
# Key Idea
#
# The value of each element is used as an index into the
# counts array.
#
# This only works when:
# - values are integers
# - values are small and within a known range
#
# So instead of comparing elements like quick sort,
# we directly place them based on their value.
#
#
# Complexity
#
# Let n = number of elements
# Let k = number of possible values (number of buckets)
#
# Counting step:   O(n)
#
# Rebuild step:
# - we loop over all k buckets
# - we write each element once (n total writes)
# → O(n + k)
#
# Total Time:      O(n + k)
#
# In this implementation:
# k = 3 (constant)
# → Total Time simplifies to O(n)
# → Space Complexity is O(1)
#
#
# Limitation
#
# This approach relies on using values as indices (or mapping values to buckets).
#
# That means we need a bucket for every possible value in the range.
#
# If the range of values is large (for example, values up to 1,000,000),
# we would need a very large counts array, even if the input only has a few elements.
#
# This makes the algorithm inefficient in terms of memory.
#
# Because of this, bucket/counting sort is only practical when:
# - the range of values is small
# - and reasonably close to the number of elements
#
# In most real-world cases, values can be large or widely spread out,
# so this approach is rarely used compared to algorithms like quick sort.


def bucket_sort(arr):
    # Assuming arr only contains 0, 1 or 2
    counts = [0, 0, 0]

    # Count the quantity of each val in arr
    for n in arr:
        counts[n] += 1
    
    # Fill each bucket in the original array
    i = 0
    for n in range(len(counts)):
        for j in range(counts[n]):
            arr[i] = n
            i += 1



if __name__ == "__main__":
    arr = [2, 1, 1, 0, 2, 1, 2, 2, 0, 0, 1]
    bucket_sort(arr)
    print(arr)