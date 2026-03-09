class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class LinkedList:
    """
    Doubly Linked List implementation.

    Design Features:
    - Dummy (sentinel) head node
    - Tail pointer for O(1) appends
    - prev pointers for reverse traversal and O(1) deletion by reference
    """

    def __init__(self):
        # head is a dummy/sentinel node.
        # The first real node is stored at head.next.
        # If head.next is None, the list is empty.
        self.head = Node()
        self.tail = self.head


    def add_node(self, node):
        """
        Append a node to the end of the list.

        Algorithm:
        1. Disconnect the new node from any existing list.
        2. Link the new node after the current tail.
        3. Update both next and prev pointers.
        4. Move the tail pointer forward.

        Time Complexity: O(1)
        """

        # node is the new tail, so it shouldn't point to another node
        node.next = None

        # Link the new node after the current tail
        self.tail.next = node
        node.prev = self.tail

        # Update the tail pointer
        self.tail = node


    def get_node(self, index):
        """
        Return the node at the given index.

        Algorithm:
        1. Start at the first real node (head.next).
        2. Traverse forward `index` steps.
        3. If traversal reaches None early, the index is invalid.
        4. Return the node found.

        Time Complexity: O(n)
        """

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
        Update the data stored in the node at the given index.

        Algorithm:
        1. Traverse to the node at the given index.
        2. Replace the data stored in that node.

        Time Complexity: O(n)
        """

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
        """
        Delete the node at the given index.

        Algorithm:
        1. Traverse to the node at the given index.
        2. Store references to the nodes before and after it.
        3. Update pointers so the previous node skips the deleted node.
        4. Fix the backward pointer of the next node.
        5. If the deleted node was the tail, update the tail pointer.

        Time Complexity: O(n)
        """

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
        """
        Delete a node when a reference to it is already known.

        Algorithm:
        1. Identify the node before and after the target node.
        2. Connect those nodes together.
        3. Update both next and prev pointers.
        4. If the deleted node was the tail, update the tail pointer.

        Time Complexity: O(1)
        """

        # The sentinel head is not a real node.
        # The first real node in the list is stored at head.next.
        if node is self.head:
            return

        prev_node = node.prev
        next_node = node.next

        # Skip over the node being deleted
        # Example: A <-> B <-> C  ->  A <-> C
        prev_node.next = next_node

        # Fix the backward pointer of the next node
        if next_node:
            next_node.prev = prev_node
        else:
            # If the deleted node was the tail,
            # move the tail pointer back
            self.tail = prev_node


    def delete_head(self):
        """
        Delete the first real node (head.next).

        Algorithm:
        1. Check if the list is empty.
        2. Store the first real node.
        3. Move head.next to the second node.
        4. Fix the backward pointer of the new first node.
        5. If the list becomes empty, reset the tail pointer.

        Time Complexity: O(1)
        """

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
        """
        Delete the last real node in the list.

        Algorithm:
        1. Check if the list is empty.
        2. Store the current tail.
        3. Move the tail pointer back one node.
        4. Disconnect the old tail.

        Time Complexity: O(1)
        """

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
        """
        Print all values in the linked list.

        Algorithm:
        Traverse from the first real node until reaching None.

        Time Complexity: O(n)
        """

        current = self.head.next

        while current:
            print(current.data, end=" ")
            current = current.next

        print()


    def print_reverse(self):
        """
        Print the linked list in reverse order.

        Algorithm:
        1. Start at the tail.
        2. Traverse backwards using prev pointers.
        3. Stop when reaching the sentinel head.

        Time Complexity: O(n)
        """

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