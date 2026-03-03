### Reading from an Array



int array\[3] = {1, 3, 5};



To read a value from the array, we access it using an index.



Example:

cout << array\[0];   // Output: 1



The number inside the square brackets (\[]) is the index.



Arrays use zero-based indexing:

array\[0] -> first element

array\[1] -> second element

array\[2] -> third element





#### Memory Layout and Address Calculation



Arrays are stored in contiguous memory (all elements are placed next to each other in RAM).



Suppose the address of the first element (array\[0]) is:

0x73a11ff9c0



Each int typically occupies 4 bytes of memory.



To calculate the address of any element, we use:



address of array\[i] = base\_address + (i × size\_of\_element)



Example: Find the address of array\[2]



array\[2] = 0x73a11ff9c0 + (2 × 4)

&nbsp;        = 0x73a11ff9c8



So array\[2] is stored at memory address 0x73a11ff9c8.



Because arrays are stored in contiguous memory, the computer does not need to search for elements.  

It can directly calculate the memory address using this formula.



This means accessing array\[2] and array\[2,000,000] takes the same amount of time.



RAM stands for "Random Access Memory."  

"Random access" means the CPU can jump directly to any memory address instantly.



Therefore, reading from an array takes constant time: O(1).





#### Fixed Size of Arrays



Arrays have a fixed size. Once created, they cannot grow or shrink.



Example:

int array\[3] = {1, 3, 5};



The operating system finds one continuous block of memory large enough to hold:



3 × sizeof(int) = 12 bytes



After that block is assigned, the memory immediately after it might belong to:

\- another variable

\- another array

\- another part of the program

\- even the operating system



If we tried to “just add one more element,” we might overwrite something important, causing:

\- undefined behavior

\- memory corruption

\- a crash



This is the biggest limitation of static arrays.





### Writing to an Array



int array\[3];



This allocates space for 3 integers, but does not specify values.



Depending on the programming language:

\- The array may be initialized to zeros

\- The array may contain garbage (uninitialized) values





You can declare an array in three common ways:



1\) Provide only the size:

int array\[3];

(May contain garbage values in C/C++ if not initialized)



2\) Provide only the data:

int array\[] = {4, 8, 0};

(The compiler determines the size automatically)



3\) Provide both size and data:

int array\[3] = {3, 4, 5};





If the declared size is larger than the number of initializers:



int array\[5] = {1, 2};



The remaining elements are automatically initialized to 0.



Result:

{1, 2, 0, 0, 0}





Writing (Assigning) to an Array



array\[0] = 5;



Like reading, writing to a specific index uses direct address calculation.



Therefore, writing to an array also takes constant time: O(1).







### Inserting into an Array (Assuming There Is Enough Space)



int array\[3] = {5, 6};   // array = {5, 6, ?}



Inserting at the end is easy:



array\[2] = 7;            // array = {5, 6, 7}



No elements need to be moved, so this operation is O(1).





Inserting at the Beginning



Suppose we want to insert 4 at the beginning.



We cannot do:

array\[0] = 4;    // This would overwrite 5



Instead, we must shift all existing elements one position to the right

to make space.



Original:

Index:  0   1

Value:  5   6



Shift elements right (start from the end to avoid overwriting):



array\[2] = array\[1];   // Move 6 to index 2

array\[1] = array\[0];   // Move 5 to index 1



Now:

Index:  0   1   2

Value:  5   5   6



Now we can insert 4:



array\[0] = 4;



Final result:

{4, 5, 6}



Because we may need to shift n elements, inserting at the beginning

is O(n). As the array grows, the number of shifts grows linearly.



### 

### Deleting from an Array



Suppose we have:

{3, 4, 5}



To delete 3 (the first element), we shift elements left:



array\[0] = array\[1];   // Move 4 to index 0

array\[1] = array\[2];   // Move 5 to index 1



Now the logical array is:

{4, 5}



Again, we had to shift elements, so deletion from the front is O(n).





Summary of Time Complexity



Read/Write i-th element:     O(1)

Insert/Remove at End:        O(1)

Insert/Remove at Front:      O(n)

Insert/Remove in Middle:     O(n)







