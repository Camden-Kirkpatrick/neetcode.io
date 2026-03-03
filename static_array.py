class MyArray:
    """
    A fixed-capacity (static) array implementation.

    This class simulates how arrays work in lower-level languages:
    - Memory is preallocated.
    - Capacity is fixed.
    - Logical size (length) is tracked separately.
    - Insertions require shifting.
    - Deletions require shifting.
    """

    def __init__(self, capacity):
        """
        Initialize the array.

        Algorithm:
        1. Store the maximum capacity.
        2. Set logical length to 0.
        3. Preallocate a contiguous block of memory using a list of size `capacity`.
        4. Fill all slots with None to represent unused memory.
        """
        self.capacity = capacity
        self.length = 0
        self.arr = [None] * capacity
        print("array created")

    def is_full(self):
        """
        Check whether the array has reached capacity.

        Algorithm:
        Compare logical length with maximum capacity.

        Time Complexity: O(1)
        """
        return self.length == self.capacity

    def is_empty(self):
        """
        Check whether the array contains no elements.

        Algorithm:
        If logical length is 0, the array is empty.

        Time Complexity: O(1)
        """
        return self.length == 0

    def add(self, value, i=None):
        """
        Insert a value at a given index (default: end of array).

        Algorithm:
        1. If no index is provided, use current length (append behavior).
        2. If array is full, stop.
        3. Assign value to index.
        4. Increment logical length.

        Time Complexity: O(1)
        """
        if i is None:
            i = self.length

        if self.is_full():
            print("Can't add any more elements to the array")
            return

        self.arr[i] = value
        print(value, "was added to the array")
        self.length += 1

    def print_array(self):
        """
        Print the logical contents of the array.

        Algorithm:
        Iterate from index 0 up to logical length,
        ignoring unused capacity slots.

        Time Complexity: O(n)
        """
        print("Array: ", end="")
        for i in range(self.length):
            print(self.arr[i], end=" ")
        print()

    def insert_at(self, index, value):
        """
        Insert a value at a specific index.

        Algorithm:
        1. Validate index (0 ≤ index ≤ length).
        2. Ensure array is not full.
        3. Shift elements right starting from the end down to index.
           (Work backwards to avoid overwriting data.)
        4. Insert value at index.
        5. Increment logical length.

        Time Complexity: O(n)
        """
        if index < 0 or index > self.length:
            print("Invalid index")
            return

        if self.is_full():
            print("Can't add any more elements to the array")
            return

        for i in range(self.length - 1, index - 1, -1):
            self.arr[i + 1] = self.arr[i]

        self.add(value, index)

    def insert_start(self, value):
        """
        Insert a value at the beginning of the array.

        Algorithm:
        1. Ensure array is not full.
        2. Shift all elements right by one position.
        3. Insert new value at index 0.
        4. Increment logical length.

        Time Complexity: O(n)
        """
        if self.is_full():
            print("Can't add any more elements to the array")
            return

        for i in range(self.length - 1, -1, -1):
            self.arr[i + 1] = self.arr[i]

        self.add(value, 0)

    def insert_end(self, value):
        """
        Insert a value at the end of the array.

        Algorithm:
        Equivalent to append.
        Insert at index = current length.

        Time Complexity: O(1)
        """
        self.add(value)

    def delete_at(self, index):
        """
        Delete an element at a specific index.

        Algorithm:
        1. Validate index (0 ≤ index < length).
        2. Ensure array is not empty.
        3. Shift elements left starting from index.
        4. Decrement logical length.
        5. Clear the freed slot by setting it to None.

        Time Complexity: O(n)
        """
        if index < 0 or index >= self.length:
            print("Invalid index")
            return

        if self.is_empty():
            print("Can't delete from empty array")
            return

        for i in range(index, self.length - 1):
            self.arr[i] = self.arr[i + 1]

        self.length -= 1
        self.arr[self.length] = None

    def delete_start(self):
        """
        Delete the first element of the array.

        Algorithm:
        1. Ensure array is not empty.
        2. Shift all elements left by one.
        3. Decrement logical length.
        4. Clear last slot.

        Time Complexity: O(n)
        """
        if self.is_empty():
            print("Can't delete from empty array")
            return

        for i in range(0, self.length - 1):
            self.arr[i] = self.arr[i + 1]

        self.length -= 1
        self.arr[self.length] = None

    def delete_end(self):
        """
        Delete the last element of the array.

        Algorithm:
        1. Ensure array is not empty.
        2. Set last logical element to None.
        3. Decrement logical length.

        Time Complexity: O(1)
        """
        if self.is_empty():
            print("Can't delete from empty array")
            return

        self.arr[self.length - 1] = None
        self.length -= 1



arr1 = MyArray(2)
arr1.add(20)
arr1.add(74)
# arr1.add(99) Array is full
arr1.print_array()

print()

arr2 = MyArray(5)
arr2.add(99)
arr2.add(24)
arr2.print_array()
print()

arr2.insert_at(1, 10)
print("After inserting '10' in the middle:")
arr2.print_array()
print()

arr2.insert_start(-16)
print("After inserting '-16' at the start:")
arr2.print_array()
print()

arr2.insert_end(0)
print("After inserting '0' at the end:")
arr2.print_array()
print()

arr2.delete_at(2)
print("After removing the third element:")
arr2.print_array()
print()

arr2.delete_start()
print("After removing the first element:")
arr2.print_array()
print()

arr2.delete_end()
print("After removing the last element:")
arr2.print_array()
print()
