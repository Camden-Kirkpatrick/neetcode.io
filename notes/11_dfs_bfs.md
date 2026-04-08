# Binary Tree Traversals: Depth-First Search (DFS) and Breadth-First Search (BFS)

## What is Depth-First Search?

Depth-First Search (DFS) explores a tree by going as deep as possible down one path before backtracking.

Instead of visiting nodes level-by-level, DFS fully explores one branch before moving to another.

This is naturally implemented using recursion.

---

## Example Tree

We will use this tree throughout:

```text
        4
      /   \
     3     6
    /     / \
   2     5   7
```

---

# Types of DFS Traversals

There are three types:

1. Inorder
2. Preorder
3. Postorder

The ONLY difference is when we print the node.

---

# Inorder Traversal (Left → Node → Right)

## Code

```python
def inorder(root):
    if not root:
        return

    inorder(root.left)
    print(root.data)
    inorder(root.right)
```

---

## Key Idea

We:
1. Go LEFT as far as possible
2. Then print
3. Then go RIGHT

---

## Full Step-by-Step Execution

Call:

```python
inorder(4)
```

### Step 1

At node 4

- go left → 3

---

### Step 2

At node 3

- go left → 2

---

### Step 3

At node 2

- go left → None → return

---

### Step 4

Back at node 2

- print 2

---

### Step 5

- go right → None → return

Node 2 is done

---

### Step 6

Back at node 3

- print 3

---

### Step 7

- go right → None → return

Node 3 is done

---

### Step 8

Back at node 4

- print 4

---

### Step 9

- go right → 6

---

### Step 10

At node 6

- go left → 5

---

### Step 11

At node 5

- go left → None → return
- print 5
- go right → None → return

Node 5 is done

---

### Step 12

Back at node 6

- print 6

---

### Step 13

- go right → 7

---

### Step 14

At node 7

- go left → None → return
- print 7
- go right → None → return

Node 7 is done

---

## Final Result

```text
2 3 4 5 6 7
```

---

## Highest → Lowest

Reverse inorder:

```python
def reverse_inorder(root):
    if not root:
        return

    reverse_inorder(root.right)
    print(root.data)
    reverse_inorder(root.left)
```

---

## Step-by-step (short)

- go right → 6 → 7
- print 7
- print 6
- print 5
- print 4
- print 3
- print 2

---

## Result

```text
7 6 5 4 3 2
```

---

# Preorder Traversal (Node → Left → Right)

## Code

```python
def preorder(root):
    if not root:
        return

    print(root.data)
    preorder(root.left)
    preorder(root.right)
```

---

## Key Idea

We:
1. Print FIRST
2. Then go LEFT
3. Then go RIGHT

---

## Full Step-by-step Execution

Call:

```python
preorder(4)
```

---

### Step 1

At node 4

- print 4
- go left → 3

---

### Step 2

At node 3

- print 3
- go left → 2

---

### Step 3

At node 2

- print 2
- go left → None → return
- go right → None → return

Node 2 done

---

### Step 4

Back at node 3

- go right → None → return

Node 3 done

---

### Step 5

Back at node 4

- go right → 6

---

### Step 6

At node 6

- print 6
- go left → 5

---

### Step 7

At node 5

- print 5
- go left → None
- go right → None

---

### Step 8

Back at node 6

- go right → 7

---

### Step 9

At node 7

- print 7
- go left → None
- go right → None

---

## Final Result

```text
4 3 2 6 5 7
```

---

# Postorder Traversal (Left → Right → Node)

## Code

```python
def postorder(root):
    if not root:
        return

    postorder(root.left)
    postorder(root.right)
    print(root.data)
```

---

## Key Idea

We:
1. Go LEFT
2. Go RIGHT
3. Print LAST

---

## Full Step-by-step Execution

Call:

```python
postorder(4)
```

---

### Step 1

At node 4

- go left → 3

---

### Step 2

At node 3

- go left → 2

---

### Step 3

At node 2

- go left → None
- go right → None
- print 2

---

### Step 4

Back at node 3

- go right → None
- print 3

---

### Step 5

Back at node 4

- go right → 6

---

### Step 6

At node 6

- go left → 5

---

### Step 7

At node 5

- go left → None
- go right → None
- print 5

---

### Step 8

Back at node 6

- go right → 7

---

