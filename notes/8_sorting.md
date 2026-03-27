# Sorting: Insertion Sort and Merge Sort

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
|   |   \\
|   |    merge -> [3, 8]
|   |
|   +-- merge_sort([7, 4])
|   |   |
|   |   +-- merge_sort([7])
|   |   +-- merge_sort([4])
|   |   \\
|   |    merge -> [4, 7]
|   |
|   \\
|    merge -> [3, 4, 7, 8]
|
+-- merge_sort([2, 6, 5, 1])
|   |
|   +-- merge_sort([2, 6])
|   |   |
|   |   +-- merge_sort([2])
|   |   +-- merge_sort([6])
|   |   \\
|   |    merge -> [2, 6]
|   |
|   +-- merge_sort([5, 1])
|   |   |
|   |   +-- merge_sort([5])
|   |   +-- merge_sort([1])
|   |   \\
|   |    merge -> [1, 5]
|   |
|   \\
|    merge -> [1, 2, 5, 6]
|
\\
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

# Comparing Insertion Sort and Merge Sort

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

---

## Intuition

### Insertion Sort feels like:
Sorting playing cards in your hand.

You keep one portion ordered and insert each new card where it belongs.

### Merge Sort feels like:
Breaking a pile into smaller piles, sorting those small piles, then combining them.

---

## Complexity Comparison

| Metric | Insertion Sort | Merge Sort |
|------|------|------|
| Worst Case Time | O(n^2) | O(n log n) |
| Best Case Time | O(n) | O(n log n) |
| Space | O(1) | O(n) |
| In-place | Yes | No (in this version) |

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

---

# Final Summary

Insertion sort and merge sort both sort arrays, but they approach the problem very differently.

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

If you want a simple algorithm that is easy to trace by hand, insertion sort is often the better starting point.

If you want better performance on larger arrays, merge sort is usually the better choice.