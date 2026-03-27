# Sorting: Insertion Sort, Merge Sort, and Quick Sort

## What is Sorting?

**Sorting** means arranging data in a particular order, usually from **smallest to largest**.

Examples:

```text
[5, 2, 4, 1, 3]  ->  [1, 2, 3, 4, 5]
[9, 7, 1]        ->  [1, 7, 9]
```

Sorting is important because many other algorithms become easier or faster when data is already ordered.

---

# Insertion Sort

## What is Insertion Sort?

**Insertion sort** builds a sorted portion of the array one element at a time.

It starts by treating the first element as already sorted.

Then it repeatedly takes the next element and inserts it into the correct position in the sorted part of the array.

---

## How Insertion Sort Works

The array is divided into two parts:

1. **Sorted portion** on the left
2. **Unsorted portion** on the right

On each pass:

- take the next element from the unsorted portion
- compare it with elements in the sorted portion
- shift larger elements one position to the right
- insert the current element into the gap

---

## Example

```text
[3, 2, 5, 4, 1]
```

Step-by-step:

```text
Start:
[3 | 2, 5, 4, 1]

Insert 2:
[2, 3 | 5, 4, 1]

Insert 5:
[2, 3, 5 | 4, 1]

Insert 4:
[2, 3, 4, 5 | 1]

Insert 1:
[1, 2, 3, 4, 5]
```

The bar shows the boundary between the sorted and unsorted portions.

---

## Python Implementation

```python
def insertion_sort(arr):
    # Traverse from the second element to the end
    for i in range(1, len(arr)):

        # Start comparing with the previous element
        j = i - 1

        # Store the current value to insert
        x = arr[i]

        # Shift elements greater than x to the right
        while j >= 0 and arr[j] > x:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert x into its correct position
        arr[j + 1] = x
```

---

## How the Code Works

Suppose:

```text
arr = [3, 2, 5, 4, 1]
```

### Pass 1 (`i = 1`)

```text
x = 2
j = 0
```

Compare `arr[0]` with `x`:

```text
3 > 2
```

Shift `3` right:

```text
[3, 3, 5, 4, 1]
```

Insert `2`:

```text
[2, 3, 5, 4, 1]
```

---

### Pass 2 (`i = 2`)

```text
x = 5
j = 1
```

Compare `3` with `5`:

```text
3 > 5   -> false
```

No shifting is needed.

Array stays:

```text
[2, 3, 5, 4, 1]
```

---

### Pass 3 (`i = 3`)

```text
x = 4
j = 2
```

Compare `5` with `4`:

```text
5 > 4
```

Shift `5` right:

```text
[2, 3, 5, 5, 1]
```

Now compare `3` with `4`:

```text
3 > 4   -> false
```

Insert `4`:

```text
[2, 3, 4, 5, 1]
```

---

### Pass 4 (`i = 4`)

```text
x = 1
j = 3
```

Shift `5`, then `4`, then `3`, then `2` right:

```text
[2, 3, 4, 5, 5]
[2, 3, 4, 4, 5]
[2, 3, 3, 4, 5]
[2, 2, 3, 4, 5]
```

Insert `1`:

```text
[1, 2, 3, 4, 5]
```

---

## Key Idea

Insertion sort works by maintaining a sorted region and inserting one new element into that region each pass.

It is similar to how you might sort playing cards in your hand:

- pick up the next card
- slide larger cards over
- place the card into the correct position

---

## Time Complexity

Another way to think about the runtime:

For each element, we may need to compare it with every previous element.

Maximum work looks like this:

```text
i = 1   -> 1 comparison
i = 2   -> 2 comparisons
i = 3   -> 3 comparisons
...
i = n-1 -> n-1 comparisons
```

Total work:

```text
1 + 2 + 3 + ... + (n - 1)
```

This simplifies to:

```text
n(n - 1) / 2
```

So:

```text
Worst Case Time Complexity: O(n^2)
```

### Best Case

If the array is already sorted, the inner loop stops immediately each time.

So:

```text
Best Case Time Complexity: O(n)
```

---

## Space Complexity

Insertion sort is **in-place**.

