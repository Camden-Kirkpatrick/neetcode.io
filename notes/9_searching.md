# Searching: Binary Search

## What is Binary Search?

**Binary search** is an efficient algorithm for finding a target value in a **sorted array**.

Instead of checking every element one by one, it repeatedly cuts the search space in half.

---

## How Binary Search Works

1. Start with two pointers:
   - `low` at the start of the array
   - `high` at the end of the array

2. Find the middle index:

```text
mid = (low + high) // 2
```

3. Compare the target with the middle value:

- if `target > arr[mid]`, search the right half
- if `target < arr[mid]`, search the left half
- if `target == arr[mid]`, the target is found

4. Keep repeating until:
- the target is found, or
- the search space becomes empty (`low > high`)

---

## Python Implementation

```python
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if target > arr[mid]:
            low = mid + 1
        elif target < arr[mid]:
            high = mid - 1
        else:
            return mid

    return -1
```

---

## Example Array

```text
[1, 4, 7, 13, 16, 22, 39, 40]
```

---

## How the Code Works

We will use this same sorted array for all walkthroughs:

```text
[1, 4, 7, 13, 16, 22, 39, 40]
```

The indices are:

```text
 0  1  2   3   4   5   6   7
[1, 4, 7, 13, 16, 22, 39, 40]
```

---

### Walkthrough 1: Target Found

Suppose:

```text
target = 39
```

### Step 1

Start with the full array:

```text
low = 0
high = 7
```

Find the middle index:

```text
mid = (0 + 7) // 2 = 3
```

Middle value:

```text
arr[3] = 13
```

Compare:

```text
39 > 13
```

So the target must be on the **right side**.

Update:

```text
low = mid + 1 = 4
high = 7
```

New search range:

```text
indices 4 to 7
[16, 22, 39, 40]
```

---

### Step 2

Now:

```text
low = 4
high = 7
```

Find the middle index:

```text
mid = (4 + 7) // 2 = 5
```

Middle value:

```text
arr[5] = 22
```

Compare:

```text
39 > 22
```

So the target must still be on the **right side**.

Update:

```text
low = mid + 1 = 6
high = 7
```

New search range:

```text
indices 6 to 7
[39, 40]
```

---

### Step 3

Now:

```text
low = 6
high = 7
```

Find the middle index:

```text
mid = (6 + 7) // 2 = 6
```

Middle value:

```text
arr[6] = 39
```

Compare:

```text
39 == 39
```

So the target is found.

Return:

```text
6
```

---

### Walkthrough 2: Target Smaller Than All Values

Suppose:

```text
target = 0
```

### Step 1

Start with the full array:

```text
low = 0
high = 7
mid = (0 + 7) // 2 = 3
arr[3] = 13
```

Compare:

```text
0 < 13
```

So the target must be on the **left side**.

Update:

```text
low = 0
high = mid - 1 = 2
```

New search range:

```text
indices 0 to 2
[1, 4, 7]
```

---

### Step 2

Now:

```text
low = 0
high = 2
mid = (0 + 2) // 2 = 1
arr[1] = 4
```

Compare:

```text
0 < 4
```

Go left again.

Update:

```text
low = 0
high = mid - 1 = 0
```

New search range:

```text
index 0
[1]
```

---

### Step 3

Now:

```text
low = 0
high = 0
mid = (0 + 0) // 2 = 0
arr[0] = 1
```

Compare:

```text
0 < 1
```

Go left again.

Update:

```text
low = 0
high = mid - 1 = -1
```

---

### Step 4

Now:

```text
low = 0
high = -1
```

Check the loop condition:

```text
low <= high
0 <= -1  -> False
```

The search space is empty, so the target is not in the array.

Return:

```text
-1
```

---

### Walkthrough 3: Target Larger Than All Values

Suppose:

```text
target = 50
```

### Step 1

Start with the full array:

```text
low = 0
high = 7
mid = (0 + 7) // 2 = 3
arr[3] = 13
```

Compare:

```text
50 > 13
```

So go right.

Update:

```text
low = mid + 1 = 4
high = 7
```

