class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


class LinkedList:
    """
    Singly Linked List implementation.

    Design Features:
    - Uses a dummy (sentinel) head node.
    - Maintains a tail pointer for O(1) appends.

    The first real node is always stored at head.next.
    If head.next is None, the list is empty.
    """

    def __init__(self):
        # head is a dummy/sentinel node.
        # The first real node is stored at head.next.
        # If head.next is None, the list is empty.
        self.head = Node()
        self.tail = self.head

    def add_node(self, node):
        """
        Append a node to the end of the linked list.

        Algorithm:
        1. Ensure the new node does not reference another node.
        2. Link the new node after the current tail.
        3. Update the tail pointer.

        Time Complexity: O(1)
        """

        # Add a node to the end of the linked list

        # node is the new tail, so it shouldn't point to another node
        node.next = None

        # Link the new node after the current tail
        self.tail.next = node

        # Update the tail pointer
        self.tail = node

    def get_node(self, index):
        """
        Return the node at the given index.

        Algorithm:
        1. Start at the first real node (head.next).
        2. Traverse forward `index` times.
        3. If traversal reaches None early, the index is invalid.
        4. Return the node found at that position.

        Time Complexity: O(n)
        """

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
        """
        Replace the data stored in a node at the given index.

        Algorithm:
        1. Traverse the list until reaching the desired index.
        2. Replace the node's data with the new value.

        Time Complexity: O(n)
        """

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

    def delete_node(self, index):
        """
        Delete the node at the given index.

        Algorithm:
        1. Start at the dummy head node so we always have a
           reference to the node before the one being deleted.
        2. Traverse to the node before the target index.
        3. Skip over the node being deleted.
        4. If the deleted node was the tail, move the tail pointer.

        Time Complexity: O(n)
        """

        # Delete the node at the given index

        if index < 0:
            print("Index must be greater than -1")
            return

        # Start at the dummy head so prev always points
        # to the node before the one we want to delete
        prev = self.head

        # Move prev to the node before the target node
        for _ in range(index):
            if prev.next is None:
                print("Invalid index")
                return
            prev = prev.next

        # If there is no node to delete, the index is invalid
        if prev.next is None:
            print("Invalid index")
            return

        # Store the node being deleted
        deleted = prev.next

        # Skip over the node being deleted
        # Example:
        # head -> A -> B -> C
        #
        # If deleting B:
        # A.next should now point to C
        prev.next = deleted.next

        # If we deleted the tail, move tail back to prev
        if deleted is self.tail:
            self.tail = prev

    def print_list(self):
        """
        Print all values stored in the linked list.

        Algorithm:
        Traverse the list from head.next until reaching None.

        Time Complexity: O(n)
        """

        # Print all values in the linked list

        current = self.head.next

        # Traverse the list until we reach None
        while current:
            print(current.data, end=" ")
            current = current.next

        print()



linked_list = LinkedList()

n1 = Node(50)
linked_list.add_node(n1)
n2 = Node(84)
linked_list.add_node(n2)
n3 = Node(-43)
linked_list.add_node(n3)

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