It only uses a few extra variables like `i`, `j`, and `x`.

```text
Space Complexity: O(1)
```

---

## Strengths of Insertion Sort

- Simple to understand
- Easy to implement
- Good for small arrays
- Good when the array is already nearly sorted
- In-place

---

## Weaknesses of Insertion Sort

- Slow on large arrays
- Worst case is O(n^2)
- Repeated shifting can be expensive

---

# Merge Sort

## What is Merge Sort?

**Merge sort** is a **divide-and-conquer** sorting algorithm.

Instead of inserting values one at a time into a sorted portion, merge sort:

1. splits the array into smaller halves
2. recursively sorts those halves
3. merges the sorted halves back together

---

## How Merge Sort Works

The array is repeatedly divided until each part has only one element.

A single element is already sorted by itself.

Then the algorithm merges the small sorted parts into larger sorted parts until the full array is sorted.

---

## Example

```text
[8, 3, 7, 4, 2, 6, 5, 1]
```

Split phase:

```text
[8, 3, 7, 4, 2, 6, 5, 1]
-> [8, 3, 7, 4] and [2, 6, 5, 1]

[8, 3, 7, 4]
-> [8, 3] and [7, 4]

[2, 6, 5, 1]
-> [2, 6] and [5, 1]

[8, 3]
-> [8] and [3]

[7, 4]
-> [7] and [4]

[2, 6]
-> [2] and [6]

[5, 1]
-> [5] and [1]
```

Now every piece has one element.

Merge phase:

```text
[8] and [3]     -> [3, 8]
[7] and [4]     -> [4, 7]
[2] and [6]     -> [2, 6]
[5] and [1]     -> [1, 5]

[3, 8] and [4, 7] -> [3, 4, 7, 8]
[2, 6] and [1, 5] -> [1, 2, 5, 6]

[3, 4, 7, 8] and [1, 2, 5, 6] -> [1, 2, 3, 4, 5, 6, 7, 8]
```

---

## Python Implementation

```python
def merge(arr, low, mid, high):
    left = arr[low : mid + 1]
    right = arr[mid + 1 : high + 1]

    i = j = 0
    k = low
    m = len(left)
    n = len(right)

    while i < m and j < n:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < m:
        arr[k] = left[i]
        i += 1
        k += 1

    while j < n:
        arr[k] = right[j]
        j += 1
        k += 1


def merge_sort(arr, low, high):
    if low < high:
        mid = (low + high) // 2

        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)
        merge(arr, low, mid, high)
```

---

## How Merge Sort Works Internally

Suppose:

```text
arr = [4, 1, 8, 7, 5]
```

### Step 1: Split

```text
merge_sort(arr, 0, 4)
```

Middle:

```text
mid = 2
```

Split into:

```text
left  -> indices 0 to 2
right -> indices 3 to 4
```

So the calls become:

```text
merge_sort(arr, 0, 2)
merge_sort(arr, 3, 4)
```

---

### Step 2: Keep Splitting

The left side:

```text
[4, 1, 8]
```

splits into:

```text
[4, 1] and [8]
```

Then:

```text
[4] and [1]
```

The right side:

```text
[7, 5]
```

splits into:

```text
[7] and [5]
```

Eventually every subarray has size 1.

That is the base case:

```text
one element = already sorted
```

---

## Recursion Tree for Merge Sort

This tree shows how the recursive calls split the array:

```text
merge_sort([8, 3, 7, 4, 2, 6, 5, 1])
|
+-- merge_sort([8, 3, 7, 4])
|   |
|   +-- merge_sort([8, 3])
|   |   |
|   |   +-- merge_sort([8])
|   |   +-- merge_sort([3])
|   |   \
|   |    merge -> [3, 8]
|   |
|   +-- merge_sort([7, 4])
|   |   |
|   |   +-- merge_sort([7])
|   |   +-- merge_sort([4])
|   |   \
|   |    merge -> [4, 7]
|   |
|   \
|    merge -> [3, 4, 7, 8]
|
+-- merge_sort([2, 6, 5, 1])
|   |
|   +-- merge_sort([2, 6])
|   |   |
|   |   +-- merge_sort([2])
|   |   +-- merge_sort([6])
|   |   \
|   |    merge -> [2, 6]
|   |
|   +-- merge_sort([5, 1])
|   |   |
|   |   +-- merge_sort([5])
|   |   +-- merge_sort([1])
|   |   \
|   |    merge -> [1, 5]
|   |
|   \
|    merge -> [1, 2, 5, 6]
|
\
 merge -> [1, 2, 3, 4, 5, 6, 7, 8]
```

