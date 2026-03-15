# Fibonacci

The **Fibonacci sequence** is a sequence of numbers where each number is the sum of the two previous numbers.

Starting values:

```text
fib(0) = 0
fib(1) = 1
```

Recursive definition:

```text
fib(n) = fib(n-1) + fib(n-2)
```

Examples:

```text
fib(0) = 0
fib(1) = 1
fib(2) = 1
fib(3) = 2
fib(4) = 3
fib(5) = 5
```

Sequence:

```text
0, 1, 1, 2, 3, 5, 8, ...
```

---

# Python Implementation

```python
def fib_rec(n):
    if n <= 1:                  # Base cases
        return n
    return fib_rec(n - 1) + fib_rec(n - 2)
```

Example call:

```python
fib_rec(5)
```

---

# Why Fibonacci Recursion Feels Different From Factorial

Factorial recursion makes **one recursive call** each time:

```text
factorial(n) -> factorial(n-1)
```

So factorial creates a **single chain** of calls.

Fibonacci recursion makes **two recursive calls** each time:

```text
fib(n) -> fib(n-1) and fib(n-2)
```

So Fibonacci creates a **branching tree** of calls.

That branching is the main reason Fibonacci recursion is harder to visualize.

---

# How Recursion Works for fib(5)

When `fib(5)` starts, it cannot return immediately.

Why?

Because it needs the results of:

```text
fib(4) and fib(3)
```

Then `fib(4)` cannot return immediately either, because it needs:

```text
fib(3) and fib(2)
```

And so on.

The recursion keeps expanding until it reaches base cases:

```text
fib(1) = 1
fib(0) = 0
```

---

# Full Recursion Tree for fib(5)

This tree shows **every recursive call** made by `fib(5)`.

```text
fib(5)
├── fib(4)
│   ├── fib(3)
│   │   ├── fib(2)
│   │   │   ├── fib(1) = 1
│   │   │   └── fib(0) = 0
│   │   └── fib(1) = 1
│   └── fib(2)
│       ├── fib(1) = 1
│       └── fib(0) = 0
└── fib(3)
    ├── fib(2)
    │   ├── fib(1) = 1
    │   └── fib(0) = 0
    └── fib(1) = 1
```

Notice that some calls appear more than once:

- `fib(3)` appears **2 times**
- `fib(2)` appears **3 times**
- `fib(1)` appears **5 times**
- `fib(0)` appears **3 times**

This repeated work is why naive recursive Fibonacci is inefficient.

---

# Better View: Tree With Return Values

Now here is the same tree, but this version also shows what each call returns.

```text
fib(5) = 5
├── fib(4) = 3
│   ├── fib(3) = 2
│   │   ├── fib(2) = 1
│   │   │   ├── fib(1) = 1
│   │   │   └── fib(0) = 0
│   │   └── fib(1) = 1
│   └── fib(2) = 1
│       ├── fib(1) = 1
│       └── fib(0) = 0
└── fib(3) = 2
    ├── fib(2) = 1
    │   ├── fib(1) = 1
    │   └── fib(0) = 0
    └── fib(1) = 1
```

This is the full story of `fib(5)`:

```text
fib(5) = fib(4) + fib(3)
       = 3 + 2
       = 5
```

---

# Going Down the Tree

The recursion first goes **downward**, creating more function calls.

One possible path downward is:

```text
fib(5)
-> fib(4)
-> fib(3)
-> fib(2)
-> fib(1)
```

At `fib(1)`, we hit a base case:

```text
fib(1) = 1
```

So that call returns immediately.

Then the recursion backs up one step and explores the other branch:

```text
fib(0) = 0
```

Then `fib(2)` finally has both values it needs.

---

# What Happens at fib(2)?

This is the smallest non-base Fibonacci call.

```text
fib(2)
= fib(1) + fib(0)
= 1 + 0
= 1
```

That makes `fib(2)` a good place to focus, because it is the first point where the recursion starts combining answers.

Diagram:

```text
fib(2)
├── fib(1) = 1
└── fib(0) = 0

fib(2) = 1 + 0 = 1
```

---

# What Happens at fib(3)?

Once one `fib(2)` has returned, the parent call can continue.

```text
fib(3)
= fib(2) + fib(1)
= 1 + 1
= 2
```

Diagram:

```text
fib(3)
├── fib(2) = 1
└── fib(1) = 1

fib(3) = 1 + 1 = 2
```

