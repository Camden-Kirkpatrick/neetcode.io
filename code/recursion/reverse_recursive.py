# Reverse Linked List (Recursive)
#
# This program demonstrates how to reverse a singly linked list
# using recursion.
#
# A linked list is a sequence of nodes where each node stores:
#
# 1. A value
# 2. A pointer to the next node
#
# Example list:
#
# head -> 1 -> 2 -> 3 -> None
#
# Reversed result:
#
# head -> 3 -> 2 -> 1 -> None
#
#
# Key Idea of the Recursive Approach
#
# Instead of reversing pointers while traversing the list forward
# (like the iterative solution), recursion works by:
#
# 1. Recursively reversing the rest of the list
# 2. Fixing the current node when the recursion returns
#
#
# High Level Strategy
#
# Suppose we start with:
#
# 1 -> 2 -> 3 -> None
#
# The recursive calls will go all the way to the end:
#
# reverse(1)
#    reverse(2)
#       reverse(3)
#
# Once we reach the last node, the recursion stops.
#
# Then the call stack begins returning and we reverse the links
# while coming back up.
#
#
# Base Case
#
# The recursion stops when:
#
# 1. The list is empty
# 2. The list has only one node
#
# In either case the list is already reversed.
#
#
# Pointer Reversal Step
#
# Suppose we are returning to node 2 in the list:
#
# 2 -> 3 -> None
#
# But the recursive call has already reversed the rest:
#
# 3 -> None
#
# We flip the link by making:
#
# 3.next = 2
#
# Then we disconnect the original forward link:
#
# 2.next = None
#
#
# Final Result
#
# Original:
#
# 1 -> 2 -> 3 -> None
#
# Reversed:
#
# 3 -> 2 -> 1 -> None
#
#
# Complexity
#
# Time Complexity:  O(n)
# Each node is processed once.
#
# Space Complexity: O(n)
# Due to the recursion call stack.


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head):
    """
    Recursive linked list reversal.

    The function reverses the list starting at `head`
    and returns the new head of the reversed list.
    """

    # Base case:
    # If the list is empty or contains a single node,
    # it is already reversed.
    if head is None or head.next is None:
        return head

    # Recursively reverse the rest of the list.
    #
    # Example:
    #
    # head -> 1 -> 2 -> 3 -> None
    #
    # reverse_list(2) returns:
    #
    # 3 -> 2 -> None
    new_head = reverse_list(head.next)

    # Reverse the current node's pointer.
    #
    # head.next is the node after the current node.
    #
    # Example before:
    #
    # 1 -> 2 -> None
    #
    # Make:
    #
    # 2 -> 1
    head.next.next = head

    # Break the original forward link to avoid a cycle.
    head.next = None

    # The head of the reversed list never changes
    # once the recursion reaches the last node.
    return new_head


def print_list(head):
    """
    Print all nodes in the linked list.
    """
    cur = head
    while cur:
        print(cur.val, end=" ")
        cur = cur.next
    print()


if __name__ == "__main__":

    # Build example linked list:
    #
    # 1 -> 2 -> 3 -> None
    head = Node(1)
    n1 = Node(2)
    head.next = n1
    n2 = Node(3)
    n1.next = n2

    print("Original list:")
    print_list(head)

    # Reverse the list
    new_head = reverse_list(head)

    print("Reversed list:")
    print_list(new_head)