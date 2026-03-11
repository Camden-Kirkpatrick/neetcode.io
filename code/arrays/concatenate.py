# Algorithm that concatenates a copy of an array to itself.

# Time Complexity: O(n)   # iterate through nums once
# Space Complexity: O(n)  # new array of size 2n
def get_concatenation(nums: list[int]) -> list[int]:
    n = len(nums)
    new_nums = [0] * (2 * n)

    for i, x in enumerate(nums):
        new_nums[i] = x
        new_nums[i + n] = x
    
    return new_nums



if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    new_nums = get_concatenation(nums)
    # [1, 2, 3, 4, 1, 2, 3, 4]
    print(new_nums)