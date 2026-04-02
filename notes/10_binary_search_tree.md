# Binary Search Trees: Search and Insert

## What is a Binary Search Tree?

A **Binary Search Tree (BST)** is a binary tree with a special rule:

- every value in the **left subtree** is smaller than the current node
- every value in the **right subtree** is larger than the current node

That rule lets us avoid checking every node.

---

## Example Tree

We will use these two trees in this file.

### Tree Used for Insertion

```text
        10
      /    \
    8        13
  /   \     /   \
 4     9   11   17
```

### Tree Used for Search

```text
        10
      /    \
    8        13
  /   \     /   \
 4     9   11   17
              \
               12
```

---

# Searching in a Binary Search Tree

## What is BST Search?

**Search** means checking whether a target value exists in the tree.

Because of the BST property:

- if the target is smaller, search left
- if the target is larger, search right
- if the target matches the current node, we found it

---

## How BST Search Works

1. Start at the root
2. Compare the target with the current node
3. If equal, return `True`
4. If smaller, recurse left
5. If larger, recurse right
6. If we reach `None`, return `False`

---

## Python Implementation

```python
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def search_tree(root, target):
    if not root:
        return False
    
    if target > root.data:
        return search_tree(root.right, target)
    elif target < root.data:
        return search_tree(root.left, target)
    else:
        return True
```

---

## Tree Used for Search

We will search for values in this tree:

```text
        10
      /    \
    8        13
  /   \     /   \
 4     9   11   17
              \
               12
```

---

## Walkthrough 1: Search for 12

Suppose:

```text
target = 12
```

### Step 1

Start at the root:

```text
current node = 10
```

Compare:

```text
12 > 10
```

So the target can only be in the **right subtree**.

We make this recursive call:

```python
return search_tree(root.right, 12)
```

That means this call now waits for the deeper recursive call to decide the answer.

---

### Step 2

Now we are at node `13`.

Compare:

```text
12 < 13
```

So the target can only be in the **left subtree**.

We make this recursive call:

```python
return search_tree(root.left, 12)
```

Again, this call waits for the deeper call to return `True` or `False`.

---

### Step 3

Now we are at node `11`.

Compare:

```text
12 > 11
```

So we recurse right:

```python
return search_tree(root.right, 12)
```

That takes us to node `12`.

---

### Step 4

Now we are at node `12`.

Compare:

```text
12 == 12
```

We found the target.

So this call returns:

```python
True
```

---

## What Happens While Returning from Recursion in Search?

Now the retrun value will travel back up the call stack

We are passing a boolean answer back upward.

Let’s walk back up.

---

### Return to the Call at Node 11

Node `11` made this call:

```python
return search_tree(root.right, 12)
```

That call returned:

```python
True
```

So node `11` also returns:

```python
True
```

---

### Return to the Call at Node 13

Node `13` made this call:

```python
return search_tree(root.left, 12)
```

That call returned:

```python
True
```

So node `13` also returns:

```python
True
```

---

### Return to the Call at Node 10

Node `10` made this call:

```python
return search_tree(root.right, 12)
```

That call returned:

```python
True
```

So node `10` also returns:

```python
True
```

That final `True` is what the original caller receives.

---

## Walkthrough 2: Search for 15

Now suppose:

```text
target = 15
```

Notice that `15` is not in the tree.

### Step 1

Start at `10`.

Compare:

```text
15 > 10
```

Go right.

---

### Step 2

Now at `13`.

Compare:

```text
15 > 13
```

Go right.

---

### Step 3

Now at `17`.

Compare:

```text
15 < 17
```

Go left.

---

### Step 4

Now `root` is `None`.

That means the target is not in the tree.

So this call returns:

```python
False
```

---

## What Happens While Returning in the Not-Found Case?

The `False` return value now travels back up the recursive calls.

- the call at `17` returns `False`
- the call at `13` returns `False`
- the call at `10` returns `False`

So the final answer is:

```text
not found
```

---

## Key Idea for Search

Search uses the BST property to eliminate half of the possible locations at each step.

And because each recursive call directly returns the result of the next one, the answer travels back up automatically.

That is why these lines work:

```python
return search_tree(root.right, target)
return search_tree(root.left, target)
```

They mean:

- go deeper into the correct subtree
- whatever answer comes back, return that same answer upward

---

## Time Complexity of Search

## Balanced vs Skewed Binary Search Trees

### Balanced Tree

A balanced BST keeps its height small, so operations are fast.

```text
        10
      /    \
    8        13
  /   \     /   \
 4     9   11   17
```

- Height is small (≈ log n)
- Each step eliminates about half the tree
- Search time: `O(log n)`

---

### Skewed Tree (Worst Case)

A skewed tree happens when nodes form a chain instead of branching.

#### Right-Skewed Tree

```text
10
  \
   13
     \
      17
        \
         20
           \
            25
```

#### Left-Skewed Tree

```text
        10
       /
      8
     /
    6
   /
  4
 /
2
```

---

### Why Skewed Trees Are Slow

Searching for a value (for example, `25`):

```text
10 → 13 → 17 → 20 → 25
```

You must check each node one-by-one.

Instead of cutting the search space in half, you move linearly:

```text
n → n-1 → n-2 → ...
```

So the time complexity becomes:

```text
O(n)
```

---

### Why Skewed Trees Happen

They usually occur when inserting already sorted data:

