# Stacks

A **stack** is a data structure that follows the **Last In, First Out (LIFO)** rule.

The most recently added element is always the first one removed.

Example:

push(10)  
push(20)  
push(30)

```
bottom
  ↓
[10][20][30]
           ↑
          top
```

pop() → 30

---

# Stack Structure

A stack stores elements in order, but operations only happen at **one end** of the structure.

That position is called the **top**.

Example using an array implementation:

```
index: 0   1   2
       ↓   ↓   ↓
      [10][20][30]
                ↑
               top
```

The **rightmost element** is the top of the stack.

---

# Stack Implementation

The Python implementation uses a **dynamic array**.

Elements are added to and removed from the **end of the array**.

Example:

```
push(3)

[3]
 ↑
top
```

```
push(8)

[3][8]
    ↑
   top
```

```
push(0)

[3][8][0]
       ↑
      top
```

---

# Stack Operations

## Push

Push adds a value to the **top** of the stack.

```
Before push(30)

[10][20]
      ↑
     top
```

```
After push(30)

[10][20][30]
           ↑
          top
```

Time Complexity:

O(1) amortized

---

## Pop

Pop removes the value at the **top**.

```
Before pop()

[10][20][30]
           ↑
          top
```

```
After pop()

[10][20]
      ↑
     top
```

Time Complexity:

O(1)

---

## Peek

Peek returns the top value without removing it.

```
[10][20][30]
           ↑
          top
```

peek() → 30

Time Complexity:

O(1)

---

# Time Complexity Summary

| Operation | Complexity |
|-----------|------------|
| Push | O(1) amortized |
| Pop | O(1) |
| Peek | O(1) |
| Check Empty | O(1) |
