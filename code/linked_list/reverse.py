# Reverse a Linked List
#
# Reversing a linked list means flipping the direction of every "next"
# pointer so that the list runs backwards.
#
# Original list:
# 50 -> 84 -> -43 -> 9 -> None
#
# Reversed list:
# 9 -> -43 -> 84 -> 50 -> None
#
# To safely reverse the pointers, we must keep track of three nodes:
#
# prev    : the node that will come before the current node in the reversed list
# current : the node we are currently processing
# next    : the next node in the original list (saved so we don't lose the rest)
#
# Algorithm steps for each node:
# 1. Save the next node (next = current.next)
# 2. Reverse the link (current.next = prev)
# 3. Move prev forward (prev = current)
# 4. Move current forward (current = next)
#
# Walkthrough with this program's example:
#
# Start
# prev = None
# current = 50
#
# Iteration 1
# next = 84
# 50.next = None
# prev = 50
# current = 84
#
# Reversed portion:
# None <- 50
#
# Remaining portion:
# 84 -> -43 -> 9 -> None

# Iteration 2
# next = -43
# 84.next = 50
# prev = 84
# current = -43
#
# Reversed portion:
# None <- 50 <- 84
#
# Remaining portion:
# -43 -> 9 -> None

# Iteration 3
# next = 9
# -43.next = 84
# prev = -43
# current = 9
#
# Reversed portion:
# None <- 50 <- 84 <- -43
#
# Remaining portion:
# 9 -> None

# Iteration 4
# next = None
# 9.next = -43
# prev = 9
# current = None
#
# Reversed portion:
# None <- 50 <- 84 <- -43 <- 9
#
# Remaining portion:
# None
#
# The loop ends when current becomes None.
# At this point, prev is the new head of the reversed list.
#
# Time Complexity: O(n)
# Space Complexity: O(1)

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, head):
        self.head = head

    def add_node(self, node):
        current = self.head
        while current:
            if not current.next:
                current.next = node
                break
            else:
                current = current.next

    def reverse_list(self):
        current = self.head
        next = None
        prev = None

        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next

        self.head = prev

    
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()



head = Node(50)
linked_list = LinkedList(head)

n1 = Node(84)
linked_list.add_node(n1)
n2 = Node(-43)
linked_list.add_node(n2)
n3 = Node(9)
linked_list.add_node(n3)
print("Linked List:", end=" ")
linked_list.print_list()

linked_list.reverse_list()
linked_list.print_list()