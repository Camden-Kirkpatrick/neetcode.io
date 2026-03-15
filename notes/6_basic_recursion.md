# Recursion

## What is Recursion?

**Recursion** is a programming technique where a function **calls itself** in order to solve a problem.

Instead of solving a large problem all at once, recursion breaks the problem into **smaller versions of the same problem**.

Every recursive function has two important parts:

1. **Base Case**
   - The condition where the recursion **stops**.
   - Prevents infinite recursion.

2. **Recursive Case**
   - The part where the function **calls itself with a smaller input**.

Example structure:

```
function solve(problem):
    if base_case:
        return answer
    else:
        return solve(smaller_problem)
```

---

# Example: Factorial

The **factorial** of a number `n` is defined as:

```
n! = n × (n-1) × (n-2) × ... × 1
```

Examples:

```
5! = 5 × 4 × 3 × 2 × 1 = 120
4! = 4 × 3 × 2 × 1 = 24
3! = 3 × 2 × 1 = 6
```

---

# Recursive Definition of Factorial

Factorial can be defined recursively as:

```
n! = n × (n-1)!
```

Base case:

```
0! = 1
1! = 1
```

---

# Python Implementation

```
def factorial(n):
    if n == 0 or n == 1:      # Base case
        return 1
    return n * factorial(n-1) # Recursive case
```

Example call:

```
factorial(5)
```

---

# How Recursion Works (Going Down the Call Stack)

When `factorial(5)` starts, each function call cannot finish yet.

Why?

Because each call is waiting for the result of the next smaller factorial.

```
factorial(5)
= 5 * factorial(4)
      needs factorial(4) first

factorial(4)
= 4 * factorial(3)
      needs factorial(3) first

factorial(3)
= 3 * factorial(2)
      needs factorial(2) first

factorial(2)
= 2 * factorial(1)
      needs factorial(1) first

factorial(1)
= 1   <-- base case reached
```

So the recursion goes **downward** until it finally reaches a call that can return immediately.

---

# Better View of the Call Stack

As the recursive calls happen, each unfinished call is placed on the call stack.

```
Step 1
Top
-----------------
factorial(5)
-----------------
Bottom

Step 2
Top
-----------------
factorial(4)   <- currently running
factorial(5)   <- waiting for factorial(4)
-----------------
Bottom

Step 3
Top
-----------------
factorial(3)   <- currently running
factorial(4)   <- waiting
factorial(5)   <- waiting
-----------------
Bottom

Step 4
Top
-----------------
factorial(2)   <- currently running
factorial(3)   <- waiting
factorial(4)   <- waiting
factorial(5)   <- waiting
-----------------
Bottom

Step 5
Top
-----------------
factorial(1)   <- base case
factorial(2)   <- waiting
factorial(3)   <- waiting
factorial(4)   <- waiting
factorial(5)   <- waiting
-----------------
Bottom
```

At this point, we cannot go deeper.

Now the recursion starts going **back up**.

---

# What Happens at the Base Case?

This is the part that usually confuses people.

When we reach:

```
factorial(1)
```

this call does **not** make another recursive call.

It immediately returns:

```
1
```

That returned value is sent back to the function that was waiting for it.

So this:

```
factorial(2)
= 2 * factorial(1)
```

now becomes:

```
factorial(2)
= 2 * 1
= 2
```

Then `factorial(2)` returns `2` to `factorial(3)`.

---

# Unwinding: Going Back Up the Call Stack

Once the base case returns, the stack starts to **unwind**.

That means each waiting function call now has the value it needed, so it can finish its multiplication and return upward.

## Visual Unwinding

```
Base case reached:

factorial(1) returns 1
```

Now go back up one level:

```
factorial(2)
= 2 * factorial(1)
= 2 * 1
= 2
returns 2
```

Go back up again:

```
factorial(3)
= 3 * factorial(2)
= 3 * 2
= 6
returns 6
```

Go back up again:

```
factorial(4)
= 4 * factorial(3)
= 4 * 6
= 24
returns 24
```

Final step:

