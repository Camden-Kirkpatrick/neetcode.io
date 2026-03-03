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


def remove_duplicates(nums: list[int]) -> int:
    found = []
    i = 0
    while i < len(nums):
        if nums[i] in found:
            nums.pop(i)
            continue
        found.append(nums[i])
        i += 1
    print(nums)
    return len(nums)


# nums must be sorted for the algorithm to work
nums = [1, 2, 2, 3, 4, 5, 6, 7, 7]
# how many unique numbers are in the list?
print(remove_duplicates(nums))
# IndexError occurs
# print(remove_duplicates_incorrect(nums))