---

# What Happens at fib(4)?

Now go one level higher.

```text
fib(4)
= fib(3) + fib(2)
= 2 + 1
= 3
```

Diagram:

```text
fib(4)
├── fib(3) = 2
└── fib(2) = 1

fib(4) = 2 + 1 = 3
```

---

# Final Step: fib(5)

Finally, the original call gets the two values it was waiting for.

```text
fib(5)
= fib(4) + fib(3)
= 3 + 2
= 5
```

Diagram:

```text
fib(5)
├── fib(4) = 3
└── fib(3) = 2

fib(5) = 3 + 2 = 5
```

---

# Layer-by-Layer View of the Tree

Sometimes it helps to see the recursion tree by levels.

```text
Level 0:
fib(5)

Level 1:
fib(4)          fib(3)

Level 2:
fib(3)   fib(2) fib(2)   fib(1)

Level 3:
fib(2) fib(1) fib(1) fib(0) fib(1) fib(0)

Level 4:
fib(1) fib(0)
```

This makes the repeated calls easier to spot.

For example:

- `fib(3)` appears at Level 2 more than once
- `fib(2)` appears several times
- base cases appear many times

---

# Step-by-Step Evaluation of fib(5)

This shows the recursion tree being resolved from the bottom up.

## Step 1: Resolve all base cases

```text
fib(1) = 1
fib(0) = 0
```

## Step 2: Resolve all fib(2) calls

```text
fib(2)
= fib(1) + fib(0)
= 1 + 0
= 1
```

There are **three** separate `fib(2)` calls in the tree, and each one evaluates to `1`.

## Step 3: Resolve all fib(3) calls

```text
fib(3)
= fib(2) + fib(1)
= 1 + 1
= 2
```

There are **two** separate `fib(3)` calls in the tree, and each one evaluates to `2`.

## Step 4: Resolve fib(4)

```text
fib(4)
= fib(3) + fib(2)
= 2 + 1
= 3
```

## Step 5: Resolve fib(5)

```text
fib(5)
= fib(4) + fib(3)
= 3 + 2
= 5
```

---

# Bottom-Up Return Diagram

This diagram focuses on the values coming back up.

```text
Base cases:
fib(1) = 1
fib(0) = 0

Then:
fib(2) = 1
fib(2) = 1
fib(2) = 1

Then:
fib(3) = 2
fib(3) = 2

Then:
fib(4) = 3

Then:
fib(5) = 5
```

A cleaner grouped view:

```text
Leaves:
fib(1), fib(0), fib(1), fib(1), fib(0), fib(1), fib(0), fib(1)

Combine upward:
fib(2), fib(3), fib(2), fib(4), fib(2), fib(3), fib(5)
```

---

# One Full Picture

This view puts the **going down** and **coming back up** ideas side by side.

```text
GOING DOWN THE TREE                COMING BACK UP THE TREE
--------------------              -------------------------
fib(5)                            fib(5) = fib(4) + fib(3)
  needs fib(4), fib(3)              = 3 + 2
                                     = 5

fib(4)                            fib(4) = fib(3) + fib(2)
  needs fib(3), fib(2)              = 2 + 1
                                     = 3

fib(3)                            fib(3) = fib(2) + fib(1)
  needs fib(2), fib(1)              = 1 + 1
                                     = 2

fib(2)                            fib(2) = fib(1) + fib(0)
  needs fib(1), fib(0)              = 1 + 0
                                     = 1

fib(1), fib(0)                    base cases return immediately
```

The left side shows the calls being created.

The right side shows the answers being combined.

---

# Why Fibonacci Recursion Is Slow

The recursive definition is simple, but it repeats work.

Look at this part of the tree:

```text
fib(5)
├── fib(4)
│   └── fib(3)
└── fib(3)
```

`fib(3)` is solved more than once.

And inside those two `fib(3)` calls, `fib(2)` gets solved multiple times too.

So the recursion does not just go deep. It also goes **wide**.

That repeated branching makes the total number of calls grow quickly.

---

# Exact Calls Made by fib(5)

If you list every call in the tree, you get:

```text
fib(5)
fib(4)
fib(3)
fib(2)
fib(1)
fib(0)
fib(1)
fib(2)
fib(1)
fib(0)
fib(3)
fib(2)
fib(1)
fib(0)
fib(1)
```

That is **15 total calls** just to compute `fib(5)`.

