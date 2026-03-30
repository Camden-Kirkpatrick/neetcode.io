# Search Matrix (Binary Search on 2D Matrix)
#
# This program demonstrates how to perform binary search
# on a 2D matrix that is sorted in a specific way:
#
# - Each row is sorted
# - The first element of each row is greater than the last
#   element of the previous row
#
# Because of this, the matrix can be treated like a single
# sorted 1D array.
#
#
# How This Works
#
# 1. Treat the matrix as a flattened array:
#    total elements = rows * cols
#
# 2. Use binary search over index range:
#    left = 0
#    right = rows * cols - 1
#
# 3. Find the middle index:
#    mid = (left + right) // 2
#
# 4. Convert the 1D index into 2D coordinates:
#
#    - row = mid // cols   → which row
#    - col = mid % cols    → position in that row
#
# 5. Compare matrix[row][col] with target:
#
#    - If target > value:
#        search right half (left = mid + 1)
#
#    - If target < value:
#        search left half (right = mid - 1)
#
#    - If equal:
#        target found
#
# 6. Repeat until:
#    - target is found, or
#    - search space is empty (left > right)
#
#
# Example
#
# Input:
# [
#   [3, 5, 8, 9],
#   [12, 15, 21, 27],
#   [34, 39, 45, 48]
# ]
#
# target = 8
#
# Step 1:
# left = 0, right = 11
# mid = 5 → matrix[1][1] = 15 → go left
#
# Step 2:
# left = 0, right = 4
# mid = 2 → matrix[0][2] = 8 → found
#
#
# Key Idea
#
# We perform binary search on indices instead of rows/columns,
# and map each index back to the matrix using division and modulo.
#
# This avoids flattening the matrix and keeps the search efficient.
#
#
# Complexity
#
# Let m = number of rows
# Let n = number of columns
#
# Total elements = m * n
#
# Each step cuts the search space in half:
# m*n → (m*n)/2 → (m*n)/4 → ...
#
# Total Time: O(log(m * n))
#
# Space Complexity: O(1)
#
#
# Limitation
#
# This only works if:
# - each row is sorted, and
# - rows do not overlap in values
#   (last element of one row < first element of next row)


def search_matrix(matrix, target):
    rows, cols = len(matrix), len(matrix[0])
    l, r = 0, rows * cols - 1

    while l <= r:
        m = (l + r) // 2
        row, col = m // cols, m % cols
        if target > matrix[row][col]:
            l = m + 1
        elif target < matrix[row][col]:
            r = m - 1
        else:
            return True
    
    return False


matrix = [
    [3, 5, 8, 9],
    [12, 15, 21, 27],
    [34, 39, 45, 48]
]
target = 8

print(f"Is {target} in the matrix? ", end="")
print(f"{'Yes' if search_matrix(matrix, target) else 'No'}")