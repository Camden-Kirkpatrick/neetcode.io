# Binary Tree Depth-First Search (DFS) Traversals
#
# This program demonstrates how to traverse a Binary Tree
# using Depth-First Search (DFS).
#
# A Binary Tree is a structure where each node can have:
#   - a left child
#   - a right child
#
#
# What This Program Does
#
# 1. Defines a TreeNode class
# 2. Builds a Binary Search Tree (BST)
# 3. Traverses the tree using three DFS methods:
#       - Inorder
#       - Preorder
#       - Postorder
#
#
# What is DFS?
#
# Depth-First Search explores a tree by going as deep as possible
# before backtracking.
#
# Instead of visiting nodes level-by-level (like BFS),
# DFS fully explores one path before moving to another.
#
#
# Types of DFS Traversals
#
# 1. Inorder (Left → Node → Right)
#    - Visit left subtree
#    - Visit current node
#    - Visit right subtree
#
#    For a BST, this gives values in sorted order.
#
#
# 2. Preorder (Node → Left → Right)
#    - Visit current node first
#    - Then explore left subtree
#    - Then explore right subtree
#
#    Useful for copying or reconstructing trees.
#
#
# 3. Postorder (Left → Right → Node)
#    - Visit left subtree
#    - Visit right subtree
#    - Visit current node last
#
#    Useful for deleting/freeing trees.
#
#
# Example Tree:
#
#         4
#       /   \
#      3     6
#     /     / \
#    2     5   7
#
#
# Traversal Results:
#
# Inorder   → 2 3 4 5 6 7
# Preorder  → 4 3 2 6 5 7
# Postorder → 2 3 5 7 6 4
#
#
# Key Idea
#
# DFS is naturally implemented using recursion.
#
# Each function call:
#   → processes a node
#   → then recursively processes its children
#
#
# Complexity
#
# Let:
# n = number of nodes
#
# Time Complexity:
#   O(n) → every node is visited once
#
# Space Complexity:
#   O(h) → recursion stack (h = height of tree)
#
#   Best Case (balanced):
#       O(log n)
#
#   Worst Case (skewed):
#       O(n)


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


def inorder(root):
    # Base Case:
    # If the current node is None, stop recursion
    if not root:
        return
    
    # Visit left subtree
    inorder(root.left)

    # Visit current node
    print(root.data)

    # Visit right subtree
    inorder(root.right)


def preorder(root):
    # Base Case:
    # If the current node is None, stop recursion
    if not root:
        return
    
    # Visit current node FIRST
    print(root.data)

    # Then explore left subtree
    preorder(root.left)

    # Then explore right subtree
    preorder(root.right)


def postorder(root):
    # Base Case:
    # If the current node is None, stop recursion
    if not root:
        return
    
    # Visit left subtree
    postorder(root.left)

    # Visit right subtree
    postorder(root.right)

    # Visit current node LAST
    print(root.data)


# Use DFS to traverse the tree and add node values to an array
def inorder_array(root):
    arr = []

    def dfs(root):
        if not root:
            return
        
        dfs(root.left)
        arr.append(root.data)
        dfs(root.right)

    dfs(root)
    return arr

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

    print("inorder traversal:")
    inorder(root)
    print()

    print("preorder traversal:")
    preorder(root)
    print()

    print("postorder traversal:")
    postorder(root)
    print("\n\n")

    node_vals = inorder_array(root)
    print("nodes:", node_vals)