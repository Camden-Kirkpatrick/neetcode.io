# Min Stack
#
# A Min Stack is a stack that supports normal stack operations
# (push, pop, top) while also allowing retrieval of the minimum
# element in constant time O(1).
#
# To avoid scanning the entire stack for the minimum (O(n)),
# we maintain a second stack called min_stack that stores the
# minimum value at each depth of the main stack.
#
# On each push:
#   • Push the value onto stack.
#   • Push the new minimum onto min_stack:
#       min(val, previous_min).
#
# On pop:
#   • Pop from both stack and min_stack to keep them aligned.
#
# The current minimum is always the top of min_stack.
#
# Example:
# push(5) → stack=[5]        min_stack=[5]
# push(3) → stack=[5,3]      min_stack=[5,3]
# push(7) → stack=[5,3,7]    min_stack=[5,3,3]
# push(2) → stack=[5,3,7,2]  min_stack=[5,3,3,2]
#
# Time Complexity: O(1) for push, pop, top, and get_min
# Space Complexity: O(n)
class MinStack:

    def __init__(self):
        # Main stack that stores all pushed values
        self.stack = []

        # Auxiliary stack that stores the minimum value at each depth
        self.min_stack = []
        

    def push(self, val: int) -> None:
        # Push the value onto the main stack
        self.stack.append(val)

        # If this is the first element, it is automatically the minimum
        if not self.min_stack:
            self.min_stack.append(val)

        # Otherwise, compare the new value with the previous minimum
        # and store the new minimum at this depth
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))


    def pop(self) -> None:
        # Remove the top element from both stacks
        # This keeps stack and min_stack synchronized
        self.stack.pop()
        self.min_stack.pop()


    def top(self) -> int:
        # Return the most recently pushed value
        return self.stack[-1]
        

    def get_min(self) -> int:
        # The current minimum is always the top of min_stack
        return self.min_stack[-1]
    
s = MinStack()
s.push(24)
s.push(45)
s.push(6)
print("top:", s.top())
print("minimum:", s.get_min())
s.pop()
print("top:", s.top())
print("minimum:", s.get_min())