---

## How the Merge Step Works

Suppose we are merging:

```text
A = [1, 4, 8]
B = [5, 7]
```

We compare the front elements of each array:

```text
1 vs 5 -> take 1
4 vs 5 -> take 4
8 vs 5 -> take 5
8 vs 7 -> take 7
```

Now `B` is exhausted, so copy the remaining value from `A`:

```text
8
```

Final merged result:

```text
[1, 4, 5, 7, 8]
```

---

## Key Idea

Merge sort first breaks the problem into smaller pieces, then combines the sorted pieces.

The most important fact is:

> merging two already-sorted arrays can be done efficiently

That is why the algorithm works so well.

---

## Time Complexity

### Where does the work happen?

Merge sort has two phases:

1. Splitting the array
2. Merging the array

Splitting is very cheap because it mostly just involves calculating indices and making recursive calls.

The real work happens during **merging**.

---

### Cost of One Merge

Suppose we merge two sorted subarrays:

- A of size `m`
- B of size `n`

There are `m + n` total elements to place into the final array.

During the merge:

- each step places exactly one element
- once an element is placed, it is never revisited

So across the main loop and the leftover loops, every element is copied exactly once.

---

### Final Conclusion

The total work is proportional to the number of elements:

`m + n`

So the time complexity of one merge is:

`O(m + n)`

---

### Work Per Level

At each level of recursion, several merges happen.

For example, if n = 8, one level might look like this:

[8]+[3]   [7]+[4]   [2]+[6]   [5]+[1]

Each merge handles 2 elements, so the total work at that level is:

2 + 2 + 2 + 2 = 8

That equals n.

At the next level, the merges might be:

[3,8]+[4,7]   [2,6]+[1,5]

Each merge now handles 4 elements, so the total work is:

4 + 4 = 8

Again, that equals n.

At the top level, we merge:

[3,4,7,8] + [1,2,5,6]

That handles all 8 elements:

8

So the key pattern is:

**Each level of recursion does a total of n work.**

This is true because:

- every element appears in exactly one subarray at that level
- every element is merged exactly once at that level

---

### Number of Levels

Merge sort repeatedly splits the array in half:

n → n/2 → n/4 → n/8 → ... → 1

The question is:

How many times can we divide n by 2 until we reach 1?

The answer is:

log2(n)

However, one important detail:

- The deepest level (where all subarrays have size 1) is the base case
- No merging happens at that level

So while the full recursion tree has log2(n) + 1 levels, only log2(n) levels actually perform merging work.

---

### Total Work

Now combine the two facts:

- work per level = n
- number of levels that do work = log(n)

So the total work is:

n + n + n + ... (repeated log(n) times)

That gives:

O(n log n)

---

### Best and Worst Case

Merge sort always performs the same overall process:

- split the array
- recursively sort both halves
- merge the halves

Even if the array is already sorted, merge sort still does all of this work.

So:

- Best Case Time Complexity: O(n log n)
- Worst Case Time Complexity: O(n log n)

---

### Final Intuition

A simple way to remember it is:

Merge sort does n work per level, and there are log(n) levels where merging happens.

So:

O(n log n)

---

## Space Complexity

This version of merge sort creates temporary arrays:

```python
A = arr[low : mid + 1]
B = arr[mid + 1 : high + 1]
```

So it is **not in-place**.

```text
Space Complexity: O(n)
```

---

## Strengths of Merge Sort

- Much faster than insertion sort on large inputs
- Predictable O(n log n) runtime
- Works well for large datasets
- Very good example of divide-and-conquer

---

## Weaknesses of Merge Sort

