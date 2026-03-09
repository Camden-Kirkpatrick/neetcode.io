# Data Structures and Memory

Data structures are ways of **organizing and managing data in RAM** so that it can be accessed and modified efficiently.

Understanding how memory works helps explain **why different data structures behave the way they do**.

---

# How RAM Works

RAM (Random Access Memory) is a large block of memory made up of **bits**.

A **bit** is a single binary value:

```
0 or 1
```

Eight bits form a **byte**.

```
8 bits = 1 byte
```

A **byte is the smallest addressable unit of memory**.

---

# Common Data Sizes

Different data types require different numbers of bytes.

Typical sizes:

| Type | Size |
|-----|------|
| char | 1 byte (8 bits) |
| int | 4 bytes (32 bits) |

Examples:

- Integers like `50`, `0`, and `-10` typically use **4 bytes**
- Characters like `'c'`, `'&'`, and `'7'` typically use **1 byte**

Single quotes indicate a **character literal**.

```
'c'
```

This means the value represents the character’s **numeric encoding** (such as ASCII), not a number used for arithmetic.

---

# Memory Addresses

Every byte in RAM has a **unique address**.

An address tells the CPU **exactly where data is stored**.

Addresses look something like:

```
0xb678add09f
```

Memory addresses are written in **hexadecimal (base 16)**.

Hexadecimal uses:

```
0 1 2 3 4 5 6 7 8 9 A B C D E F
```

Hexadecimal is useful because it maps cleanly to binary:

```
1 hex digit = 4 bits
```

---

# Hexadecimal Example

Consider the hexadecimal value:

```
FF
```

Each hex digit represents **4 bits**.

```
F  = 1111
FF = 11111111
```

In decimal:

```
11111111 (binary) = 255 (decimal)
```

255 is the **largest value that can be stored in one byte**.

Therefore:

```
0xFF (hex) = 255 (decimal) = 11111111 (binary)
```

---

# Example: Variable in Memory

Consider the variable:

```
int x = 10;
```

Suppose the variable is stored starting at memory address:

```
0x73a11ff9c0
```

Since an `int` typically uses **4 bytes**, the variable occupies:

```
0x73a11ff9c0
0x73a11ff9c1
0x73a11ff9c2
0x73a11ff9c3
```

Memory addresses increase by **1 byte at a time**.

The next available address would be:

```
0x73a11ff9c4
```

---

# Why This Matters for Data Structures

Data structures determine **how we organize data in memory**.

They control:

- how data is stored
- how data is accessed
- how efficiently operations can be performed

Understanding memory layout is the foundation for understanding:

- arrays
- linked lists
- stacks
- queues
- trees
- hash tables