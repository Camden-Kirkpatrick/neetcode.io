from arrays.dynamic_array import DynamicArray

class Stack:
    """
    A stack (LIFO) implementation backed by a DynamicArray.

    - Push adds to the top of the stack.
    - Pop removes from the top of the stack.
    - Peek reads the top without removing it.
    """

    def __init__(self, capacity=2):
        """
        Initialize the stack.

        Algorithm:
        1. Create an underlying DynamicArray with the given initial capacity.
        """
        self.data = DynamicArray(capacity)

    def size(self):
        """
        Return the number of elements in the stack.

        Algorithm:
        Return the size of the underlying dynamic array.

        Time Complexity: O(1)
        """
        return self.data.size()
    
    def __len__(self):
        """
        Equivalent to size().
        Allow "len()" syntax.
        """
        return self.data.size()

    def is_empty(self) -> bool:
        """
        Check whether the stack is empty.

        Algorithm:
        If the underlying array is empty, the stack is empty.

        Time Complexity: O(1)
        """
        return self.data.is_empty()
    
    def push(self, value) -> None:
        """
        Push a value onto the top of the stack.

        Algorithm:
        Insert the value at the end of the underlying dynamic array.

        Time Complexity: O(1) amortized
        """
        self.data.insert_end(value)

    def peek(self):
        """
        Return the top element without removing it.

        Algorithm:
        1. Ensure stack is not empty.
        2. Return the last element of the underlying dynamic array.

        Time Complexity: O(1)
        """
        if self.data.is_empty():
            print("Can't peek from empty stack")
            return None
        
        return self.data.last()
    
    def pop(self):
        """
        Remove and return the top element.

        Algorithm:
        Delete and return the last element of the underlying dynamic array.

        Time Complexity: O(1)
        """
        return self.data.delete_end()