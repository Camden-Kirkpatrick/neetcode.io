# Binary Search Tree (BST) Deletion
#
# This program demonstrates how to remove values from a
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
# 3. Removes a value using recursion
# 4. Shows how the tree changes after deletion
#
#
# How Deletion Works
#
# To remove a value:
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
#    - you find the node to delete
#
# 4. Handle one of three cases:
#
#    Case 1: No children (leaf node)
#        → simply remove it (return None)
#
#    Case 2: One child
#        → return the child (replace the node)
#
#    Case 3: Two children
#        → find the smallest value in the RIGHT subtree
#        → replace current node's value with it
#        → remove that duplicate value from the right subtree
#
#
# Important Idea
#
# We are not just removing a node directly.
#
# We must maintain the BST property after deletion.
#
#
# Example
#
# Initial Tree:
#
#         4
#       /   \
#      3     6
#     /     / \
#    2     5   7
#
#
# Remove: 4
#
# Step 1:
# Node 4 has TWO children
#
# Step 2:
# Find minimum in right subtree → 5
#
# Step 3:
# Replace 4 with 5
#
# Step 4:
# Remove 5 from right subtree
#
#
# Final Tree:
#
#         5
#       /   \
#      3     6
#     /       \
#    2         7
#
#
# Key Idea
#
# Each recursive call moves us down the tree to find the node.
#
# When we modify or remove a node:
#   → we return the updated subtree
#
# This allows parent nodes to reconnect properly.
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
    if not root:
        return TreeNode(data)
    
    if data > root.data:
        root.right = insert_node(root.right, data)
    elif data < root.data:
        root.left = insert_node(root.left, data)

    return root


def search_tree(root, target):
    if not root:
        return False
    
    if target > root.data:
        return search_tree(root.right, target)
    elif target < root.data:
        return search_tree(root.left, target)
    else:
        return True


# Helper function for remove_node
def find_min(root):
    while root.left:
        root = root.left
    return root


def remove_node(root, data):
    # Base Case:
    # If we reach an empty subtree, the value is not found
    if not root:
        return None

    # If the value is greater, go to the right subtree
    if data > root.data:
        root.right = remove_node(root.right, data)

    # If the value is smaller, go to the left subtree
    elif data < root.data:
        root.left = remove_node(root.left, data)

    # Node found → perform deletion
    else:
        # Case 1: No left child
        # Replace node with its right child
        if not root.left:
            return root.right

        # Case 2: No right child
        # Replace node with its left child
        elif not root.right:
            return root.left

        # Case 3: Two children
        else:
            # Find the smallest value in the right subtree
            min_node = find_min(root.right)

            # Replace current node's value with that minimum
            root.data = min_node.data

            # Remove the duplicate value from the right subtree
            root.right = remove_node(root.right, min_node.data)

    # Return the root so parent nodes reconnect properly
    return root


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