### Step 9

At node 7

- go left → None
- go right → None
- print 7

---

### Step 10

Back at node 6

- print 6

---

### Step 11

Back at node 4

- print 4

---

## Final Result

```text
2 3 5 7 6 4
```

---

# DFS Summary

- Inorder → sorted order
- Preorder → root first
- Postorder → root last

---

# DFS Complexity

Time: O(n)  
Space: O(h)

- balanced → O(log n)
- skewed → O(n)

---

# Breadth-First Search (BFS)

## What is Breadth-First Search?

Breadth-First Search (BFS) explores a tree layer by layer.

You visit all nodes at the current depth before moving deeper. Within each level, you go left to right (for a binary tree, that means each node’s left child is enqueued before its right child).

This is the opposite of DFS, which follows one branch as deep as possible before backtracking.

BFS is naturally implemented with a **queue** (FIFO): the next node you visit is always the one that has been waiting the longest since it was discovered.

---

## Example Tree

We will use the same tree:

```text
        4
      /   \
     3     6
    /     / \
   2     5   7
```

---

# Level-Order Traversal

Level-order traversal is the usual way to “run BFS” on a tree: print (or collect) nodes by depth, one level at a time.

---

## Code

```python
from collections import deque

def bfs(root):
    queue = deque()

    if not root:
        return

    queue.append(root)

    level = 0
    while len(queue) > 0:
        print("level:", level)
        for _ in range(len(queue)):
            curr = queue.popleft()
            print(curr.data)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        level += 1
```

---

## Key Idea

We:

1. Start with the root in the queue.
2. Repeat until the queue is empty:
   - Record how many nodes are in the queue **right now** (`len(queue)`). That count is exactly one level’s worth of nodes.
   - Dequeue that many times: each time, print the node and enqueue its children at the **back**.
3. Increment `level` after each pass.

Using `for _ in range(len(queue))` at the start of each outer iteration is what makes each printed block correspond to one depth: children added during that inner loop are not counted in the current `range`, so they are processed on the next level.

---

## Full Step-by-Step Execution

Call:

```python
bfs(root)  # root is the node with value 4
```

Assume the queue holds node values for readability (in code it holds `TreeNode` references).

---

### Step 1 — Level 0

- Queue: `[4]`
- Inner loop runs `len(queue) == 1` time.
- Dequeue `4`, print `4`. Enqueue `3`, then `6`.
- Queue: `[3, 6]`
- `level` becomes `1`.

---

### Step 2 — Level 1

- Queue: `[3, 6]`
- Inner loop runs `len(queue) == 2` times.
- First iteration: dequeue `3`, print `3`. Enqueue `2` → queue `[6, 2]`.
- Second iteration: dequeue `6`, print `6`. Enqueue `5`, then `7` → queue `[2, 5, 7]`.
- `level` becomes `2`.

---

### Step 3 — Level 2

- Queue: `[2, 5, 7]`
- Inner loop runs `len(queue) == 3` times.
- Dequeue `2`, print `2` (no children).
- Dequeue `5`, print `5` (no children).
- Dequeue `7`, print `7` (no children).
- Queue is empty; the outer `while` exits.

---

## Final Result

Printed values in order (ignoring the `"level:"` lines):

```text
4 3 6 2 5 7
```

---

## Why use a queue?

A queue is **FIFO** (first in, first out). BFS needs to visit nodes in order of **distance from the root**: every node at depth `d` must be handled before any node at depth `d + 1`. The node discovered first among those still waiting should be visited next—that is exactly what the front of a queue gives you. A stack (LIFO), as in recursive DFS, would instead always go back to the most recently discovered branch, which is depth-first, not breadth-first.

---

# BFS Summary

- Level-order (BFS) visits the root, then all nodes at depth 1, then depth 2, and so on; within a level, left before right when you enqueue left then right.
- Use a queue: dequeue to visit, enqueue children for later levels.
- The `len(queue)` snapshot splits processing into clear “levels” when printing layer by layer.

---

# BFS Complexity

Time: O(n) — each node is dequeued once and each edge is followed once.

Space: O(w), where w is the size of the **widest level** (maximum nodes on any single row). The queue’s peak size is on the order of that width: a bushy level can have Θ(n) nodes; a skewed tree has w = 1, so only O(1) extra queue space (time is still O(n)).
