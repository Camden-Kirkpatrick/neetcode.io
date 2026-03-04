# Algorithm that returns the number of unique elements from a sorted array.

# This is not the correct way to remove all duplicates.
#
# Example:
# nums = [1, 2, 2, 3]
#
# i = 0 → found = [1]
# i = 1 → found = [1, 2]
#
# Now i = 2, and nums[2] = 2 is already in found,
# so we remove it with nums.pop(2).
#
# The list becomes:
# nums = [1, 2, 3]
#
# The problem:
# The loop was originally created with range(len(nums)),
# where len(nums) was 4 at the start.
# So the loop will still try to go through:
# i = 0, 1, 2, 3
#
# But the list is now shorter (length = 3).
#
# Two issues occur:
# 1) The element that shifts into index 2 (the 3)
#    is never checked properly because the loop
#    automatically moves to i = 3 next.
#
# 2) When i = 3, nums[3] no longer exists,
#    which can cause an IndexError.
#
# The core problem:
# We are modifying the list (removing elements)
# while iterating forward over it using a fixed range.
#
# When elements are removed, the list shrinks and
# elements shift left, but the loop index continues forward,
# causing skipped elements or out-of-bounds access.
def remove_duplicates_incorrect(nums: list[int]) -> int:
    found = []
    for i in range(len(nums)):
        if nums[i] in found:
            nums.pop(i)
            continue
        found.append(nums[i])
    return len(nums)


# Time Complexity: O(n²)
# - The loop runs up to n times.
# - The check 'nums[i] in found' takes O(n) in the worst case.
# - Removing elements with 'nums.pop(i)' can also shift elements (O(n)).
#
# Space Complexity: O(n)
# - The 'found' list stores the unique values encountered.
def remove_duplicates(nums: list[int]) -> int:
    found = []
    i = 0
    while i < len(nums):
        # If the value already exists in 'found', remove it.
        # We do NOT increment i here because popping shifts all
        # elements left, so the next element moves into index i
        # and still needs to be checked.
        if nums[i] in found:
            nums.pop(i)
            continue
        found.append(nums[i])
        i += 1
    print(nums)
    # return the number of unique elements
    return len(nums)

# This is a more efficient algorithm
def remove_duplicates_best(nums):
    """
    Remove duplicates from a sorted array in-place using the two-pointer technique.

    Algorithm:
    1. Assume the first element is always unique.
       Initialize a write pointer 'w = 1', which marks the position where the
    next unique value should be placed.
    2. Use a read pointer 'r' to scan through the array starting at index 1.
    3. If the current value differs from the previous value, it is a new unique element.
    4. Copy that element to index 'w' and increment 'w'.
    5. Continue until the entire array has been scanned.

    Invariant:
    All elements to the left of 'w' are unique and in their correct position.

    Example:
        nums = [1,1,2,3,3]

        r scans the array:
        [1 | 1 2 3 3]  duplicate → skip
        [1 2 | 2 3 3]  new value → copy
        [1 2 3 | 3 3]  new value → copy
        [1 2 3 | 3 3]  duplicate → skip

        Result:
        nums[:3] = [1,2,3]

    Returns:
        int: The number of unique elements (k). The first k elements
        of nums contain the unique values.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    w = 1

    for r in range(1, len(nums)):
        if nums[r] != nums[r-1]:
            nums[w] = nums[r]
            w += 1

    return w


nums = [1, 2, 2, 3, 4, 5, 6, 7, 7]
num_unique_nums = remove_duplicates_best(nums)
print(num_unique_nums)
# IndexError occurs
# print(remove_duplicates_incorrect(nums))