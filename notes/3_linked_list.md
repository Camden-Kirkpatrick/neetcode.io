# Linked Lists

A **linked list** is a data structure made of **nodes connected by pointers**.

Unlike arrays, linked list elements are **not stored next to each other in memory**.  
Instead, each node stores a reference to another node.

Example:

```
head → A → B → C → None
```

Each node contains:

```
data
pointer to the next node
```

The final node points to:

```
None
```

Because nodes are not stored contiguously in memory, a linked list **cannot jump directly to an index** like an array.

Instead, the list must be **traversed node by node**.

---

# Singly Linked Lists

A **singly linked list** is the simplest type of linked list.

Each node stores two values:

```
data
next
```

Structure:

```
[data | next]
```

Example:

```
head → A → B → C → None
```

Characteristics:

- Each node knows **only the next node**
- Traversal can move **forward only**
- Accessing a node requires **walking through the list**

---

# Doubly Linked Lists

A **doubly linked list** stores an additional pointer in each node.

Each node stores:

```
prev
data
next
```

Structure:

```
[prev | data | next]
```

Example:

```
head ↔ A ↔ B ↔ C
```

Characteristics:

- Nodes know both the **previous node** and the **next node**
- Traversal can move **forward or backward**
- Deleting nodes is easier when a reference to the node already exists

---

# Traversal

Traversal means **moving through the list node by node**.

Example list:

```
head → A → B → C → None
```

Traversal path:

```
A → B → C
```

Steps:

1. Start at the first real node
2. Move to the next node
3. Repeat until reaching `None`

Time complexity:

```
O(n)
```

because every node may need to be visited.

---

# Structural Design Decisions

The linked list implementations described here use several structural features that simplify algorithms.

These include:

- A **dummy / sentinel head node**
- A **tail pointer**
- A **previous pointer** (for doubly linked lists)

---

# Dummy / Sentinel Head Node

A **dummy node** exists before the first real node.

Example:

```
head(dummy) → A → B → C → None
```

The dummy node:

- does **not store real data**
- always exists
- ensures every real node has a **previous node**

The first real node is always:

```
head.next
```

If:

```
head.next = None
```

the list is empty.

This removes special cases when inserting or deleting the first node.

---

# Tail Pointer

The list stores a pointer to the **last node**.

Example:

```
head → A → B → C → None
                  ↑
                 tail
```

This allows nodes to be appended in **constant time**.

Without a tail pointer, appending would require traversing the entire list to locate the last node.

---

# Singly Linked List Operations

## Append (Add Node to End)

Appending inserts a node at the **end of the list**.

Example:

```
head → A → B → None
              ↑
             tail
```

Steps:

1. The current tail's next pointer is updated to reference the new node.
2. The new node becomes the last node.
3. The tail pointer moves to the new node.

Result:

```
head → A → B → X → None
                  ↑
                 tail
```

Time complexity:

```
O(1)
```

---

## Read Node by Index

To access a node:

1. Start at the first real node.
2. Move forward through the list.
3. Stop when the desired index is reached.

Example:

```
head → A → B → C
        0   1   2
```

To reach index 2:

```
A → B → C
```

Time complexity:

```
O(n)
```

---

## Update Node

Updating a node uses the **same traversal process as reading**.

Steps:

1. Traverse to the desired node.
2. Replace the value stored in that node.

Example:

```
head → A → B → C
          ↓
       change to 36
```

Result:

```
head → A → 36 → C
```

Time complexity:

```
O(n)
```

---

## Delete Node by Index

Deletion works by **skipping the node being removed**.

Example:

```
head(dummy) → A → B → C → None
```

Delete `B`.

Steps:

1. Move to the node before the node being deleted.
2. Update its next pointer to reference the node after the deleted node.

Result:

```
head → A → C → None
```

If the deleted node was the tail, the tail pointer moves backward.

Time complexity:

```
O(n)
```

---

# Doubly Linked List Operations

## Append

Steps:

1. Set the new node's `prev` pointer to the current tail.
2. Update the current tail's `next` pointer to reference the new node.
3. Move the tail pointer to the new node.

Result:

```
head ↔ A ↔ B ↔ X
                ↑
               tail
```

Time complexity:

```
O(1)
```

---

## Delete Node by Index

Example:

```
head ↔ A ↔ B ↔ C
```

Delete `B`.

Steps:

1. Traverse to the node.
2. Identify the node before it.
3. Identify the node after it.
4. Connect those two nodes together.

Result:

```
head ↔ A ↔ C
```

Time complexity:

```
O(n)
```

---

## Delete Node by Reference

If a reference to the node already exists:

1. Identify the previous node.
2. Identify the next node.
3. Connect them together.

Example:

```
A ↔ B ↔ C
```

Delete `B`:

```
A ↔ C
```

Time complexity:

```
O(1)
```

---

## Delete Head

Example:

```
head ↔ A ↔ B
```

Steps:

1. Identify the first real node.
2. Update the head's next pointer to skip that node.
3. Fix the previous pointer of the new first node.

Result:

```
head ↔ B
```

If the list becomes empty, the tail pointer resets to the dummy head.

---

## Delete Tail

Example:

```
head ↔ A ↔ B ↔ C
```

Steps:

1. Identify the current tail.
2. Move the tail pointer to the previous node.
3. Set the new tail's next pointer to `None`.

Result:

```
head ↔ A ↔ B
```

Time complexity:

```
O(1)
```

---

# Example Operations

## Singly Linked List Example

Initial list:

```
head → 10 → 20 → 30 → None
```

Append `40`:

```
head → 10 → 20 → 30 → 40 → None
```

Read index `2`:

```
10 → 20 → 30
```

Result:

```
30
```

Update index `1` to `99`:

```
head → 10 → 99 → 30 → 40 → None
```

Delete index `2`:

```
head → 10 → 99 → 40 → None
```

---

## Doubly Linked List Example

Initial list:

```
head ↔ 5 ↔ 15 ↔ 25
```

Append `35`:

```
head ↔ 5 ↔ 15 ↔ 25 ↔ 35
```

Delete node `15`:

```
head ↔ 5 ↔ 25 ↔ 35
```

Delete head:

```
head ↔ 25 ↔ 35
```

Delete tail:

```
head ↔ 25
```

---

# Time Complexity Summary

## Singly Linked List

| Operation | Complexity |
|----------|------------|
| Append | O(1) |
| Read by index | O(n) |
| Update by index | O(n) |
| Delete by index | O(n) |

---

## Doubly Linked List

| Operation | Complexity |
|----------|------------|
| Append | O(1) |
| Read by index | O(n) |
| Update by index | O(n) |
| Delete by index | O(n) |
| Delete by reference | O(1) |
| Delete head | O(1) |
| Delete tail | O(1) |