- Uses extra memory
- More complex than insertion sort
- For very small arrays, the overhead may not be worth it

---


# Quick Sort

## What is Quick Sort?

**Quick sort** is a **divide-and-conquer** sorting algorithm.

Instead of merging sorted halves like merge sort, quick sort:

1. picks a pivot
2. partitions the array around that pivot
3. recursively sorts the left and right sides

---

## How Quick Sort Works

The array is divided based on a pivot element.

After partitioning:

- all elements smaller than the pivot are on the left
- all elements greater than or equal to the pivot are on the right
- the pivot is in its final sorted position

Then the algorithm recursively sorts both sides.

---

## Example

```text
[4, 2, 7, 1, 6, 3, 8, 5]
```

---

## Python Implementation

```python
def quick_sort(arr, start, end):
    if start >= end:
        return

    pivot = arr[end]
    left = start

    for i in range(start, end):
        if arr[i] < pivot:
            arr[left], arr[i] = arr[i], arr[left]
            left += 1

    arr[end], arr[left] = arr[left], arr[end]

    quick_sort(arr, start, left - 1)
    quick_sort(arr, left + 1, end)
```

---

## How Quick Sort Works Internally

Suppose:

```text
arr = [4, 2, 7, 1, 6, 3, 8, 5]
```

### Step 1: First Partition

```text
quick_sort(arr, 0, 7)
```

Pivot (right-most element):

```text
5
```

After partitioning:

```text
[4, 2, 1, 3, 5, 7, 8, 6]
```

Now:

```text
left side  -> [4, 2, 1, 3]
right side -> [7, 8, 6]
```

The pivot `5` is now in its final sorted position.

---

### Step 2: Partition the Left and Right Sides

Left side:

```text
[4, 2, 1, 3]
```

Pivot:

```text
3
```

After partitioning:

```text
[2, 1, 3, 4]
```

Right side:

```text
[7, 8, 6]
```

Pivot:

```text
6
```

After partitioning:

```text
[6, 8, 7]
```

---

### Step 3: Keep Partitioning

Now the remaining unsorted subarrays are:

```text
[2, 1]   [8, 7]
```

Partition `[2, 1]` around pivot `1`:

```text
[1, 2]
```

Partition `[8, 7]` around pivot `7`:

```text
[7, 8]
```

Now the full array is sorted.

---

## Recursion Tree for Quick Sort

This tree shows how the recursive calls partition the array:

```text
quick_sort([4, 2, 7, 1, 6, 3, 8, 5])
|
+-- partition around 5 -> [4, 2, 1, 3] [5] [7, 8, 6]
|
+-- quick_sort([4, 2, 1, 3])
|   |
|   +-- partition around 3 -> [2, 1] [3] [4]
|   |
|   +-- quick_sort([2, 1])
|   |   |
|   |   +-- partition around 1 -> [] [1] [2]
|   |   |
|   |   +-- quick_sort([])  -> base case
|   |   +-- quick_sort([2]) -> base case
|   |
|   +-- quick_sort([4]) -> base case
|
+-- quick_sort([7, 8, 6])
|   |
|   +-- partition around 6 -> [] [6] [8, 7]
|   |
|   +-- quick_sort([]) -> base case
|   +-- quick_sort([8, 7])
|       |
|       +-- partition around 7 -> [] [7] [8]
|       |
|       +-- quick_sort([])  -> base case
|       +-- quick_sort([8]) -> base case
|
\\
 final sorted array -> [1, 2, 3, 4, 5, 6, 7, 8]
```

---

## How the Partition Step Works

Suppose we partition:

```text
[4, 2, 7, 1, 6, 3, 8, 5]
```

with pivot:

```text
5
```

We compare each element before the pivot to `5`:

```text
4 < 5 -> goes left
2 < 5 -> goes left
7 < 5 -> stays on right
1 < 5 -> goes left
6 < 5 -> stays on right
3 < 5 -> goes left
8 < 5 -> stays on right
```

After those comparisons, we place the pivot between the two groups:

```text
[4, 2, 1, 3, 5, 7, 8, 6]
```

So partitioning puts the pivot into its correct sorted position.