```text
insert: 10, 13, 17, 20, 25
```

Each value goes to the right, forming a chain.

---

### Key Intuition

Balanced tree:

```text
cut → cut → cut → fast
```

Skewed tree:

```text
walk → walk → walk → slow
```

---

### Memory Trick

A skewed BST is basically a linked list in disguise.

---

## Space Complexity of Search

This recursive version uses one stack frame per level.

So the space complexity is:

```text
O(h)
```

Where `h` is the height of the tree.

That means:

- balanced tree: `O(log n)`
- skewed tree: `O(n)`

---


# Inserting into a Binary Search Tree

## What is BST Insertion?

**Insertion** means adding a new value to the tree while keeping the BST property valid.

We do that by starting at the root and moving:

- **left** if the new value is smaller
- **right** if the new value is larger

We keep going until we reach `None`.

That `None` is the empty spot where the new node belongs.

---

## How BST Insertion Works

1. Start at the root
2. Compare the new value with the current node
3. If the value is smaller, recurse left
4. If the value is larger, recurse right
5. If we reach `None`, create and return a new node there
6. As recursion returns, each parent reconnects its left or right child to the returned node

---

## Python Implementation

```python
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
```

---

## Tree Before Insertion

We will insert `12` into this tree:

```text
        10
      /    \
    8        13
  /   \     /   \
 4     9   11   17
```

---

## Walkthrough: Insert 12

Suppose:

```text
new value = 12
```

### Step 1

Start at the root:

```text
current node = 10
```

Compare:

```text
12 > 10
```

So `12` must go in the **right subtree**.

That means we make this recursive call:

```python
root.right = insert_node(root.right, 12)
```

Since `root.right` is the node `13`, the call continues into the subtree rooted at `13`.

---

### Step 2

Now we are at node `13`.

Compare:

```text
12 < 13
```

So `12` must go in the **left subtree**.

We make this recursive call:

```python
root.left = insert_node(root.left, 12)
```

Since `root.left` is the node `11`, the call continues into the subtree rooted at `11`.

---

### Step 3

Now we are at node `11`.

Compare:

```text
12 > 11
```

So `12` must go in the **right subtree**.

We make this recursive call:

```python
root.right = insert_node(root.right, 12)
```

But `11.right` is currently `None`, so we recurse into an empty spot.

---

### Step 4: Base Case

Now `root` is `None`.

So this line runs:

```python
return TreeNode(12)
```

A new node containing `12` is created and returned.

This is the first return on the way back up.

---

## What Happens While Returning from Recursion?

This is the part that usually feels confusing.

The recursive calls do **not** just return and disappear.

Each returning call gives a value back to its parent call, and the parent uses that return value to reconnect the updated subtree.

Let’s walk back up carefully.

---

### Return to the Call at Node 11

Node `11` made this call:

```python
root.right = insert_node(root.right, 12)
```

The recursive call returned:

```python
TreeNode(12)
```

So now node `11` does this:

```python
11.right = TreeNode(12)
```

Now node `11` has been updated:

```text
11
  \
   12
```

Then the function returns node `11` itself:

```python
return root
```

So the updated subtree rooted at `11` is returned upward.

---

### Return to the Call at Node 13

Earlier, node `13` made this call:

```python
root.left = insert_node(root.left, 12)
```

That recursive call now returns the updated node `11`.

So node `13` reconnects its left child to that returned subtree:

```python
13.left = 11
```

But now `11` already has `12` attached as its right child, so the subtree under `13.left` is now:

```text
11
  \
   12
```

Then node `13` returns itself upward:

```python
return root
```

---

### Return to the Call at Node 10

At the root, node `10` originally made this call:

```python
root.right = insert_node(root.right, 12)
```

That recursive call now returns the updated node `13`.

So node `10` reconnects its right child to that returned subtree:

```python
10.right = 13
```

Then node `10` returns itself.

That is why the full tree is now updated correctly.

---

## Final Tree After Insertion

```text
        10
      /    \
    8        13
  /   \     /   \
 4     9   11   17
              \
               12
```

---

## Key Idea for Insertion

The base case creates the new node.

Then each recursive call returns back upward and reconnects the updated subtree.

That is why these lines matter:

```python
root.right = insert_node(root.right, data)
root.left = insert_node(root.left, data)
```

They do two jobs:

1. recurse downward to find the insertion spot
2. reconnect the returned subtree while coming back up

---

## Time Complexity of Insertion

Let `n` = number of nodes.

### Balanced tree

If the BST is balanced, each step moves down about one level of a short tree.

So insertion takes:

```text
O(log n)
```

### Skewed tree

If the BST is shaped like a chain, we may have to visit every node.

So insertion takes:

```text
O(n)
```

---

## Space Complexity of Insertion

This recursive version uses the call stack.

If the height of the tree is `h`, then the recursion depth is also `h`.

So the space complexity is:

```text
O(h)
```

Which means:

- balanced tree: `O(log n)`
- skewed tree: `O(n)`

---

## Final Summary

### Insertion

- starts at the root
- moves left or right based on comparisons
- creates a new node when it reaches `None`
- reconnects the updated subtree while returning from recursion

### Search

- starts at the root
- moves left or right based on comparisons
- returns `True` if the target is found
- returns `False` if it reaches `None`
- passes the answer back up through the recursive calls

Both operations depend on the BST property:

```text
left < node < right
```

That property is what makes BSTs efficient.