# Binary Search Tree (BST) Search
#
# This program demonstrates how to search for a value
# in a Binary Search Tree using recursion.
#
# A Binary Search Tree (BST) has the property:
#
#   For every node:
#     - all values in the left subtree are smaller
#     - all values in the right subtree are larger
#
#
# What This Program Does
#
# 1. Defines a TreeNode class
# 2. Builds a BST manually
# 3. Searches for a target value using recursion
# 4. Returns True if found, False otherwise
#
#
# How Search Works
#
# To search for a value:
#
# 1. Start at the root
#
# 2. Compare the target with the current node:
#
#    - If target == current node:
#        FOUND → return True
#
#    - If target < current node:
#        go LEFT
#
#    - If target > current node:
#        go RIGHT
#
# 3. Repeat until:
#    - you find the value → return True
#    - or you reach None → return False
#
#
# Important Idea
#
# We eliminate half of the tree at each step.
#
# Because of the BST property:
#   - If target is smaller, it CANNOT be on the right
#   - If target is larger, it CANNOT be on the left
#
# This is similar to binary search on an array.
#
#
# Example
#
# Tree:
#
#         10
#       /    \
#     8        13
#   /   \     /   \
# 4       9  11    17
#               \
#                12
#
#
# Search: 12
#
# Step 1:
# Start at 10
# 12 > 10 → go RIGHT
#
# Step 2:
# At 13
# 12 < 13 → go LEFT
#
# Step 3:
# At 11
# 12 > 11 → go RIGHT
#
# Step 4:
# At 12
# 12 == 12 → FOUND → return True
#
#
# Example (not found):
#
# Search: 15
#
# Step 1:
# Start at 10 → go RIGHT
# Step 2:
# At 13 → go RIGHT
# Step 3:
# At 17 → go LEFT
# Step 4:
# None → NOT FOUND → return False
#
#
# Key Idea
#
# Each recursive call moves us down one level in the tree.
#
# If we reach None:
#   → the value does not exist in the tree
#
#
# Complexity
#
# Let:
# n = number of nodes
#
# Best Case (balanced tree):
#   O(log n)
#
# Worst Case (skewed tree):
#   O(n)
#
# Space Complexity:
#   O(h), where h = height of tree (recursion stack)


class TreeNode:
    def __init__(self, data):
        # Store the value in the node
        self.data = data

        # Left and right children start as empty
        self.left = None
        self.right = None


def search_tree(root, target):
    # Base Case:
    # If we reach None, the value is not in the tree
    if not root:
        return False
    
    # If target is greater, search the right subtree
    if target > root.data:
        return search_tree(root.right, target)

    # If target is smaller, search the left subtree
    elif target < root.data:
        return search_tree(root.left, target)

    # Otherwise, we found the value
    else:
        return True


#         10
#       /    \
#     8        13
#   /   \     /   \
# 4       9  11    17
#               \
#                12
if __name__ == "__main__":

    # Build the same BST as insert_binary_tree
    root = TreeNode(10)

    n1 = TreeNode(8)
    root.left = n1

    n2 = TreeNode(13)
    root.right = n2

    n3 = TreeNode(4)
    n1.left = n3

    n5 = TreeNode(9)
    n1.right = n5

    n4 = TreeNode(11)
    n2.left = n4

    n6 = TreeNode(17)
    n2.right = n6

    # Insert 12 to match final tree
    n7 = TreeNode(12)
    n4.right = n7


    # Search for a value
    target = 12

    result = search_tree(root, target)

    print(f"{target} was {'found' if result else 'not found'}")