---

## Key Idea

Quick sort works by placing one element, the pivot, into its correct position each time.

After partitioning:

- everything to the left is smaller
- everything to the right is greater than or equal to it

That means the pivot never needs to move again.

---

## Time Complexity

### Where does the work happen?

Quick sort has two main parts:

1. Partitioning the array
2. Recursively sorting the left and right sides

The real work happens during **partitioning**.

That is because partitioning scans through the current subarray once.

---

### Cost of One Partition

Suppose the current subarray has size `n`.

The loop checks every element except the pivot itself.

So the partition step does:

```text
n - 1 comparisons
```

That means one partition takes:

```text
O(n) time
```

---

### Work Per Level

At each level of recursion, several partitions may happen.

Using our example with `n = 8`:

Level 1:

```text
[4, 2, 7, 1, 6, 3, 8, 5]
```

One partition of size 8:

```text
7 comparisons
```

Level 2:

```text
[4, 2, 1, 3]   [7, 8, 6]
```

Partitions of sizes 4 and 3:

```text
3 + 2 = 5 comparisons
```

Level 3:

```text
[2, 1]   [8, 7]
```

Partitions of sizes 2 and 2:

```text
1 + 1 = 2 comparisons
```

So the total comparisons per level are not always exactly `n - 1`.

But they are **at most proportional to n**.

The important pattern is:

- each partition scans its own subarray once
- the subarrays at one level do not overlap
- so the total work across one level is at most `O(n)`

---

### Number of Levels

In the best and average case, quick sort splits the array roughly in half each time:

```text
n → n/2 → n/4 → n/8 → ... → 1
```

So the number of levels is about:

```text
log2(n)
```

---

### Total Work

Now combine the two facts:

- work per level = O(n)
- number of levels = O(log n)

So the total work is:

```text
O(n log n)
```

---

### Best and Worst Case

### Best / Average Case

If partitions are reasonably balanced, quick sort has:

```text
Best Case Time Complexity: O(n log n)
Average Case Time Complexity: O(n log n)
```

### Worst Case

If the pivot is always the smallest or largest element, the partitions become very unbalanced:

```text
n → n - 1 → n - 2 → ...
```

That creates about `n` levels of recursion.

Since each level still does up to `O(n)` work, the total becomes:

```text
Worst Case Time Complexity: O(n^2)
```

---

### Final Intuition

A simple way to remember it is:

Quick sort does partitioning work across each level, and the total work on one level is at most proportional to `n`.

If the recursion tree stays balanced, there are about `log(n)` levels.

So:

```text
O(n log n)
```

If the tree becomes very unbalanced, there can be about `n` levels.

So:

```text
O(n^2)
```

---

## Space Complexity

Quick sort is **in-place** because it does not create extra arrays for sorting.

However, it still uses recursion.

So the space depends on recursion depth:

```text
Best / Average Case: O(log n)
Worst Case: O(n)
```

---

## Strengths of Quick Sort

- Very fast in practice
- In-place
- Good average-case performance
- Very widely used

---

## Weaknesses of Quick Sort

- Worst case is O(n^2)
- Performance depends on pivot choice
- Recursive depth can become large in bad cases

---


# Counting Sort

## What is Counting Sort?

**Counting sort** is a **non-comparison** sorting algorithm.

Instead of comparing elements like insertion sort, merge sort, or quick sort, it counts how many times each value appears, then reconstructs the sorted array.

---

## How Counting Sort Works

1. Find the maximum value in the array
2. Create a counts array of size `(max + 1)`
3. Count how many times each value appears
4. Rebuild the original array using those counts

---

## Example

```text
[7, 3, 2, 4, 5, 1, 2, 3]
```

Maximum value:

```text
7
```

After counting:

```text
[0, 1, 2, 2, 1, 1, 0, 1]
```

Rebuilding:

```text
[1, 2, 2, 3, 3, 4, 5, 7]
```

---

## Python Implementation

```python
def counting_sort(arr):
    maxx = max(arr)
    counts = [0] * (maxx + 1)

    for x in arr:
        counts[x] += 1

    i = 0
    for c in range(maxx + 1):
        while counts[c] > 0:
            arr[i] = c
            i += 1
            counts[c] -= 1
```

