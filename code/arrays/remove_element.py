# Algorithm that returns the number of elements in an array not equal to value.

# Time Complexity: O(n²)
# - The loop can run up to n times.
# - Each nums.pop(i) operation shifts the remaining elements left (O(n)).
# - In the worst case, many pops occur, resulting in n * n → O(n²).
#
# Space Complexity: O(1)
# - The algorithm modifies the array in-place and does not use extra memory.
def remove_element(nums: list[int], val: int) -> int:
    i = 0
    while i < len(nums):
        # If the value matches the target, remove it.
        # We do NOT increment i because popping shifts the
        # remaining elements left, so a new element moves
        # into index i and must still be checked.
        if nums[i] == val:
            nums.pop(i)
            continue
        i += 1
    print(nums)
    # return the number of elements != to value
    return len(nums)

def remove_element_best(nums: list[int], val: int) -> int:
    """
    Remove all occurrences of a given value from an array in-place
    using the two-pointer technique.

    Algorithm:
    1. Initialize a write pointer `w = 0`, which marks the position
       where the next valid value should be written.
    2. Use a read pointer `r` to scan through the array.
    3. If the current value is NOT equal to `val`, it should remain
       in the array.
    4. Copy that value to index `w` and increment `w`.
    5. Continue scanning until the entire array has been processed.

    Invariant:
    All elements to the left of `w` are valid elements that are not
    equal to `val`.

    Example:
        nums = [10, 23, -87, 10, 38, 56, 10]
        val = 10

        r scans the array:
        [23 | 23 -87 10 38 56 10]  keep 23
        [23 -87 | -87 10 38 56 10] keep -87
        skip 10
        [23 -87 38 | 10 38 56 10]  keep 38
        [23 -87 38 56 | 38 56 10]  keep 56
        skip 10

        Result:
        nums[:4] = [23, -87, 38, 56]

    Returns:
        int: The number of elements not equal to `val`. The first k
        elements of nums contain the valid values.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    w = 0

    for r in range(len(nums)):
        if nums[r] != val:
            nums[w] = nums[r]
            w += 1

    return w



if __name__ == "__main__":
    val = 10
    nums = [10, 23, -87, 10, 38, 56, 10]
    print(remove_element(nums, val))