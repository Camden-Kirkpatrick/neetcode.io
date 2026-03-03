### Data Structures



Data structures are how we organize and manage data in RAM.





### How RAM Works



RAM is one long, contiguous block of memory made up of 1s and 0s (bits).



8 bits = 1 byte  

A byte is the smallest addressable unit of memory.



Common data sizes:

\- char → 1 byte (8 bits)

\- int  → usually 4 bytes (32 bits)



Examples:

\- Integers like 50, 0, and -10 typically use 4 bytes.

\- Characters like 'c', '\&', and '7' typically use 1 byte.



Single quotes ('c') indicate a character literal.  

This means the value represents the character’s numeric encoding (such as ASCII), not a number used for arithmetic.





### Memory Addresses



Every byte in RAM has a unique address.



An address tells the CPU exactly where a piece of data is stored.



Addresses look something like:

0xb678add09f



Addresses are written in hexadecimal (base 16), which uses:

0–9 and a–f



Hexadecimal is used because it maps cleanly to binary:

1 hex digit = 4 bits





Hexadecimal Example



FF represents one byte in hexadecimal.



Each hex digit represents 4 bits:

F  = 1111

FF = 1111 1111



In decimal:

11111111 (binary) = 255 (decimal)



255 is the largest value that can be stored in one byte.



So:

0xFF (hex) = 255 (decimal) = 11111111 (binary)





Example in Memory



int x = 10;



Suppose x is stored at memory address:

0x73a11ff9c0



Memory addresses increase by 1 for each byte.



Since an int takes 4 bytes, it occupies:



0x73a11ff9c0

0x73a11ff9c1

0x73a11ff9c2

0x73a11ff9c3



The next available memory location would be:



0x73a11ff9c4



Understanding how memory works is the foundation for understanding data structures.

They define how we arrange and access data efficiently inside this memory.

