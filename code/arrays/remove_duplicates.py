def remove_duplicates(nums: list[int]) -> int:
    found = []
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] in found:
            nums.pop(i)
            continue
        found.append(nums[i])
    print(nums)
    return len(nums)



nums = [1, 2, 2, 3, 3, 4, 5, 6, 7, 8, 9, 9]
print(remove_duplicates(nums))
