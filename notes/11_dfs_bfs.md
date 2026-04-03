# Binary Tree Traversals: Depth-First Search (DFS)

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

# Summary

- Inorder → sorted order
- Preorder → root first
- Postorder → root last

---

# Complexity

Time: O(n)  
Space: O(h)

- balanced → O(log n)
- skewed → O(n)

---

# (Coming Later)

- Breadth-First Search (BFS)
