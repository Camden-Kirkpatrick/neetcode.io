# improved error handling in static_array.py

class DynamicArray:
    """
    A resizable (dynamic) array implementation.

    This class simulates how dynamic arrays work in lower-level languages:
    - Memory is preallocated.
    - Capacity grows when the array becomes full.
    - Logical size (length) is tracked separately.
    - Insertions may require shifting.
    - Deletions require shifting and clearing freed slots.
    """

    def __init__(self, capacity=2):
        """
        Initialize the dynamic array.

        Algorithm:
        1. Store the initial capacity.
        2. Set logical length to 0.
        3. Preallocate a list of size `capacity`.
        4. Fill all slots with None to represent unused memory.
        """
        if capacity < 1:
            raise ValueError("Capacity must be at least 1")

        self.capacity = capacity
        self.length = 0
        self.arr = [None] * capacity

    def size(self):
        """
        Return the logical number of elements stored.

        Algorithm:
        Return the current logical length.

        Time Complexity: O(1)
        """
        return self.length
    
    def __len__(self):
        """
        Equivalent to size().
        Allows "len()" syntax.
        """
        return self.length
    
    def get_capacity(self):
        """
        Return the current capacity of the underlying array.

        Algorithm:
        Return the current capacity.

        Time Complexity: O(1)
        """
        return self.capacity

    def is_full(self):
        """
        Check whether the array has reached capacity.

        Algorithm:
        Compare logical length with current capacity.

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
    
    def get(self, index):
        """
        Return the element at a specific index.

        Algorithm:
        1. Validate index (0 ≤ index < length).
        2. Return the value stored at that index.

        Time Complexity: O(1)
        """
        if index < 0 or index >= self.length:
            raise IndexError("Invalid index")
        
        return self.arr[index]
    
    def set(self, index, value):
        """
        Replace the element at a specific index.

        Algorithm:
        1. Validate index (0 ≤ index < length).
        2. Assign the new value to that index.

        Time Complexity: O(1)
        """
        if index < 0 or index >= self.length:
            raise IndexError("Invalid index")
        
        self.arr[index] = value

    def last(self):
        """
        Return the last logical element (top/end) without removing it.

        This method is not used internally by the DynamicArray itself.
        It exists mainly for external data structures (e.g., Stack)
        that need to read the final element without accessing the
        underlying array directly.

        Algorithm:
        1. If the array is empty, return None.
        2. Return the element at index (length - 1).

        """
        if self.is_empty():
            return None
        
        return self.arr[self.length - 1]

    def resize(self):
        """
        Double the capacity of the array.

        Algorithm:
        1. Create a new array with capacity = 2 * current capacity.
        2. Copy all logical elements from the old array into the new array.
        3. Replace the old array reference with the new array.
        4. Update capacity.

        Time Complexity: O(n)
        """
        new_capacity = 2 * self.capacity
        new_arr = [None] * new_capacity

        for i in range(self.length):
            new_arr[i] = self.arr[i]

        self.arr = new_arr
        self.capacity = new_capacity

    def add(self, value, i=None):
        """
        Insert a value at a given index (default: end of array).

        Algorithm:
        1. If no index is provided, use current length (append behavior).
        2. If array is full, resize.
        3. Assign value to index.
        4. Increment logical length.

        Time Complexity: O(1) amortized
        """
        if i is None:
            i = self.length

        if i < 0 or i > self.length:
            raise IndexError("Invalid index")

        if self.is_full():
            self.resize()

        self.arr[i] = value
        self.length += 1

    def print_array(self):
        print("Array: ", end="")
        for i in range(self.length):
            print(self.arr[i], end=" ")
        print()

    def insert_at(self, index, value):
        """
        Insert a value at a specific index.

        Algorithm:
        1. Validate index (0 ≤ index ≤ length).
        2. If array is full, resize.
        3. Shift elements right starting from the end down to index.
        4. Insert value at index.
        5. Increment logical length.

        Time Complexity: O(n)
        """
        if index < 0 or index > self.length:
            raise IndexError("Invalid index")

        if self.is_full():
            self.resize()

        for i in range(self.length - 1, index - 1, -1):
            self.arr[i + 1] = self.arr[i]

        self.add(value, index)

    def insert_start(self, value):
        """
        Insert a value at the beginning of the array.

        Algorithm:
        1. If array is full, resize.
        2. Shift all elements right by one position.
        3. Insert new value at index 0.
        4. Increment logical length.

        Time Complexity: O(n)
        """
        if self.is_full():
            self.resize()

        for i in range(self.length - 1, -1, -1):
            self.arr[i + 1] = self.arr[i]

        self.add(value, 0)

    def insert_end(self, value):
        """
        Insert a value at the end of the array.

        Algorithm:
        Equivalent to append.
        Insert at index = current length.

        Time Complexity: O(1) amortized
        """
        self.add(value)

    def delete_at(self, index):
        """
        Delete and return an element at a specific index.

        Algorithm:
        1. Validate index (0 ≤ index < length).
        2. Ensure array is not empty.
        3. Shift elements left starting from index.
        4. Store the duplicated value at the last logical slot.
        5. Decrement logical length.
        6. Clear the now-unused slot (set to None).
        7. Return the removed value.

        Time Complexity: O(n)
        """
        if self.is_empty():
            raise IndexError("Can't delete from empty array")

        if index < 0 or index >= self.length:
            raise IndexError("Invalid index")

        value = self.arr[index]

        for i in range(index, self.length - 1):
            self.arr[i] = self.arr[i + 1]

        self.length -= 1
        self.arr[self.length] = None
        return value

    def delete_start(self):
        """
        Delete and return the first element of the array.

        Algorithm:
        1. Ensure array is not empty.
        2. Shift all elements left by one.
        3. Store the duplicated value at the last logical slot.
        4. Decrement logical length.
        5. Clear the now-unused slot (set to None).
        6. Return the removed value.

        Time Complexity: O(n)
        """
        if self.is_empty():
            raise IndexError("Can't delete from empty array")

        value = self.arr[0]

        for i in range(self.length - 1):
            self.arr[i] = self.arr[i + 1]

        self.length -= 1
        self.arr[self.length] = None
        return value

    def delete_end(self):
        """
        Delete and return the last element of the array.

        Algorithm:
        1. Ensure array is not empty.
        2. Store the last logical element.
        3. Decrement logical length.
        4. Clear the now-unused slot (set to None).
        5. Return the removed value.

        Time Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Can't delete from empty array")

        value = self.arr[self.length - 1]
        self.length -= 1
        self.arr[self.length] = None
        return value


