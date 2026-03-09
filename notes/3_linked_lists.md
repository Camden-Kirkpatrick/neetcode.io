
# Linked Lists

A **linked list** is a data structure made of **nodes connected by pointers**.

Unlike arrays, linked list elements are **not stored next to each other in memory**.  
Instead, each node stores a reference to another node.

Example:

head → A → B → C → tail

Each node contains:

data  
pointer to the next node

Because nodes are not stored contiguously in memory, a linked list **cannot jump directly to an index** like an array.

Instead, the list must be **traversed node by node**.

---

# Singly Linked Lists

A **singly linked list** is the simplest type of linked list.

Each node stores two values:

data  
next

Structure:

[data | next]

Example:

head → A → B → C → tail

Characteristics:

- Each node knows **only the next node**
- Traversal can move **forward only**
- Accessing a node requires **walking through the list**

The implementation used in the Python code includes:

- A **dummy / sentinel head node**
- A **dummy / sentinel tail node**

Example empty list:

head → tail

The first real node is always:

head.next

If:

head.next is tail

the list is empty.

---

# Doubly Linked Lists

A **doubly linked list** stores an additional pointer in each node.

Each node stores:

prev  
data  
next

Structure:

[prev | data | next]

Example:

head ↔ A ↔ B ↔ C ↔ tail

Characteristics:

- Nodes know both the **previous node** and the **next node**
- Traversal can move **forward or backward**
- Deleting nodes is easier when a reference to the node already exists

The Python implementation also uses:

- A **dummy head node**
- A **dummy tail node**

Empty list:

head ↔ tail

The first real node is:

head.next

The last real node is:

tail.prev

---

# Traversal

Traversal means **moving through the list node by node**.

Example list:

head → A → B → C → tail

Traversal path:

A → B → C

Steps:

1. Start at the first real node
2. Move to the next node
3. Repeat until reaching the **dummy tail**

Time complexity:

O(n)

because every node may need to be visited.

---

# Structural Design Decisions

The linked list implementations described in the Python files use several structural features that simplify algorithms.

These include:

- A **dummy / sentinel head node**
- A **dummy / sentinel tail node**
- A **previous pointer** (for doubly linked lists)

---

# Dummy / Sentinel Nodes

A **dummy node** exists before the first real node and after the last real node.

Example:

head → A → B → C → tail

The dummy nodes:

- do **not store real data**
- always exist
- simplify insertion and deletion logic

The first real node is always:

head.next

The last real node is always:

tail.prev (doubly list)  
the node before tail (singly list)

This removes special cases when inserting or deleting the first or last node.

---

# Singly Linked List Operations

## Insert at Head

Steps:

1. Identify the first real node (head.next)
2. Insert the new node between head and that node

Example:

Before:

head → A → B → tail

Insert X:

head → X → A → B → tail

Time complexity:

O(1)

---

## Insert at Tail

Because the singly linked list does not store a previous pointer, the list must be **traversed to find the node before the dummy tail**.

Steps:

1. Traverse the list until reaching the node before tail
2. Insert the new node between that node and tail

Example:

Before:

head → A → B → tail

Insert X:

head → A → B → X → tail

Time complexity:

O(n)

---

## Insert at Index

Steps:

1. Traverse until reaching the node currently at the specified index
2. Insert the new node **before that node**

Example:

Before:

head → A → B → C → tail

Insert X at index 1:

head → A → X → B → C → tail

Time complexity:

O(n)

---

## Read Node by Index

To access a node:

1. Start at the first real node
2. Move forward through the list
3. Stop when the desired index is reached

Example:

head → A → B → C → tail
       0   1   2

Time complexity:

O(n)

---

## Update Node

Updating a node uses the **same traversal process as reading**.

Steps:

1. Traverse to the desired node
2. Replace the value stored in that node

Example:

Before:

head → A → B → C → tail

Update index 1:

head → A → 36 → C → tail

Time complexity:

