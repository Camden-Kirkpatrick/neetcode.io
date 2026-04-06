# Balanced Binary Tree
#
# This program demonstrates how to check whether a
# Binary Tree is height-balanced using recursion.
#
# A tree is considered BALANCED if:
#
# For every node:
#    The difference between the left and right subtree heights is at most 1
#    |height(left) - height(right)| ≤ 1
#
#
# What This Program Does
#
# 1. Defines a TreeNode class
# 2. Builds a Binary Search Tree (BST)
# 3. Recursively checks if the tree is balanced
# 4. Prints the result
#
#
# Key Idea
#
# At every node, we:
#
#   1. Compute the height of the LEFT subtree
#   2. Compute the height of the RIGHT subtree
#   3. Check the difference between them
#
# If the difference is greater than 1:
#   → the tree is NOT balanced
#
#
# Why do we use balanced[0]?
#
# Python booleans are immutable.
#
# If we tried:
#
#   balanced = True
#
# and then modified it inside the nested function,
# Python would create a NEW local variable instead
# of updating the outer one.
#
# To fix this, we use a list:
#
#   balanced = [True]
#
# Lists are mutable, so:
#
#   balanced[0] = False
#
# updates the SAME object across all recursive calls.
#
#
# Optimization (Important)
#
# After computing left_height, we check:
#
#   if balanced[0] == False:
#       return 0
#
# Why?
#
# If we already know the tree is NOT balanced,
# there is NO reason to continue exploring the tree.
#
# So we stop early and avoid unnecessary work.
#
# This improves performance in cases where the tree
# becomes unbalanced near the top.
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
# We cannot determine if it's balanced yet,
# because we need:
#   - height(3)
#   - height(6)
#
#
# Go LEFT to node 3
#
# We cannot determine balance yet,
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
# |0 - 0| = 0 → balanced
#
# height(2) = 1
#
#
# Back to node 3
#
# left_height = 1
#
# Go RIGHT → None → return 0
#
# |1 - 0| = 1 → balanced
#
# height(3) = 2
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
# |0 - 0| = 0 → balanced
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
# |0 - 0| = 0 → balanced
#
# height(7) = 1
#
#
# Back to node 6
#
# right_height = 1
#
# |1 - 1| = 0 → balanced
#
# height(6) = 2
#
#
# Back to node 4
#
# right_height = 2
#
# |2 - 2| = 0 → balanced
#
#
# Final Answer:
#   Tree is BALANCED
#
#
# Key Insight
#
# Just like height and diameter:
#   recursion goes DOWN first
#
# But:
#   balance is checked on the way BACK UP
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


def is_balanced(root):
    # Store whether the tree is balanced
    # Use a list so it can be modified inside nested function
    balanced = [True]

    def height(root):
        # Base Case:
        # Empty node has height 0
        if not root:
            return 0
        
        # Compute left subtree height
        left_height = height(root.left)

        # Optimization:
        # If already unbalanced, stop further work
        if balanced[0] == False:
            return 0

        # Compute right subtree height
        right_height = height(root.right)

        # Check balance condition at this node
        if abs(left_height - right_height) > 1:
            balanced[0] = False
            return 0

        # Return height of this node
        return 1 + max(left_height, right_height)
    
    height(root)

    # Return final result
    return balanced[0]



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

    balanced = is_balanced(root)
    print(f"is the binary tree balanced? {'yes' if balanced else 'no'}")