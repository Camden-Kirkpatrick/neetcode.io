# Binary Tree Breadth-First Search (BFS) Traversal
#
# This program demonstrates how to traverse a Binary Tree
# using Breadth-First Search (BFS).
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
# 3. Traverses the tree using BFS (level-order):
#       - Visit nodes level by level, left to right
#
#
# What is BFS?
#
# Breadth-First Search explores a tree layer by layer.
#
# You visit all nodes at the current depth before moving deeper.
# This is the opposite of DFS, which goes deep along one branch first.
#
#
# Level-Order Traversal
#
# - Process level 0 (the root), then level 1, then level 2, and so on.
# - Within each level, visit nodes from left to right.
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
# Traversal Result (level-order):
#
# Level-order → 4 3 6 2 5 7
#
#
# Key Idea
#
# BFS is naturally implemented using a queue (FIFO).
#
# You enqueue the root, then repeatedly:
#   → dequeue the next node to visit
#   → enqueue its children (so deeper nodes wait their turn)
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
# Space Complexity (extra memory for the queue):
#   O(w), where w = size of the widest level (most nodes on one row).
#
#   The queue only stores the "frontier" you have not finished yet.
#   That frontier is never larger than one level at its fattest point,
#   so peak queue size is about w, not n (unless the tree is very wide).
#
#   Wide / bushy tree (e.g. many nodes on one level):
#       w can be on the order of n → O(n) queue space.
#
#   Skewed tree (each level has only one node, like a linked list):
#       w = 1 → O(1) queue space (time is still O(n) to visit every node).


from collections import deque


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


def bfs(root):
    queue = deque()

    # Base case: empty tree
    if not root:
        return

    queue.append(root)

    level = 0
    # Drain the queue in layers: each pass handles one depth before any deeper nodes print.
    while len(queue) > 0:
        print("level:", level)
        # Snapshot queue length so we only process nodes already in the queue:
        # one full level per outer iteration.
        for _ in range(len(queue)):
            curr = queue.popleft()
            print(curr.data)
            # Children join the back of the queue and are visited in a later layer.
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        level += 1


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

    print("level-order traversal (by level):")
    bfs(root)