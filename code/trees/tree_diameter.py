# Binary Tree Diameter
#
# This program demonstrates how to calculate the diameter
# of a Binary Tree using recursion.
#
# The diameter of a tree is defined as:
#
#   The number of edges on the longest path
#   between ANY two nodes in the tree.
#
# IMPORTANT:
#   The longest path does NOT have to pass through the root.
#
#
# What This Program Does
#
# 1. Defines a TreeNode class
# 2. Builds a Binary Search Tree (BST)
# 3. Recursively calculates the diameter
# 4. Prints the result
#
#
# Key Idea
#
# At every node, we consider:
#
#   "What is the longest path that passes THROUGH this node?"
#
# That path would be:
#
#   left subtree height + right subtree height
#
#
# Why does this work?
#
# If you pick any node:
#
#   - The longest path going through it must go:
#         down the LEFT side
#         then through the node
#         then down the RIGHT side
#
# So the total length is:
#
#   height(left) + height(right)
#
#
# We compute this value at EVERY node,
# and keep track of the largest one we see.
#
#
# Why largest_diameter[0]?
#
# Python integers are immutable.
#
# That means if we try to update a variable inside
# a nested function, it creates a NEW local variable,
# instead of modifying the outer one.
#
# To get around this, we use a list:
#
#   largest_diameter = [0]
#
# Lists are mutable, so:
#
#   largest_diameter[0] = ...
#
# actually updates the same object across all recursive calls.
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
# We cannot compute diameter yet,
# because we first need:
#   - height(3)
#   - height(6)
#
#
# Go LEFT to node 3
#
# We cannot compute diameter(3) yet,
# because we need:
#   - height(2)
#   - height(None)
#
#
# Go LEFT to node 2
#
# Go LEFT → None → return 0
# Go RIGHT → None → return 0
#
# Now at node 2:
#
# left_height = 0
# right_height = 0
#
# diameter through 2 = 0 + 0 = 0
#
# largest_diameter = max(0, 0) = 0
#
# height(2) = 1 + max(0, 0) = 1
#
#
# Back to node 3
#
# left_height = 1
#
# Go RIGHT → None → return 0
#
# diameter through 3 = 1 + 0 = 1
#
# largest_diameter = max(0, 1) = 1
#
# height(3) = 1 + max(1, 0) = 2
#
#
# Back to node 4
#
# left_height = 2
#
# Go RIGHT to node 6
#
#
# Go LEFT to node 5
#
# Go LEFT → None → return 0
# Go RIGHT → None → return 0
#
# diameter through 5 = 0 + 0 = 0
# largest_diameter stays 1
#
# height(5) = 1
#
#
# Back to node 6
#
# left_height = 1
#
# Go RIGHT to node 7
#
# Go LEFT → None → return 0
# Go RIGHT → None → return 0
#
# diameter through 7 = 0 + 0 = 0
# largest_diameter stays 1
#
# height(7) = 1
#
#
# Back to node 6
#
# right_height = 1
#
# diameter through 6 = 1 + 1 = 2
#
# largest_diameter = max(1, 2) = 2
#
# height(6) = 1 + max(1, 1) = 2
#
#
# Back to node 4
#
# right_height = 2
#
# diameter through 4 = 2 + 2 = 4
#
# largest_diameter = max(2, 4) = 4
#
#
# Final Answer:
#   Diameter = 4
#
#
# Key Insight
#
# Just like height:
#   recursion goes DOWN first
#
# But:
#   diameter is calculated on the way BACK UP
#
# because we need both subtree heights first.
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
#   O(h) → recursion stack
#     O(log n) for balanced trees
#     O(n) for skewed trees


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


def binary_tree_diameter(root):
    # Store the maximum diameter found so far
    # Use a list so it can be modified inside nested function
    largest_diameter = [0]

    def height(root):
        # Base Case:
        # Empty node has height 0
        if not root:
            return 0
        
        # Compute left subtree height
        left_height = height(root.left)

        # Compute right subtree height
        right_height = height(root.right)

        # Diameter passing THROUGH this node
        diameter = left_height + right_height

        # Update global maximum diameter if needed
        largest_diameter[0] = max(largest_diameter[0], diameter)

        # Return height of this node
        return 1 + max(left_height, right_height)
    
    height(root)

    # Return the largest diameter found
    return largest_diameter[0]



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

    diameter = binary_tree_diameter(root)
    print("diamater of binary tree:", diameter)