O(n)

---

## Delete Node by Index

Deletion works by **skipping the node being removed**.

Example:

head → A → B → C → tail

Delete B.

Steps:

1. Move to the node before the node being deleted
2. Update its next pointer to reference the node after the deleted node

Result:

head → A → C → tail

Time complexity:

O(n)

---

## Delete Head

Example:

head → A → B → tail

Steps:

1. Check if the list is empty
2. Store the first real node
3. Move head.next to the second node

Result:

head → B → tail

Time complexity:

O(1)

---

## Delete Tail

Because a singly linked list has no previous pointer, the list must be traversed to find the node before the last real node.

Example:

head → A → B → C → tail

Steps:

1. Traverse to the node before C
2. Update its next pointer to reference tail

Result:

head → A → B → tail

Time complexity:

O(n)

---

# Doubly Linked List Operations

## Insert at Head

Steps:

1. Identify head.next
2. Insert the new node between head and that node
3. Fix both next and prev pointers

Example:

head ↔ A ↔ B ↔ tail

Insert X:

head ↔ X ↔ A ↔ B ↔ tail

Time complexity:

O(1)

---

## Insert at Tail

Because the doubly linked list stores a previous pointer, the last real node is always:

tail.prev

Steps:

1. Store tail.prev
2. Insert the new node between tail.prev and tail

Example:

head ↔ A ↔ B ↔ tail

Insert X:

head ↔ A ↔ B ↔ X ↔ tail

Time complexity:

O(1)

---

## Insert at Index

Steps:

1. Traverse to the node currently at the specified index
2. Insert the new node before that node
3. Fix both next and prev pointers

Time complexity:

O(n)

---

## Delete Node by Index

Example:

head ↔ A ↔ B ↔ C ↔ tail

Delete B.

Steps:

1. Traverse to the node
2. Identify the node before it
3. Identify the node after it
4. Connect those nodes together

Result:

head ↔ A ↔ C ↔ tail

Time complexity:

O(n)

---

## Delete Node by Reference

If a reference to the node already exists:

1. Identify the previous node
2. Identify the next node
3. Connect them together

Example:

A ↔ B ↔ C

Delete B:

A ↔ C

Time complexity:

O(1)

---

## Delete Head

Example:

head ↔ A ↔ B ↔ tail

Steps:

1. Identify the first real node
2. Move head.next to the second node
3. Fix the backward pointer

Result:

head ↔ B ↔ tail

Time complexity:

O(1)

---

## Delete Tail

Example:

head ↔ A ↔ B ↔ C ↔ tail

Steps:

1. Identify tail.prev
2. Move tail.prev to the previous node
3. Fix the next pointer

Result:

head ↔ A ↔ B ↔ tail

Time complexity:

O(1)

---

## Reverse Traversal

Because each node stores a previous pointer, traversal can also move backward.

Example:

head ↔ A ↔ B ↔ C ↔ tail

Reverse traversal:

C ← B ← A

Time complexity:

O(n)

---

# Time Complexity Summary

<div style="display:flex; gap:60px; align-items:flex-start;">

<div>

### Singly Linked List

| Operation        | Complexity |
|------------------|-----------|
| Insert at head   | O(1) |
| Insert at tail   | O(n) |
| Insert at index  | O(n) |
| Read by index    | O(n) |
| Update by index  | O(n) |
| Delete by index  | O(n) |
| Delete head      | O(1) |
| Delete tail      | O(n) |

</div>

<div>

### Doubly Linked List

| Operation          | Complexity |
|--------------------|-----------|
| Insert at head     | O(1) |
| Insert at tail     | O(1) |
| Insert at index    | O(n) |
| Read by index      | O(n) |
| Update by index    | O(n) |
| Delete by index    | O(n) |
| Delete head        | O(1) |
| Delete tail        | O(1) |
| Delete by reference| O(1) |
| Reverse traversal  | O(n) |

</div>

</div>
