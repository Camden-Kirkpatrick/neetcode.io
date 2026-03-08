# Linked List
#
# A linked list is a linear data structure made of nodes. Each node stores:
#   1. Data (the value of the node)
#   2. A reference (pointer) to the next node in the list
#
# Example structure:
#
#   50 -> 84 -> -43 -> None
#
# Each arrow represents the "next" pointer that links one node to another.
# The first node in the list is called the "head". The last node points to None.
#
#
# Node structure used in this program:
#
#   class Node:
#       data -> stores the value
#       next -> reference to the next node
#
#
# Why linked lists exist
#
# Arrays store elements in contiguous memory and allow O(1) indexing,
# but inserting or deleting elements in the middle requires shifting
# many elements.
#
# Linked lists avoid shifting by changing pointers instead.
#
# Example deletion:
#
#   10 -> 20 -> 30 -> 40
#
# Delete 30:
#
#   10 -> 20 -> 40
#
# Only one pointer changes:
#
#   20.next = 40
#
#
# Key operations
#
# Traversal:
#   Walk through the list starting from the head.
#
# Insertion:
#   Add a node by updating the previous node's "next" pointer.
#
# Deletion:
#   Skip over a node by linking the previous node to the next node.
#
#
# Time complexity
#
# Operation              Complexity
# --------------------------------
# Access by index        O(n)
# Search                 O(n)
# Insert (known node)    O(1)
# Delete (known node)    O(1)
#
# If you do NOT already know where the node is, you must traverse
# the list first, which costs O(n).
#
#
# Advantages of linked lists
#
# • Dynamic size (can grow and shrink easily)
# • Efficient insertions and deletions
# • No shifting of elements required
#
#
# Disadvantages
#
# • No direct indexing like arrays
# • Extra memory required for pointers
# • Traversal required for most operations
#
#
# This implementation demonstrates:
#
#   add_node(index)   → append a node to the end
#   get_node(index)   → retrieve a node by index
#   set_node(index)   → update a node's value
#   delete_node(index)→ remove a node
#   print_list()      → traverse and print the list

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, head):
        # head points to the first node in the list
        # If head is None, the list is empty
        self.head = head

    def add_node(self, node):
        # Add a node to the end of the linked list

        current = self.head

        # Traverse the list until we reach the last node
        while current:
            if not current.next:
                # If the current node is the last node,
                # link it to the new node
                current.next = node
                break
            else:
                # Otherwise move to the next node
                current = current.next
    
    def get_node(self, index):
        # Return the node at the given index

        if index < 0:
            print("Index must be greater than -1")
            return
        
        current = self.head

        # Move forward index times
        # Each iteration moves one node ahead
        for _ in range(index):
            if current is None:
                # If we hit None before reaching the index,
                # the index is out of bounds
                print("Invalid index")
                return
            current = current.next
        
        # current now points to the node at the requested index
        return current

    def set_node(self, index, value):
        # Update the data stored in the node at the given index

        if index < 0:
            print("Index must be greater than -1")
            return
        
        current = self.head

        # Traverse to the desired index
        for _ in range(index):
            if current is None:
                print("Invalid index")
                return
            current = current.next

        # Replace the data stored in that node
        current.data = value

    def delete_node(self, index):
        # Delete the node at the given index

        if index < 0:
            print("Index must be greater than -1")
            return

        # If the list is empty, nothing to delete
        if not self.head:
            print("Linked list is empty")
            return

        # Special case: deleting the head node
        if index == 0:
            # Move the head pointer to the next node
            self.head = self.head.next
            return

        current = self.head

        # Traverse to the node BEFORE the one we want to delete
        for _ in range(index - 1):
            current = current.next

            if current is None:
                # Index is out of bounds
                print("Invalid index")
                return

        # If current.next is None, the index does not exist
        if current.next is None:
            print("Invalid index")
            return
        
        # Skip over the node being deleted
        # Example:
        # current -> [A] -> [B] -> [C]
        # If deleting B:
        # current.next = current.next.next
        # Result:
        # current -> [A] -> [C]
        current.next = current.next.next
    
    def print_list(self):
        # Print all values in the linked list

        current = self.head

        # Traverse the list until we reach None
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
print("Linked List:", end=" ")
linked_list.print_list()

copy_n2 = linked_list.get_node(2)
print("Data from node 3:", copy_n2.data)
invalid = linked_list.get_node(-1)
invalid = linked_list.get_node(100)

print("After changing the second node:", end=" ")
linked_list.set_node(1, 36)
linked_list.print_list()

linked_list.delete_node(2)
linked_list.print_list()
linked_list.delete_node(-1)
linked_list.delete_node(100)