```
factorial(5)
= 5 * factorial(4)
= 5 * 24
= 120
returns 120
```

---

# Stack Unwinding Diagram

This shows both the return value and which call gets removed from the stack.

```
Top
-----------------
factorial(1)   <- returns 1
factorial(2)   <- waiting for 1
factorial(3)   <- waiting
factorial(4)   <- waiting
factorial(5)   <- waiting
-----------------
Bottom
```

After `factorial(1)` returns:

```
Top
-----------------
factorial(2)   <- computes 2 * 1 = 2, returns 2
factorial(3)   <- waiting for 2
factorial(4)   <- waiting
factorial(5)   <- waiting
-----------------
Bottom
```

After `factorial(2)` returns:

```
Top
-----------------
factorial(3)   <- computes 3 * 2 = 6, returns 6
factorial(4)   <- waiting for 6
factorial(5)   <- waiting
-----------------
Bottom
```

After `factorial(3)` returns:

```
Top
-----------------
factorial(4)   <- computes 4 * 6 = 24, returns 24
factorial(5)   <- waiting for 24
-----------------
Bottom
```

After `factorial(4)` returns:

```
Top
-----------------
factorial(5)   <- computes 5 * 24 = 120, returns 120
-----------------
Bottom
```

After `factorial(5)` returns:

```
Stack is empty
Final answer: 120
```

---

# One Full Picture

Sometimes it helps to see the whole process in one diagram.

```
GOING DOWN                    GOING BACK UP
-----------                   ----------------
factorial(5)                  factorial(5) = 5 * 24 = 120
  waits for factorial(4)   <- returns 120

factorial(4)                  factorial(4) = 4 * 6 = 24
  waits for factorial(3)   <- returns 24

factorial(3)                  factorial(3) = 3 * 2 = 6
  waits for factorial(2)   <- returns 6

factorial(2)                  factorial(2) = 2 * 1 = 2
  waits for factorial(1)   <- returns 2

factorial(1)                  base case returns 1
```

The left side shows the calls being made.

The right side shows the answers coming back.

---

# Recursion Decision Tree

Even though factorial only has **one recursive branch**, we can still visualize the calls as a chain:

```
factorial(5)
    |
factorial(4)
    |
factorial(3)
    |
factorial(2)
    |
factorial(1)
```

Another simple view:

```
5!
|
4!
|
3!
|
2!
|
1!
```

Each level represents **one recursive call**.

---

# Key Idea to Remember

A recursive call has two phases:

1. **Going down**
   - More function calls are created.
   - Each call pauses and waits.

2. **Coming back up**
   - The base case returns a real value.
   - Each waiting call resumes, finishes its work, and returns.

For factorial:

- Going down: build the multiplications
- Coming back up: actually perform the multiplications

You can think of it like this:

```
factorial(5)
= 5 * factorial(4)
= 5 * (4 * factorial(3))
= 5 * (4 * (3 * factorial(2)))
= 5 * (4 * (3 * (2 * factorial(1))))
= 5 * (4 * (3 * (2 * 1)))
= 5 * (4 * (3 * 2))
= 5 * (4 * 6)
= 5 * 24
= 120
```

---

# Time Complexity

For factorial recursion:

```
factorial(n) calls factorial(n-1)
```

So the function executes **once per level**.

```
factorial(5)
factorial(4)
factorial(3)
factorial(2)
factorial(1)
```

Number of calls:

```
n
```

Therefore:

```
Time Complexity = O(n)
```

---

# Space Complexity

Recursion uses the **call stack**.

At maximum depth, the stack contains:

```
factorial(n)
factorial(n-1)
...
factorial(1)
```

That means:

```
Space Complexity = O(n)
```

because `n` stack frames are stored.

---

# Summary

Recursion works by:

1. Defining a **base case** that stops the recursion
2. Calling the function again with a **smaller input**
3. Using the **call stack** to remember unfinished work
4. Resolving the calls in reverse order once the base case is reached

For factorial:

```
factorial(n) = n * factorial(n-1)
```

Complexities:

| Metric | Complexity |
|------|------|
| Time | O(n) |
| Space | O(n) |