Even though the final answer is only `5`, the function does much more work than it seems.

---

# Recursion Decision Tree

Fibonacci recursion is best visualized as a decision tree.

```text
fib(5)
├── fib(4)
│   ├── fib(3)
│   │   ├── fib(2)
│   │   │   ├── fib(1)
│   │   │   └── fib(0)
│   │   └── fib(1)
│   └── fib(2)
│       ├── fib(1)
│       └── fib(0)
└── fib(3)
    ├── fib(2)
    │   ├── fib(1)
    │   └── fib(0)
    └── fib(1)
```

Each node is a recursive call.

Each branch means:

```text
"To solve this Fibonacci number, solve these two smaller ones first."
```

---

# Key Idea to Remember

A Fibonacci recursive call has two phases:

1. **Going down**
   - More function calls are created
   - Each call splits into two smaller calls
   - This builds a recursion tree

2. **Coming back up**
   - Base cases return actual values
   - Parent calls add those values together
   - Answers move upward until the original call finishes

For Fibonacci:

- Going down: build the recursion tree
- Coming back up: add child results together

You can think of it like this:

```text
fib(5)
= fib(4) + fib(3)
= (fib(3) + fib(2)) + (fib(2) + fib(1))
= ((fib(2) + fib(1)) + (fib(1) + fib(0))) + ((fib(1) + fib(0)) + fib(1))
= ((1 + 1) + (1 + 0)) + ((1 + 0) + 1)
= (2 + 1) + (1 + 1)
= 3 + 2
= 5
```

---

# Time Complexity

The time complexity of naive recursive Fibonacci comes from the
number of recursive calls made.

Each call to:

fib(n)

creates two additional recursive calls:

fib(n-1)
fib(n-2)

This means the recursion expands into a binary recursion tree.

Example for fib(5):

fib(5)
├── fib(4)
│   ├── fib(3)
│   └── fib(2)
└── fib(3)
    ├── fib(2)
    └── fib(1)

The tree keeps expanding until it reaches base cases.

For fib(5) the total calls are:

fib(5)
fib(4)
fib(3)
fib(2)
fib(1)
fib(0)
fib(1)
fib(2)
fib(1)
fib(0)
fib(3)
fib(2)
fib(1)
fib(0)
fib(1)

This is **15 total calls** just to compute fib(5).

The number of calls grows roughly like this:

Level 0: 1 call
Level 1: 2 calls
Level 2: 4 calls
Level 3: 8 calls
Level 4: 16 calls

So the total number of calls grows approximately like:

2^n

Therefore:

Time Complexity = O(2^n)

This means the running time roughly doubles every time n increases by 1.

Example growth:

n = 5   → 15 calls
n = 10  → ~177 calls
n = 20  → ~21,891 calls
n = 30  → ~2,692,537 calls

This is why naive recursive Fibonacci becomes extremely slow for
larger values of n.


# Space Complexity

The space complexity comes from the recursion call stack.

Even though the recursion tree contains many calls, the program
does not store the entire tree in memory at once.

Instead, it only stores the current chain of recursive calls.

The deepest path in the recursion occurs when the program repeatedly
calls fib(n-1).

Example deepest path for fib(5):

fib(5)
fib(4)
fib(3)
fib(2)
fib(1)

This path contains 5 stack frames.

In general, the maximum recursion depth is:

n

Therefore:

Space Complexity = O(n)

because the call stack grows linearly with n.

For example:

fib(100)

could require up to 100 stack frames on the call stack.


# Important Distinction

It is important to distinguish between:

Total number of function calls

and

Maximum recursion depth.

For Fibonacci recursion:

Total calls      → O(2^n)
Recursion depth  → O(n)

The algorithm performs exponentially many calls,
but only one branch of the recursion tree exists on the call
stack at a time.

---

# Summary

Fibonacci recursion works by:

1. Defining **base cases**
   - `fib(0) = 0`
   - `fib(1) = 1`

2. Breaking the problem into **two smaller Fibonacci problems**
   - `fib(n) = fib(n-1) + fib(n-2)`

3. Building a **recursion tree**
   - Each node splits into two child calls

4. Combining results while returning upward
   - Child calls return values
   - Parent calls add them together

For `fib(5)`:

```text
fib(5)
= fib(4) + fib(3)
= 3 + 2
= 5
```

Complexities:

| Metric | Complexity |
|------|------|
| Time | O(2^n) |
| Space | O(n) |
