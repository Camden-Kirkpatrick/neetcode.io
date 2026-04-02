# Binary Search Trees: Search, Insert, and Remove

## What is a Binary Search Tree?

A **Binary Search Tree (BST)** is a binary tree with a special rule:

- every value in the **left subtree** is smaller than the current node
- every value in the **right subtree** is larger than the current node

That rule lets us avoid checking every node.

---

## Example Trees

We will use these trees in this file.

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

### Tree Used for Insertion

```text
        10
      /    \
    8        13
  /   \     /   \
 4     9   11   17
```

### Tree Used for Removal

```text
        4
      /   \
     3     6
    /     / \
   2     5   7
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

Now the return value will travel back up the call stack.

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


# Removing from a Binary Search Tree

## What is BST Removal?

**Removal** means deleting a value from the tree while keeping the BST property valid.

This is more complicated than search and insertion because removing a node can change how the tree is connected.

When we delete a node, we must make sure the values on the left are still smaller and the values on the right are still larger.

---

## How BST Removal Works

1. Start at the root
2. Compare the value to remove with the current node
3. If the value is smaller, recurse left
4. If the value is larger, recurse right
5. If the value matches the current node, delete that node
6. Return the updated subtree so parent nodes reconnect correctly

---

## The Three Deletion Cases

When we find the node to remove, there are three possible cases.

### Case 1: The node has no children

This is a leaf node.

We can remove it by returning `None`.

### Case 2: The node has one child

We return the single child.

That child takes the deleted node's place.

### Case 3: The node has two children

We cannot just delete it immediately, because that would disconnect both subtrees.

Instead:

1. find the smallest node in the right subtree
2. copy that value into the current node
3. remove that duplicate value from the right subtree

That smallest value in the right subtree is called the **inorder successor**.

---

## Python Implementation

```python
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def find_min(root):
    while root.left:
        root = root.left
    return root


def remove_node(root, data):
    if not root:
        return None

    if data > root.data:
        root.right = remove_node(root.right, data)
    elif data < root.data:
        root.left = remove_node(root.left, data)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            min_node = find_min(root.right)
            root.data = min_node.data
            root.right = remove_node(root.right, min_node.data)

    return root
```

---

## Tree Used for Removal

We will remove values from this tree:

```text
        4
      /   \
     3     6
    /     / \
   2     5   7
```

This tree is useful because it lets us show all three deletion cases:

- removing `4` shows the **two-children case**
- removing `3` shows the **one-child case**
- removing `5` shows the **leaf case**

---

## Walkthrough 1: Remove Node 4

Suppose:

```text
remove 4
```

We start with:

```text
        4
      /   \
     3     6
    /     / \
   2     5   7
```

### Step 1

Start at the root:

```text
current node = 4
```

Compare:

```text
4 == 4
```

So we found the node to remove.

Now we must decide which deletion case applies.

---

### Step 2: Determine the Case

Node `4` has:

- a left child: `3`
- a right child: `6`

So this is the **two-children case**.

We cannot simply return `None`.

We also cannot simply return one child, because that would throw away the other subtree.

So we need a replacement value that keeps the BST valid.

---

### Step 3: Find the Smallest Value in the Right Subtree

The right subtree of `4` is:

```text
    6
   / \
  5   7
```

To find the smallest value in a BST subtree, we go left as far as possible.

Start at `6`:

```text
6 -> go left -> 5
```

Node `5` has no left child, so `5` is the minimum.

So:

```text
inorder successor = 5
```

---

### Step 4: Copy the Successor Value into the Current Node

We do:

```python
root.data = min_node.data
```

So the root node's value changes from `4` to `5`.

The tree now looks like this:

```text
        5
      /   \
     3     6
    /     / \
   2     5   7
```

This can look strange at first, because now there are temporarily **two 5s**.

That is okay.

The next step is to delete the duplicate `5` from the right subtree.

---

### Step 5: Remove the Duplicate 5 from the Right Subtree

We make this recursive call:

```python
root.right = remove_node(root.right, 5)
```

That means:

- go into the subtree rooted at `6`
- remove the node with value `5`

Now we trace that recursive deletion.

---

### Step 6: Recursive Deletion Inside the Right Subtree

We are now at node `6`.

Compare:

```text
5 < 6
```

So we recurse left:

```python
root.left = remove_node(root.left, 5)
```

That takes us to node `5`.

Now compare:

```text
5 == 5
```

We found the node to delete.

This node has:

- no left child
- no right child

So this is the **leaf case**.

The function returns:

```python
None
```

That means node `6.left` becomes `None`.

So the subtree rooted at `6` is now:

```text
  6
   \
    7
```

---

## What Happens While Returning from Recursion in Remove 4?

Now the updated subtree returns upward.

### Return to the Call at Node 6

Node `6` made this call:

```python
root.left = remove_node(root.left, 5)
```

That call returned `None`.

So now:

```python
6.left = None
```

Node `6` then returns itself upward.

---

### Return to the Original Call at the Root

The original root node, which now stores `5`, made this call:

```python
root.right = remove_node(root.right, 5)
```

That call returned the updated subtree rooted at `6`.

So the root reconnects its right child to that updated subtree.

---

## Final Tree After Removing 4

```text
        5
      /   \
     3     6
    /       \
   2         7