New search range:

```text
indices 4 to 7
[16, 22, 39, 40]
```

---

### Step 2

Now:

```text
low = 4
high = 7
mid = (4 + 7) // 2 = 5
arr[5] = 22
```

Compare:

```text
50 > 22
```

Go right again.

Update:

```text
low = mid + 1 = 6
high = 7
```

New search range:

```text
indices 6 to 7
[39, 40]
```

---

### Step 3

Now:

```text
low = 6
high = 7
mid = (6 + 7) // 2 = 6
arr[6] = 39
```

Compare:

```text
50 > 39
```

Go right again.

Update:

```text
low = mid + 1 = 7
high = 7
```

New search range:

```text
index 7
[40]
```

---

### Step 4

Now:

```text
low = 7
high = 7
mid = (7 + 7) // 2 = 7
arr[7] = 40
```

Compare:

```text
50 > 40
```

Go right again.

Update:

```text
low = mid + 1 = 8
high = 7
```

---

### Step 5

Now:

```text
low = 8
high = 7
```

Check the loop condition:

```text
low <= high
8 <= 7  -> False
```

The search space is empty, so the target is not in the array.

Return:

```text
-1
```

---

### Walkthrough 4: Target Is In Range But Not Present

Suppose:

```text
target = 19
```

Notice that `19` is between the smallest and largest values in the array, but it is not actually present.

### Step 1

Start with the full array:

```text
low = 0
high = 7
mid = (0 + 7) // 2 = 3
arr[3] = 13
```

Compare:

```text
19 > 13
```

So go right.

Update:

```text
low = mid + 1 = 4
high = 7
```

New search range:

```text
indices 4 to 7
[16, 22, 39, 40]
```

---

### Step 2

Now:

```text
low = 4
high = 7
mid = (4 + 7) // 2 = 5
arr[5] = 22
```

Compare:

```text
19 < 22
```

So go left.

Update:

```text
low = 4
high = mid - 1 = 4
```

New search range:

```text
index 4
[16]
```

---

### Step 3

Now:

```text
low = 4
high = 4
mid = (4 + 4) // 2 = 4
arr[4] = 16
```

Compare:

```text
19 > 16
```

So go right.

Update:

```text
low = mid + 1 = 5
high = 4
```

---

### Step 4

Now:

```text
low = 5
high = 4
```

Check the loop condition:

```text
low <= high
5 <= 4  -> False
```

The search space is empty, so the target is not in the array.

Return:

```text
-1
```

---

## Key Idea

Binary search works by repeatedly cutting the search space in half.

That means we do **not** check every element.

Instead, each comparison tells us which half can be ignored.

---

## Time Complexity

Let `n` = number of elements

### What happens each step?

Each iteration cuts the remaining search space in half:

```text
n → n/2 → n/4 → n/8 → ...
```

For example, if there are 8 elements:

```text
8 → 4 → 2 → 1
```

So the number of steps grows very slowly as `n` gets larger.

---

### Total Time

The question is:

How many times can we divide `n` by 2 before we reach 1?

The answer is:

```text
log₂(n)
```

So the total time complexity is:

```text
O(log n)
```

This is much faster than linear search, which may need to check every element one by one.

---

## Space Complexity

This iterative version of binary search only uses a few extra variables:

- `low`
- `high`
- `mid`

It does not create new arrays.

So the space complexity is:

```text
O(1)
```

---

## Limitation

Binary search only works correctly if the array is already sorted.

If the array is not sorted, comparing with the middle value does not tell us which half to eliminate.

So with unsorted data, binary search does not work.

---

## Intuition

Binary search feels like:

```text
cut → cut → cut → found / not found
```

You keep narrowing down where the target could possibly be until:

- you find it, or
- there is nowhere left to look

---

## Final Summary

- Requires a **sorted array**
- Very fast: `O(log n)`
- Eliminates half the search space each step
- Uses only constant extra memory: `O(1)`
- Ends when:
  - the target is found, or
  - `low > high` (the search space is empty)

Binary search is one of the most efficient searching algorithms when the data is already sorted.
