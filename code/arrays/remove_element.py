def remove_element(nums: list[int], val: int) -> int:
    i = 0
    while i < len(nums):
        if nums[i] == val:
            nums.pop(i)
            continue
        i += 1
    print(nums)
    # return the number of elements != to value
    return len(nums)


val = 10
nums = [10, 23, -87, 10, 38, 56, 10]
print(remove_element(nums, val))