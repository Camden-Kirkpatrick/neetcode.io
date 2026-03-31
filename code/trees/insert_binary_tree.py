# Binary Search Tree (BST) Insertion
#
# This program demonstrates how to insert values into a
# Binary Search Tree using recursion.
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
# 3. Inserts a new value using recursion
# 4. Shows how the tree changes after insertion
#
#
# How Insertion Works
#
# To insert a value:
#
# 1. Start at the root
#
# 2. Compare the value with the current node:
#
#    - If value < current node:
#        go LEFT
#
#    - If value > current node:
#        go RIGHT
#
# 3. Repeat until:
#    - you reach a None (empty spot)
#
# 4. Insert the new node there
#
#
# Important Idea
#
# We are not searching for a value that already exists.
#
# We are searching for the correct POSITION where the
# new value should go.
#
#
# Example
#
# Initial Tree:
#
#         10
#       /    \
#     8        13
#   /   \     /   \
# 4       9  11    17
#
#
# Insert: 12
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
# Right child is None → insert here
#
#
# Final Tree:
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
# Key Idea
#
# Each recursive call moves us one level down the tree.
#
# When we reach a None:
#   → that is the correct insertion point
#
# The recursion then "builds back up", reconnecting nodes.
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


def insert_node(root, data):
    # Base Case:
    # If we reach an empty spot, insert the new node here
    if not root:
        return TreeNode(data)
    
    # If the value is greater, go to the right subtree
    if data > root.data:
        root.right = insert_node(root.right, data)

    # If the value is smaller, go to the left subtree
    elif data < root.data:
        root.left = insert_node(root.left, data)

    # If the value already exists, do nothing (no duplicates)
    
    # Return the root so parent nodes can reconnect properly
    return root


#         10
#       /    \
#     8        13
#   /   \     /   \
# 4       9  11    17
if __name__ == "__main__":

    # Create root node
    root = TreeNode(10)

    # Build left subtree
    n1 = TreeNode(8)
    root.left = n1

    n3 = TreeNode(4)
    n1.left = n3

    n5 = TreeNode(9)
    n1.right = n5

    # Build right subtree
    n2 = TreeNode(13)
    root.right = n2

    n4 = TreeNode(11)
    n2.left = n4

    n6 = TreeNode(17)
    n2.right = n6


    # Insert a new value into the BST
    new_node = 12

    # IMPORTANT:
    # We assign back to root in case the tree was empty
    root = insert_node(root, new_node)

    print("Inserted", new_node)


    # Final Binary Tree
    #
    #         10
    #       /    \
    #     8        13
    #   /   \     /   \
    # 4       9  11    17
    #               \
    #                12