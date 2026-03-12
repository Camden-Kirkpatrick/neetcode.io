# Go to "\code", then run: python -m stack.stack

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
        Create an underlying DynamicArray with the given initial capacity.
        """
        self.data = DynamicArray(capacity)


    def size(self):
        return self.data.size()
    

    def __len__(self):
        return self.data.size()


    def is_empty(self) -> bool:
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
            raise IndexError("Can't peek from empty stack")
        
        return self.data.last()
    

    def pop(self):
        """
        Remove and return the top element.

        Algorithm:
        Delete and return the last element of the underlying dynamic array.

        Time Complexity: O(1)
        """
        return self.data.delete_end()



if __name__ == "__main__":
    print("===== BASIC STACK OPERATIONS =====")
    s = Stack()

    print("Initial size:", s.size())
    print("Is empty:", s.is_empty())
    print()

    s.push(3)
    s.push(8)
    s.push(0)

    print("After pushing 3, 8, and 0:")
    print("len(stack):", len(s))
    print("stack.size():", s.size())
    print("top:", s.peek())
    print()

    removed = s.pop()
    print("Popped:", removed)
    print("New top:", s.peek())
    print()

    removed = s.pop()
    print("Popped:", removed)
    print("New top:", s.peek())
    print()

    removed = s.pop()
    print("Popped:", removed)
    print("Is empty:", s.is_empty())
    print()

    print("===== ERROR HANDLING EXAMPLES =====")

    try:
        print("Trying to peek from empty stack:")
        print(s.peek())
    except IndexError as e:
        print("Error:", e)

    try:
        print("Trying to pop from empty stack:")
        print(s.pop())
    except IndexError as e:
        print("Error:", e)

    try:
        print("Trying to create a stack with invalid capacity:")
        bad_stack = Stack(0)
    except ValueError as e:
        print("Error:", e)

    print()
    print("===== RESIZE TEST =====")

    s2 = Stack(2)
    s2.push(10)
    s2.push(20)
    s2.push(30)

    print("After pushing 10, 20, and 30 into Stack(2):")
    print("len(stack):", len(s2))
    print("top:", s2.peek())

    print("Popped:", s2.pop())
    print("Popped:", s2.pop())
    print("Popped:", s2.pop())

    try:
        s2.pop()
    except IndexError as e:
        print("Error:", e)