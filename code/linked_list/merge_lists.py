# Merge Two Sorted Linked Lists
#
# Merging two linked lists means creating a new list that contains all nodes
# from both lists while maintaining sorted order.
#
# Example:
#
# List 1 (n nodes):
# 1 -> 4 -> 5 -> 13 -> None
#
# List 2 (m nodes):
# 1 -> 3 -> 7 -> 10 -> 19 -> None
#
# Merged list (n + m nodes):
# 1 -> 1 -> 3 -> 4 -> 5 -> 7 -> 10 -> 13 -> 19 -> None
#
# Pointers used:
#
# cur1   : current node in list 1
# cur2   : current node in list 2
# list3  : last node in the merged list being built
# new_head : start of the merged list (never moves)
#
# Walkthrough with the example lists:
#
# Start
# cur1 = 1
# cur2 = 1
#
# Compare cur1 and cur2
# 1 <= 1 so create first node from list1
#
# new_head -> 1
#            ^
#          list3
#
# cur1 moves to 4
#
# Iteration 1
# cur1 = 4
# cur2 = 1
#
# 1 < 4 so append cur2
#
# new_head -> 1 -> 1
#                 ^
#               list3
#
# cur2 moves to 3
#
# Iteration 2
# cur1 = 4
# cur2 = 3
#
# 3 < 4 so append cur2
#
# new_head -> 1 -> 1 -> 3
#                      ^
#                    list3
#
# cur2 moves to 7
#
# Iteration 3
# cur1 = 4
# cur2 = 7
#
# 4 < 7 so append cur1
#
# new_head -> 1 -> 1 -> 3 -> 4
#                           ^
#                         list3
#
# Continue until one list becomes None.
#
# Once one list ends, append the remaining nodes
# from the other list directly to the merged list.
#
# Time Complexity: O(n + m)
# We traverse each node from both lists once.

# Space Complexity: O(1)
# No new nodes are created; we reuse the existing nodes and only update their next pointers.

class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def merge_linked_lists(head1, head2):
    cur1 = head1
    cur2 = head2
    list3 = None

    if cur1.data < cur2.data:
            list3 = cur1
            cur1 = cur1.next
    else:
         list3 = cur2
         cur2 = cur2.next

    new_head = list3

    while cur1 and cur2:
        if cur1.data < cur2.data:
            list3.next = cur1
            list3 = list3.next
            cur1 = cur1.next
        else:
            list3.next = cur2
            list3 = list3.next
            cur2 = cur2.next

    while cur1:
         list3.next = cur1
         list3 = list3.next
         cur1 = cur1.next

    while cur2:
         list3.next = cur2
         list3 = list3.next
         cur2 = cur2.next
        

    return new_head

def print_list(list):
        current = list

        while current:
            print(current.data, end=" ")
            current = current.next
        print()
     


l0 = Node(1)
l0n1 = Node(4)
l0n2 = Node(5)
l0n3 = Node(13)

l1 = Node(1)
l1n1 = Node(3)
l1n2 = Node(7)
l1n3 = Node(10)
l1n4 = Node(19)


l0.next = l0n1
l0n1.next = l0n2
l0n2.next = l0n3

l1.next = l1n1
l1n1.next = l1n2
l1n2.next = l1n3
l1n3.next = l1n4

list3 = merge_linked_lists(l0, l1)
print_list(list3)