---

## How the Code Works

Suppose:

```text
arr = [7, 3, 2, 4, 5, 1, 2, 3]
```

### Step 1: Find the Maximum Value

```python
maxx = max(arr)
```

Here:

```text
maxx = 7
```

We use this to determine how many buckets we need.

Since the values go from `0` to `7`, we need 8 positions in the counts array.

---

### Step 2: Create the Counts Array

```python
counts = [0] * (maxx + 1)
```

So we get:

```text
counts = [0, 0, 0, 0, 0, 0, 0, 0]
```

Each index represents a value:

```text
counts[0] -> number of 0s
counts[1] -> number of 1s
counts[2] -> number of 2s
...
counts[7] -> number of 7s
```

---

### Step 3: Count Each Value

Now we loop through the input array:

```python
for x in arr:
    counts[x] += 1
```

Process each value:

```text
Read 7 -> counts[7] += 1
[0, 0, 0, 0, 0, 0, 0, 1]

Read 3 -> counts[3] += 1
[0, 0, 0, 1, 0, 0, 0, 1]

Read 2 -> counts[2] += 1
[0, 0, 1, 1, 0, 0, 0, 1]

Read 4 -> counts[4] += 1
[0, 0, 1, 1, 1, 0, 0, 1]

Read 5 -> counts[5] += 1
[0, 0, 1, 1, 1, 1, 0, 1]

Read 1 -> counts[1] += 1
[0, 1, 1, 1, 1, 1, 0, 1]

Read 2 -> counts[2] += 1
[0, 1, 2, 1, 1, 1, 0, 1]

Read 3 -> counts[3] += 1
[0, 1, 2, 2, 1, 1, 0, 1]
```

At the end, the counts array tells us exactly how many times each value appears.

---

### Step 4: Rebuild the Array

Now we walk through the counts array from left to right:

```python
i = 0
for c in range(maxx + 1):
    while counts[c] > 0:
        arr[i] = c
        i += 1
        counts[c] -= 1
```

This means:

- if `counts[0] = 0`, write no 0s
- if `counts[1] = 1`, write one 1
- if `counts[2] = 2`, write two 2s
- if `counts[3] = 2`, write two 3s
- and so on

Rebuild process:

```text
write 1  -> [1, _, _, _, _, _, _, _]
write 2  -> [1, 2, _, _, _, _, _, _]
write 2  -> [1, 2, 2, _, _, _, _, _]
write 3  -> [1, 2, 2, 3, _, _, _, _]
write 3  -> [1, 2, 2, 3, 3, _, _, _]
write 4  -> [1, 2, 2, 3, 3, 4, _, _]
write 5  -> [1, 2, 2, 3, 3, 4, 5, _]
write 7  -> [1, 2, 2, 3, 3, 4, 5, 7]
```

Final result:

```text
[1, 2, 2, 3, 3, 4, 5, 7]
```

---

## Key Idea

The value of each element is used as an index into the counts array.

That means counting sort does not need to compare elements to figure out which one is smaller.

Instead, it records how many of each value exists, then writes them back in order.

---

## Time Complexity

Let:

- `n` = number of elements in the input array
- `k` = number of possible values, from `0` to `maxx`

### Counting Step

```python
for x in arr:
    counts[x] += 1
```

This loop visits each element once.

So the counting step takes:

```text
O(n)
```

---

### Rebuild Step

```python
for c in range(maxx + 1):
    while counts[c] > 0:
        arr[i] = c
```

There are two parts to this work:

1. We loop over all possible values from `0` to `maxx`
   - that is `k` buckets

2. Across all buckets, we write each element back exactly once
   - that is `n` total writes

So the rebuild step takes:

```text
O(n + k)
```

---

### Total Time

Combine both steps:

- counting = `O(n)`
- rebuilding = `O(n + k)`

So the total time complexity is:

```text
O(n + k)
```

This is very fast when `k` is small.

But if `k` is very large, the algorithm loses its advantage.

---

## Space Complexity

