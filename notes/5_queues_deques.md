# Queues and Deques

Queues and deques store elements in a specific order.

They differ in **where elements can be inserted and removed**.

---

# Queue

A **queue** follows the **First In, First Out (FIFO)** rule.

The first element added is the first element removed.

Example:

enqueue(10)  
enqueue(20)  
enqueue(30)

```
front
  ↓
[10] → [20] → [30]
               ↑
              back
```

dequeue() → 10

---

# Queue Structure

A queue has two important positions:

front – where elements are removed  
back – where elements are added

```
front
  ↓
[10] → [20] → [30]
               ↑
              back
```

enqueue adds at the **back**.  
dequeue removes from the **front**.

---

# Queue Implementation

The Python implementation uses a **doubly linked list**.

```
head ↔ [10] ↔ [20] ↔ [30] ↔ tail
```

The first real node is:

```
head.next
```

The last real node is:

```
tail.prev
```

This allows constant-time insertion and deletion.

---

# Queue Operations

## Enqueue

Add a value to the **back**.

```
Before enqueue(30)

front
  ↓
[10] → [20]
         ↑
        back
```

```
After enqueue(30)

front
  ↓
[10] → [20] → [30]
               ↑
              back
```

Time Complexity:

O(1)

---

## Dequeue

Remove the value at the **front**.

```
Before dequeue()

front
  ↓
[10] → [20] → [30]
               ↑
              back
```

```
After dequeue()

front
  ↓
[20] → [30]
         ↑
        back
```

Time Complexity:

O(1)

---

# Deque (Double Ended Queue)

A **deque** allows insertion and removal from **both ends**.

```
front
  ↓
[10] ↔ [20] ↔ [30]
                 ↑
                back
```

Supported operations:

- enqueue_front
- enqueue_back
- dequeue_front
- dequeue_back

---

# Time Complexity Summary

<div style="display:flex; gap:60px; align-items:flex-start;">

<div>

### Queue

| Operation | Complexity |
|-----------|------------|
| Enqueue | O(1) |
| Dequeue | O(1) |
| Check Empty | O(1) |

</div>

<div>

### Deque

| Operation | Complexity |
|-----------|------------|
| Enqueue Front | O(1) |
| Enqueue Back | O(1) |
| Dequeue Front | O(1) |
| Dequeue Back | O(1) |
| Check Empty | O(1) |

</div>

</div>
