# Guess Number (Binary Search with API)
#
# This program demonstrates how to use binary search to find
# a hidden number within a given range using a provided API.
#
# The API function:
#   guess(num)
#
# returns:
#   -1 if num is higher than the picked number
#    1 if num is lower than the picked number
#    0 if num is exactly the picked number
#
#
# How This Works
#
# 1. Start with a search range:
#    low = start of range
#    high = end of range
#
# 2. Find the middle value:
#    mid = (low + high) // 2
#
# 3. Call the guess API:
#    result = guess(mid)
#
# 4. Use the result to adjust the search range:
#
#    - If result == 1:
#        mid is too low → search right half (low = mid + 1)
#
#    - If result == -1:
#        mid is too high → search left half (high = mid - 1)
#
#    - If result == 0:
#        we found the number
#
# 5. Repeat until:
#    - the number is found, or
#    - the search space becomes empty (low > high)
#
#
# Example
#
# Suppose the secret number is 10
#
# Range: 1 to 100
#
# Step 1:
# low = 1, high = 100
# mid = 50 → too high → go left
#
# Step 2:
# low = 1, high = 49
# mid = 25 → too high → go left
#
# Step 3:
# low = 1, high = 24
# mid = 12 → too high → go left
#
# Step 4:
# low = 1, high = 11
# mid = 6 → too low → go right
#
# Step 5:
# low = 7, high = 11
# mid = 9 → too low → go right
#
# Step 6:
# low = 10, high = 11
# mid = 10 → found
#
#
# Key Idea
#
# We cannot see the actual number directly.
# Instead, we use feedback from the API to eliminate
# half of the remaining possibilities each step.
#
#
# Complexity
#
# Let n = size of the range
#
# Each step cuts the search space in half:
# n → n/2 → n/4 → n/8 → ...
#
# Total Time: O(log n)
#
# Space Complexity: O(1)
#
#
# Limitation
#
# This approach requires the ability to compare guesses
# through the provided API. Without it, we cannot determine
# which direction to search.

def guess_number(low, high) -> int:
    while low <= high:
        mid = (low + high) // 2
        result = guess(mid)

        if result == 1:
            high = mid - 1
        elif result == -1:
            low = mid + 1
        else:
            return mid
    return -1


def guess(n):
    if n > 10:
        return 1
    elif n < 10:
        return -1
    else:
        return 10 # 10 is the number being searched for
    

print(f"Is the secret number in the range? ", end="")
print(f"{'Yes' if guess_number(0, 100) == 10 else 'No'}")