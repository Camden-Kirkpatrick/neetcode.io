# Stack Using Queues
#
# This program demonstrates how to implement a stack (LIFO)
# using only queue operations.
#
# A stack normally works like this:
#
# push(x) -> add x to the top
# pop()   -> remove the most recently added element
# top()   -> read the top element
#
#
# Stack Behavior (Last In, First Out)
#
# Example:
#
# push(1)
# push(2)
# push(3)
#
# Stack:
#
# top
#  ↓
# 3
# 2
# 1
#
# pop() -> 3
#
#
# Queue Behavior (First In, First Out)
#
# Example:
#
# append(1)
# append(2)
# append(3)
#
# Queue:
#
# front -> [1, 2, 3] <- back
#
# popleft() -> 1
#
#
# The Problem
#
# Queues remove the OLDEST element.
# Stacks remove the NEWEST element.
#
# So how can we simulate stack behavior using queues?
#
#
# Key Idea
#
# If we arrange the queue so that the newest element is always
# at the FRONT, then removing from the queue behaves exactly
# like popping from a stack.
#
# In other words:
#
# queue front = stack top
#
#
# Strategy
#
# We use two queues:
#
# q1 -> main queue that stores the stack
# q2 -> temporary helper queue used during push
#
#
# Push Algorithm
#
# When pushing a new value x:
#
# 1. Put x into the helper queue (q2)
#
# 2. Move all existing elements from q1 to q2
#
#    This places the previous elements behind x.
#
#    Example:
#
#    Before push(3):
#
#    q1 = [2,1]
#
#    After step 1:
#
#    q2 = [3]
#
#    After step 2:
#
#    q2 = [3,2,1]
#
# 3. Swap q1 and q2
#
#    Now the main queue contains the correct stack order.
#
#
# Result
#
# The queue always stores the stack like this:
#
# front -> [top, next, next, ...]
#
#
# Complexity
#
# push()  -> O(n)
# pop()   -> O(1)
# top()   -> O(1)
# empty() -> O(1)
#
#
# Why This Works
#
# Queues normally remove from the front.
# By forcing the newest element to be at the front,
# queue removal behaves exactly like stack pop.


from collections import deque


class MyStack:

    def __init__(self):
        """
        Initialize two queues.

        q1 is the main queue that represents the stack.

        q2 is a temporary helper queue used during push
        operations to reorder elements.
        """
        self.q1 = deque()
        self.q2 = deque()


    def push(self, x: int) -> None:
        """
        Push a new value onto the stack.

        Algorithm:
        1. Insert the new element into q2.
        2. Move all elements from q1 into q2.
        3. Swap q1 and q2 so q1 becomes the main stack queue.

        This ensures the newest element is always at the
        FRONT of q1.
        """

        # Step 1: add the new element to the helper queue
        self.q2.append(x)

        # Step 2: move all existing elements behind it
        while self.q1:
            self.q2.append(self.q1.popleft())

        # Step 3: swap queues so q1 becomes the updated stack
        self.q1, self.q2 = self.q2, self.q1


    def pop(self) -> int:
        """
        Remove and return the top element of the stack.

        Since the newest element is always stored at the
        FRONT of q1, we simply remove from the front.

        Time Complexity: O(1)
        """
        return self.q1.popleft()


    def top(self) -> int:
        """
        Return the top element without removing it.

        The stack top is stored at the front of q1.
        """
        return self.q1[0]


    def empty(self) -> bool:
        """
        Check whether the stack is empty.

        If q1 contains no elements, the stack is empty.
        """
        return len(self.q1) == 0



if __name__ == "__main__":

    print("===== STACK USING QUEUES DEMO =====")
    stack = MyStack()

    print("Stack empty?", stack.empty())
    print()

    print("Pushing 1")
    stack.push(1)

    print("Pushing 2")
    stack.push(2)

    print("Pushing 3")
    stack.push(3)

    # Internally the queue now looks like:
    # front -> [3,2,1]

    print()
    print("Current top:", stack.top())
    print()

    print("Popping:", stack.pop())
    print("New top:", stack.top())
    print()

    print("Popping:", stack.pop())
    print("New top:", stack.top())
    print()

    print("Popping:", stack.pop())
    print()

    print("Stack empty?", stack.empty())