```

---

## Why Removing 4 Shows the Two-Children Case

The original node `4` had two children.

So removal required three important ideas:

1. find a replacement value
2. copy it into the node being deleted
3. delete the duplicate from the right subtree

This is the most complex deletion case.

---

## Walkthrough 2: Remove Node 3

For this example, start again from the **original tree**:

```text
        4
      /   \
     3     6
    /     / \
   2     5   7
```

Suppose:

```text
remove 3
```

### Step 1

Start at the root:

```text
current node = 4
```

Compare:

```text
3 < 4
```

So the value must be in the **left subtree**.

We make this recursive call:

```python
root.left = remove_node(root.left, 3)
```

That takes us to node `3`.

---

### Step 2

Now we are at node `3`.

Compare:

```text
3 == 3
```

We found the node to remove.

Now we determine the case.

---

### Step 3: Determine the Case

Node `3` has:

- a left child: `2`
- no right child

So this is the **one-child case**.

Since node `3` only has one child, we do not need a successor.

We simply return its only child.

This line runs:

```python
return root.left
```

That returns node `2`.

---

## What Happens While Returning from Recursion in Remove 3?

Now that returned node `2` goes back to the caller.

### Return to the Call at Node 4

Node `4` made this call:

```python
root.left = remove_node(root.left, 3)
```

That call returned node `2`.

So node `4` now does:

```python
4.left = 2
```

That means node `2` takes node `3`'s place in the tree.

---

## Final Tree After Removing 3

```text
        4
      /   \
     2     6
          / \
         5   7
```

---

## Why Removing 3 Shows the One-Child Case

The node `3` had exactly one child.

So deletion was simpler:

- remove node `3`
- connect its parent directly to node `2`

Nothing else had to be rearranged.

---

## Walkthrough 3: Remove Node 5

Again, start from the **original tree**:

```text
        4
      /   \
     3     6
    /     / \
   2     5   7
```

Suppose:

```text
remove 5
```

### Step 1

Start at the root:

```text
current node = 4
```

Compare:

```text
5 > 4
```

So we recurse right:

```python
root.right = remove_node(root.right, 5)
```

That takes us to node `6`.

---

### Step 2

At node `6`, compare:

```text
5 < 6
```

So we recurse left:

```python
root.left = remove_node(root.left, 5)
```

That takes us to node `5`.

---

### Step 3

Now we are at node `5`.

Compare:

```text
5 == 5
```

We found the node to remove.

Now determine the case.

---

### Step 4: Determine the Case

Node `5` has:

- no left child
- no right child

So this is the **leaf case**.

A leaf node can simply be removed by returning `None`.

So this call returns:

```python
None
```

---

## What Happens While Returning from Recursion in Remove 5?

### Return to the Call at Node 6

Node `6` made this call:

```python
root.left = remove_node(root.left, 5)
```

That call returned `None`.

So now:

```python
6.left = None
```

Node `6` returns itself upward.

---

### Return to the Call at Node 4

Node `4` made this call:

```python
root.right = remove_node(root.right, 5)
```

That call returned the updated subtree rooted at `6`.

So node `4` reconnects its right child to that subtree.

---

## Final Tree After Removing 5

```text
        4
      /   \
     3     6
    /       \
   2         7
```

---

## Why Removing 5 Shows the Leaf Case

The node `5` had no children.

So deletion was the simplest possible case:

- return `None`
- parent disconnects that leaf

---

## Key Idea for Removal

Just like insertion, deletion uses recursion to move downward.

But unlike insertion, the return value can mean different things:

- `None` if a node is removed and nothing replaces it
- a child node if one child takes the deleted node's place
- the same root node, but with an updated subtree attached

That is why these lines matter:

```python
root.right = remove_node(root.right, data)
root.left = remove_node(root.left, data)
```

They recurse downward, then reconnect the updated subtree on the way back up.

---

## Time Complexity of Removal

Let `n` = number of nodes.

### Balanced tree

If the tree is balanced, removal takes:

```text
O(log n)
```

because we only travel down the height of the tree.

### Skewed tree

If the tree is skewed, removal takes:

```text
O(n)
```

because we may have to walk through the whole chain.

---

## Space Complexity of Removal

This recursive version uses the call stack.

So the space complexity is:

```text
O(h)
```

Where `h` is the height of the tree.

That means:

- balanced tree: `O(log n)`
- skewed tree: `O(n)`

---

## Final Summary

### Search

- starts at the root
- moves left or right based on comparisons
- returns `True` if the target is found
- returns `False` if it reaches `None`
- passes the answer back up through the recursive calls

### Insertion

- starts at the root
- moves left or right based on comparisons
- creates a new node when it reaches `None`
- reconnects the updated subtree while returning from recursion

### Removal

- starts at the root
- moves left or right based on comparisons
- handles one of three deletion cases when the node is found
- returns the updated subtree while recursion unwinds

All three operations depend on the BST property:

```text
left < node < right
```

That property is what makes BSTs efficient.
