"""
Doubly Linked List Design Overview
----------------------------------

This implementation uses three important design choices:

1. Dummy / Sentinel Head Node
2. Tail Pointer
3. Previous (prev) Pointer


1. Dummy / Sentinel Node
------------------------

The linked list starts with a special node called a sentinel (or dummy node).

    head (sentinel) <-> A <-> B <-> C

The sentinel does not store real data. Its job is to simplify insertions
and deletions at the front of the list.

Without a sentinel node, the first real node has no node before it:

    head -> A <-> B <-> C

So deleting A requires special logic:

    if index == 0:
        self.head = self.head.next

Using a sentinel fixes this problem because every real node always has
a previous node.

    head (sentinel) <-> A <-> B <-> C

Now deleting the first node uses the same pointer update pattern used
for all nodes:

    prev.next = next
    next.prev = prev

The first real node is always stored at:

    head.next

If head.next is None, the list is empty.


2. Tail Pointer
---------------

The list also stores a reference to the last node:

    self.tail

This allows appending nodes in constant time.

Without a tail pointer:

    add_node() requires traversing the entire list
    Time Complexity: O(n)

With a tail pointer:

    self.tail.next = new_node
    new_node.prev = self.tail
    self.tail = new_node

    Time Complexity: O(1)

The tail pointer also allows deleting the last node in O(1):

    self.tail = self.tail.prev
    self.tail.next = None


3. Previous (prev) Pointer
--------------------------

Each node stores two pointers:

    next -> the node after it
    prev -> the node before it

This makes the structure a doubly linked list:

    A <-> B <-> C

The prev pointer allows us to:

• Traverse the list backwards
• Delete nodes when we already have a reference to them
• Easily update neighbors during insertion and deletion

Deletion becomes:

    prev.next = next
    next.prev = prev


Supported Operations
--------------------

This implementation supports several deletion strategies:

Delete by index:
    Traverse to the node and unlink it.

Delete by reference:
    If we already have a pointer to the node, it can be removed in O(1).

Delete head:
    Remove the first real node (head.next).

Delete tail:
    Remove the last node using the tail pointer.

Reverse traversal:
    Walk backward through the list using prev pointers.


Summary
-------

Sentinel Node
    Removes edge cases when inserting or deleting the first node.

Tail Pointer
    Allows O(1) insertion and deletion at the end of the list.

Prev Pointer
    Enables backward traversal and O(1) deletion when a node reference
    is already known.
"""

class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self):
        # head is a dummy/sentinel node.
        # The first real node is stored at head.next.
        # If head.next is None, the list is empty.
        self.head = Node()
        self.tail = self.head


    def add_node(self, node):
        # Add a node to the end of the linked list

        # node is the new tail, so it shouldn't point to another node
        node.next = None

        # Link the new node after the current tail
        self.tail.next = node
        node.prev = self.tail

        # Update the tail pointer
        self.tail = node
    

    def get_node(self, index):
        # Return the node at the given index

        if index < 0:
            print("Index must be greater than -1")
            return
        
        current = self.head.next

        # Move forward index times
        # Each iteration moves one node ahead
        for _ in range(index):
            if current is None:
                # If we hit None before reaching the index,
                # the index is out of bounds
                print("Invalid index")
                return
            current = current.next

        # If current is None after the traversal,
        # the index does not exist
        if current is None:
            print("Invalid index")
            return
        
        # current now points to the node at the requested index
        return current


    def set_node(self, index, value):
        # Update the data stored in the node at the given index

        if index < 0:
            print("Index must be greater than -1")
            return
        
        current = self.head.next

        # Traverse to the desired index
        for _ in range(index):
            if current is None:
                print("Invalid index")
                return
            current = current.next

        # If current is None after the traversal,
        # the index does not exist
        if current is None:
            print("Invalid index")
            return

        # Replace the data stored in that node
        current.data = value


    def delete_node_index(self, index):
        # Delete the node at the given index

        if index < 0:
            print("Index must be greater than -1")
            return

        # Start at the first real node
        # (self.head is a dummy/sentinel node)
        current = self.head.next

        # Traverse forward until we reach the node
        # at the requested index
        for _ in range(index):
            if current is None:
                # If we reach None before finishing the traversal,
                # the index is out of bounds
                print("Invalid index")
                return
            current = current.next

        # If current is None after the traversal,
        # the index does not exist
        if current is None:
            print("Invalid index")
            return

        # Store references to the nodes before and after
        # the node being deleted
        prev_node = current.prev
        next_node = current.next

        if current is self.tail:
            self.tail = prev_node

        # Skip over the node being deleted
        # Example:
        # [A] <-> [B] <-> [C]
        #
        # If deleting B:
        # A.next should now point to C
        # and C.prev should now point to A
        #
        # Result:
        # [A] <-> [C]
        prev_node.next = next_node

        # If there is a node after the deleted node,
        # update its prev pointer so it points back
        # to the correct previous node
        if next_node:
            next_node.prev = prev_node


    def delete_node_reference(self, node):
        # Delete a node when we already have a reference to it

        prev_node = node.prev
        next_node = node.next

        # Skip over the node being deleted
        # Example: A <-> B <-> C  ->  A <-> C
        prev_node.next = next_node

        # Fix the backward pointer of the next node
        if next_node:
            next_node.prev = prev_node

    
    def delete_head(self):
        # Delete the first real node (self.head.next)

        # If the list is empty, nothing to delete
        if self.head.next is None:
            return

        # Store the first real node
        first = self.head.next

        # Skip over the node being deleted
        # Example: head <-> A <-> B  ->  head <-> B
        self.head.next = first.next

        # Fix the backward pointer of the new first node
        if first.next:
            first.next.prev = self.head
        else:
            # If the list is now empty, reset the tail
            self.tail = self.head
    

    def delete_tail(self):
        # Delete the last real node in the list

        # If the list is empty, nothing to delete
        if self.tail is self.head:
            return

        # Store the current tail node
        last = self.tail

        # Move the tail pointer back one node
        # Example: head <-> A <-> B <-> C  ->  head <-> A <-> B
        self.tail = last.prev

        # Disconnect the old tail
        self.tail.next = None
    

    def print_list(self):
        # Print all values in the linked list

        current = self.head.next

        # Traverse the list until we reach None
        while current:
            print(current.data, end=" ")
            current = current.next

        print()

    def print_reverse(self):
        current = self.tail

        while current is not self.head:
            print(current.data, end=" ")
            current = current.prev

        print()



linked_list = LinkedList()

# Create and add nodes to the linked list
n1 = Node(84)
linked_list.add_node(n1)
n2 = Node(-43)
linked_list.add_node(n2)
n3 = Node(28)
linked_list.add_node(n3)
print("Linked List:", end=" ")
linked_list.print_list()

# Get a node by index
copy_n2 = linked_list.get_node(2)
print("Data from node 3:", copy_n2.data)
invalid = linked_list.get_node(-1)
invalid = linked_list.get_node(100)

# Set a node to a new value
print("After changing the second node:", end=" ")
linked_list.set_node(1, 36)
linked_list.print_list()

# Delete a node by index
linked_list.delete_node_index(0)
print("After deleting the first node:", end=" ")
linked_list.print_list()
linked_list.delete_node_index(-1)
linked_list.delete_node_index(100)

# Delete a node by reference
n4 = Node(101)
linked_list.add_node(n4)
print("After adding Node(101):", end=" ")
linked_list.print_list()
print("After deleting Node(101):", end=" ")
linked_list.delete_node_reference(n4)
linked_list.print_list()

print("Reversed list:", end=" ")
linked_list.print_reverse()