Counting sort creates an extra counts array:

```python
counts = [0] * (maxx + 1)
```

That array has one slot for every possible value from `0` to `maxx`.

So the extra space used is:

```text
O(k)
```

The original array is sorted in place, but the counts array is still extra memory.

---

## Limitation

Counting sort requires a bucket for every value from `0` to `max(arr)`.

If the maximum value is large, the counts array becomes very large,
even if the input size is small.

Because of this, counting sort is only practical when:

- values are non-negative integers
- the range of values is small

In most real-world cases, values are large or widely spread out,
so this algorithm is rarely used compared to algorithms like quick sort.

---

# Comparing Insertion Sort, Merge Sort, Quick Sort, and Counting Sort

## Main Difference in Strategy

### Insertion Sort
Builds one sorted portion gradually.

```text
sorted | unsorted
```

Each pass inserts one new element into the sorted side.

### Merge Sort
Breaks the array apart, sorts the pieces, then merges them back together.

```text
split -> split -> split
merge -> merge -> merge
```

### Quick Sort
Picks a pivot, partitions the array around it, then recursively sorts the two sides.

```text
partition -> partition -> partition
```

### Counting Sort
Counts how many times each value appears, then rebuilds the array in sorted order.

```text
count -> count -> rebuild
```

---

## Intuition

### Insertion Sort feels like:
Sorting playing cards in your hand.

You keep one portion ordered and insert each new card where it belongs.

### Merge Sort feels like:
Breaking a pile into smaller piles, sorting those small piles, then combining them.

### Quick Sort feels like:
Picking one value, putting it where it belongs, then doing the same thing to the left and right parts.

### Counting Sort feels like:
Counting how many copies of each value you have, then writing them back in order.

---

## Complexity Comparison

| Metric | Insertion Sort | Merge Sort | Quick Sort | Counting Sort |
|------|------|------|------|------|
| Worst Case Time | O(n^2) | O(n log n) | O(n^2) | O(n + k) |
| Best Case Time | O(n) | O(n log n) | O(n log n) | O(n + k) |
| Average Case Time | O(n^2) | O(n log n) | O(n log n) | O(n + k) |
| Space | O(1) | O(n) | O(log n) avg | O(k) |
| In-place | Yes | No (in this version) | Yes | No |

---

## When to Use Each One

### Insertion Sort
Use when:

- the input is small
- the array is already nearly sorted
- you want a simple in-place algorithm
- you are learning basic sorting ideas

### Merge Sort
Use when:

- the input is large
- you want consistently good runtime
- O(n log n) performance matters more than extra memory
- you want to practice divide-and-conquer recursion

### Quick Sort
Use when:

- you want a fast in-place algorithm
- average-case performance matters
- you are comfortable with recursion and partitioning
- memory usage should stay low

### Counting Sort
Use when:

- values are non-negative integers
- the range of values is small
- you want very fast sorting for that special case
- extra memory for the counts array is acceptable

---

# Final Summary

Insertion sort, merge sort, quick sort, and counting sort all sort arrays, but they approach the problem very differently.

## Insertion Sort
- Builds a sorted portion one element at a time
- Simple and intuitive
- Good for small or nearly sorted inputs
- Worst case O(n^2)
- Space O(1)

## Merge Sort
- Splits the problem into smaller halves
- Sorts recursively
- Merges sorted halves
- Much faster on large inputs
- Time O(n log n)
- Space O(n)

## Quick Sort
- Partitions the array around a pivot
- Sorts recursively
- Usually very fast in practice
- Average time O(n log n)
- Worst case O(n^2)
- Space O(log n) average

## Counting Sort
- Counts how many times each value appears
- Rebuilds the array from those counts
- Time O(n + k)
- Space O(k)
- Very fast when the value range is small
- Rarely practical when values are large or widely spread out

If you want a simple algorithm that is easy to trace by hand, insertion sort is often the better starting point.

If you want consistently good runtime, merge sort is a strong choice.

If you want a fast in-place algorithm with very good average performance, quick sort is often the better choice.

If the values are non-negative integers in a small range, counting sort can be very efficient.
