# Binary Tree Height (Max Height)
#
# This program demonstrates how to calculate the height
# of a Binary Tree using recursion.
#
# The height of a tree is defined as:
#
#   The number of nodes along the longest path
#   from the root node down to a leaf node.
#
#
# What This Program Does
#
# 1. Defines a TreeNode class
# 2. Builds a Binary Search Tree (BST)
# 3. Recursively calculates the height
# 4. Prints the result
#
#
# How Height is Calculated
#
# We use recursion to explore BOTH subtrees:
#
# 1. Start at the root
#
# 2. Go LEFT until we cannot go any further
#
# 3. When we hit None:
#      return 0
#
# 4. Come back to the previous node
#
# 5. Then explore the RIGHT subtree
#
# 6. Once we know both subtree heights:
#      take the larger one
#      and add 1 for the current node
#
#
# Formula:
#
#   height(node) = 1 + max(height(left), height(right))
#
#
# Base Case
#
# If the node is None (empty subtree):
#   → height = 0
#
#
# Example
#
# Tree:
#
#         4
#       /   \
#      3     6
#     /     / \
#    2     5   7
#
#
# Walkthrough
#
# Start at node 4
#
# We cannot calculate height(4) yet,
# because we first need:
#   - height(3)
#   - height(6)
#
#
# Go LEFT to node 3
#
# We cannot calculate height(3) yet,
# because we first need:
#   - height(2)
#   - height(None)
#
#
# Go LEFT to node 2
#
# We cannot calculate height(2) yet,
# because we first need:
#   - height(None)
#   - height(None)
#
#
# Go LEFT from 2
# That is None
# return 0
#
# Go RIGHT from 2
# That is None
# return 0
#
# Now come back to node 2
#
# height(2) = 1 + max(0, 0) = 1
#
#
# Now come back to node 3
#
# We already know:
#   left height = 1
#
# Now go RIGHT from 3
# That is None
# return 0
#
# So:
# height(3) = 1 + max(1, 0) = 2
#
#
# Now come back to node 4
#
# We already know:
#   left height = 2
#
# Now go RIGHT to node 6
#
# We cannot calculate height(6) yet,
# because we first need:
#   - height(5)
#   - height(7)
#
#
# Go LEFT to node 5
#
# Go LEFT from 5
# That is None
# return 0
#
# Go RIGHT from 5
# That is None
# return 0
#
# Now come back to node 5
#
# height(5) = 1 + max(0, 0) = 1
#
#
# Now come back to node 6
#
# We already know:
#   left height = 1
#
# Now go RIGHT to node 7
#
# Go LEFT from 7
# That is None
# return 0
#
# Go RIGHT from 7
# That is None
# return 0
#
# Now come back to node 7
#
# height(7) = 1 + max(0, 0) = 1
#
#
# Now come back to node 6
#
# height(6) = 1 + max(1, 1) = 2
#
#
# Now come back to node 4
#
# height(4) = 1 + max(2, 2) = 3
#
#
# Final Answer:
#   Height = 3
#
#
# Key Idea
#
# The recursion goes DOWN the tree first.
#
# But a node cannot compute its height until
# the recursive calls return back up.
#
# So height is really calculated on the way BACK UP,
# after both subtrees have been explored.
#
#
# Complexity
#
# Let:
# n = number of nodes
#
# Time Complexity:
#   O(n) → we visit every node once
#
# Space Complexity:
#   O(h) → recursion stack (h = height of tree):
#     O(log n) for a balanced binary tree
#     O(n) for a skewed binary tree


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert_node(root, data):
    if not root:
        return TreeNode(data)
    
    if data > root.data:
        root.right = insert_node(root.right, data)
    elif data < root.data:
        root.left = insert_node(root.left, data)

    return root


def height(root):
    # Base Case:
    # If the node is empty, its height is 0
    if not root:
        return 0
    
    # Recursively compute height of left subtree
    left_height = height(root.left)

    # Recursively compute height of right subtree
    right_height = height(root.right)

    # Return:
    # 1 (current node) + the taller subtree
    return 1 + max(left_height, right_height)



#       4
#     /   \
#    3     6
#   /     / \
#  2     5   7
if __name__ == "__main__":
    root = TreeNode(4)
    insert_node(root, 3)
    insert_node(root, 6)
    insert_node(root, 2)
    insert_node(root, 5)
    insert_node(root, 7)

    tree_height = height(root)
    print("height of the tree:", tree_height)