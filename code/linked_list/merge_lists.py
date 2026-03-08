# Merge Two Sorted Linked Lists
#
# Merging two linked lists means combining two already-sorted lists into
# one sorted list by relinking the existing nodes.
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
# To simplify the algorithm, we use a **dummy node**.
# The dummy node acts as a temporary starting point so we do not need
# special logic to determine the head of the merged list.
#
# Pointers used:
#
# cur1  : current node in list 1
# cur2  : current node in list 2
# node  : last node in the merged list being built (tail pointer)
# dummy : fixed starting node used to simplify linking
#
# Walkthrough with the example lists:
#
# Start
# dummy -> None
#          ^
#        node
#
# cur1 = 1
# cur2 = 1
#
# Compare cur1 and cur2
# 1 <= 1 so attach cur1
#
# dummy -> 1
#           ^
#         node
#
# cur1 moves to 4
#
# Iteration 1
# cur1 = 4
# cur2 = 1
#
# 1 < 4 so attach cur2
#
# dummy -> 1 -> 1
#                ^
#              node
#
# cur2 moves to 3
#
# Iteration 2
# cur1 = 4
# cur2 = 3
#
# 3 < 4 so attach cur2
#
# dummy -> 1 -> 1 -> 3
#                     ^
#                   node
#
# Continue comparing nodes until one list becomes None.
#
# Once one list ends, attach the remaining portion of the other list
# directly to the merged list.
#
# Finally, return dummy.next to skip the temporary dummy node.
#
# Time Complexity: O(n + m)
# We traverse each node from both lists once.
#
# Space Complexity: O(1)
# No new nodes are created; we reuse the existing nodes and only update
# their next pointers.

class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


def merge_linked_lists(head1, head2):
    dummy = node = Node()

    cur1 = head1
    cur2 = head2

    while cur1 and cur2:
        if cur1.data < cur2.data:
            node.next = cur1
            cur1 = cur1.next
        else:
            node.next = cur2
            cur2 = cur2.next

        node = node.next

    # Attach whichever list still has remaining nodes
    node.next = cur1 or cur2

    # dummy isn't part of the merged list, so return the next node
    return dummy.next

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