if __name__ == "__main__":
    # Basic creation + automatic resizing
    arr = DynamicArray(2)

    print("Initial size:", arr.size())
    print("Initial capacity:", arr.get_capacity())
    arr.print_array()
    print()

    arr.insert_end(10)
    arr.insert_end(20)

    print("After inserting 10 and 20:")
    arr.print_array()
    print("Size:", arr.size())
    print("Capacity:", arr.get_capacity())
    print()

    arr.insert_end(30)

    print("After inserting 30 (resize should have happened):")
    arr.print_array()
    print("Size:", arr.size())
    print("Capacity:", arr.get_capacity())
    print()

    arr.insert_at(1, 99)
    print("After inserting 99 at index 1:")
    arr.print_array()
    print()

    arr.insert_start(-5)
    print("After inserting -5 at the start:")
    arr.print_array()
    print()

    print("Element at index 2:", arr.get(2))
    print("Last element:", arr.last())
    print()

    arr.set(2, 777)
    print("After setting index 2 to 777:")
    arr.print_array()
    print()

    removed = arr.delete_at(1)
    print("Removed from index 1:", removed)
    arr.print_array()
    print()

    removed = arr.delete_start()
    print("Removed from start:", removed)
    arr.print_array()
    print()

    removed = arr.delete_end()
    print("Removed from end:", removed)
    arr.print_array()
    print()

    print("===== Error handling examples =====")

    try:
        print(arr.get(100))
    except IndexError as e:
        print("Error:", e)

    try:
        arr.set(-1, 500)
    except IndexError as e:
        print("Error:", e)

    try:
        arr.insert_at(100, 42)
    except IndexError as e:
        print("Error:", e)

    empty = DynamicArray()

    try:
        empty.delete_end()
    except IndexError as e:
        print("Error:", e)

    try:
        empty.delete_start()
    except IndexError as e:
        print("Error:", e)

    try:
        empty.delete_at(0)
    except IndexError as e:
        print("Error:", e)