# Arrays

An **array** is a data structure that stores elements in **contiguous memory**.

Example:

```
int array[3] = {1, 3, 5};
```

Memory layout:

```
Index:  0   1   2
Value:  1   3   5
```

Arrays use **zero-based indexing**.

```
array[0] → first element
array[1] → second element
array[2] → third element
```

---

# Reading from an Array

To read a value, we access it using its **index**.

Example:

```
cout << array[0];   // Output: 1
```

The number inside the brackets is the **index**.

---

# Memory Layout and Address Calculation

Arrays are stored in **contiguous memory**.

Example:

```
array[0] array[1] array[2]
```

Suppose the address of `array[0]` is:

```
0x73a11ff9c0
```

If an `int` uses **4 bytes**, then each element occupies 4 bytes.

The address of any element can be calculated with:

```
address of array[i] = base_address + (i × size_of_element)
```

Example: Find the address of `array[2]`.

```
array[2] = 0x73a11ff9c0 + (2 × 4)
         = 0x73a11ff9c8
```

Because the address can be calculated directly, the computer **does not need to search for the element**.

This is why array access is **constant time**.

```
Time Complexity: O(1)
```

Even accessing `array[2,000,000]` takes the same time.

This is where the term **Random Access Memory** comes from.

The CPU can jump directly to any memory address.

---

# Fixed Size of Arrays

Arrays have a **fixed size**.

Example:

```
int array[3] = {1, 3, 5};
```

The system allocates enough memory to hold:

```
3 × sizeof(int) = 12 bytes
```

Once this block is assigned, the memory immediately after it may belong to:

- another variable
- another array
- another part of the program
- the operating system

If we attempted to add another element beyond the array size, we might overwrite unrelated memory.

This can cause:

- undefined behavior
- memory corruption
- program crashes

This is the main limitation of **static arrays**.

---

# Writing to an Array

Example:

```
int array[3];
```

This allocates space for three integers but does not assign values.

Depending on the programming language:

- values may be **initialized to zero**
- values may contain **garbage (uninitialized data)**

---

# Ways to Declare Arrays

### 1. Provide Only the Size

```
int array[3];
```

In C/C++, elements may contain **garbage values** if not initialized.

---

### 2. Provide Only the Data

```
int array[] = {4, 8, 0};
```

The compiler determines the array size automatically.

---

### 3. Provide Both Size and Data

```
int array[3] = {3, 4, 5};
```

---

# Partial Initialization

If the array size is larger than the number of initializers:

```
int array[5] = {1, 2};
```

Remaining elements are automatically set to **0**.

Result:

```
{1, 2, 0, 0, 0}
```

---

# Writing to an Array

Example:

```
array[0] = 5;
```

Like reading, writing uses direct address calculation.

```
Time Complexity: O(1)
```

---

# Inserting into an Array (If Space Exists)

Example:

```
int array[3] = {5, 6};  // {5, 6, ?}
```

Insert at the end:

```
array[2] = 7
```

Result:

```
{5, 6, 7}
```

No elements move, so this is:

```
O(1)
```

---

# Inserting at the Beginning

Suppose we insert `4` into:

```
{5, 6}
```

We cannot overwrite `array[0]`.

Instead we shift elements right.

Original:

```
Index: 0 1
Value: 5 6
```

Shift right:

```
array[2] = array[1]
array[1] = array[0]
```

Now:

```
{5, 5, 6}
```

Insert new value:

```
array[0] = 4
```

Final:

```
{4, 5, 6}
```

Because elements must move, insertion is:

```
O(n)
```

---

# Deleting from an Array

Example:

```
{3, 4, 5}
```

Delete the first element.

Shift elements left:

```
array[0] = array[1]
array[1] = array[2]
```

Result:

```
{4, 5}
```

Deletion requires shifting elements, so it is:

```
O(n)
```

---

# Time Complexity Summary

| Operation | Complexity |
|----------|------------|
| Read i-th element | O(1) |
| Write i-th element | O(1) |
| Insert at end | O(1) |
| Insert at front | O(n) |
| Insert in middle | O(n) |
| Delete from front | O(n) |
| Delete from middle | O(n) |

---

# Dynamic Arrays

A **dynamic array** is an array that can **grow automatically when it runs out of space**.

Static arrays have a fixed size:

```
int array[3];
```

Once memory is allocated, the array cannot grow.

Dynamic arrays solve this limitation by allocating **a larger block of memory when necessary**.

---

# How Dynamic Arrays Grow

A dynamic array keeps track of two values:

```
size     → number of elements currently stored
capacity → total number of elements the array can hold
```

Example:

```
size = 3
capacity = 4
```

Memory layout:

```
Index:   0   1   2   3
Value:  10  20  30   ?
```

Three elements are stored, but there is still space for one more.

---

# What Happens When the Array Becomes Full

Suppose the array is full:

```
size = 4
capacity = 4

Index:   0   1   2   3
Value:  10  20  30  40
```

If we try to insert another element, the array must **resize**.

Resizing works like this:

1. Allocate a new block of memory with larger capacity (often **double the size**).
2. Copy all existing elements into the new memory.
3. Insert the new element.
4. Free the old memory block.

---

# Example Resize

Original array:

```
capacity = 4
```

```
[10, 20, 30, 40]
```

Resize to:

```
capacity = 8
```

New memory block:

```
[10, 20, 30, 40, ?, ?, ?, ?]
```

Now new elements can be inserted without resizing again immediately.

---

# Why Capacity Is Usually Doubled

Dynamic arrays often **double their capacity** during resizing.

Example growth pattern:

```
capacity = 1
capacity = 2
capacity = 4
capacity = 8
capacity = 16
```

Doubling prevents resizing from happening too frequently.

If the array only increased by one element each time, resizing would happen **every insertion**, which would be extremely slow.

---

# Time Complexity of Dynamic Arrays

Most operations are the same as static arrays.

| Operation | Complexity |
|----------|------------|
| Read i-th element | O(1) |
| Write i-th element | O(1) |
| Insert at end (average) | O(1) |
| Insert at end (resize) | O(n) |
| Insert at front | O(n) |
| Insert in middle | O(n) |
| Delete | O(n) |

Even though resizing takes **O(n)** time, it happens rarely.

Because of this, inserting at the end of a dynamic array is considered **amortized O(1)**.

---

# Dynamic Arrays in Real Programming Languages

Many programming languages use dynamic arrays internally.

Examples:

| Language | Dynamic Array Type |
|---------|-------------------|
| C++ | `std::vector` |
| Java | `ArrayList` |
| Python | `list` |
| JavaScript | `Array` |

These structures automatically handle resizing behind the scenes.