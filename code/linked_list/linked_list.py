class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


class LinkedList:
    """
    Singly Linked List implementation.

    Design Features:
    - Dummy (sentinel) head node
    - Dummy (sentinel) tail node
    - Only forward traversal (no prev pointers)
    """

    def __init__(self):
        # head is a dummy/sentinel node.
        # The first real node is stored at head.next.
        # If head.next is tail, the list is empty.
        self.head = Node()

        # tail is also a dummy/sentinel node
        # This replaces the need for None at the end of the list.
        self.tail = Node()

        # Connect the two sentinel nodes
        # head -> tail represents an empty list
        self.head.next = self.tail


    def add_at_tail(self, node):
        """
        Append a node to the end of the list.

        Algorithm:
        1. The new node is inserted before the dummy tail node.
        2. Traverse until reaching the node before the tail.
        3. Connect the new node between (prev_node) and (tail).

        Time Complexity: O(n)
        """

        # The node before insertion
        # head -> A -> B -> tail
        #              ^
        #          prev_node

        prev_node = self.head
        current = self.head.next

        # Traverse until we reach the dummy tail
        while current is not self.tail:
            prev_node = current
            current = current.next

        next_node = self.tail

        # Insert node between prev_node and next_node
        node.next = next_node
        prev_node.next = node


    def add_at_head(self, node):
        """
        Insert a node at the beginning of the list.

        Algorithm:
        1. The new node is inserted after the dummy head node.
        2. The first real node is stored in head.next.
        3. Connect the new node between (head) and (head.next).

        Time Complexity: O(1)
        """

        # Example before:
        # head -> A -> B -> tail
        #
        # After inserting X:
        # head -> X -> A -> B -> tail

        prev_node = self.head
        next_node = self.head.next

        node.next = next_node
        prev_node.next = node


    def add_at_index(self, index, node):
        """
        Insert a node at the specified index.

        Algorithm:
        1. Traverse the list until reaching the node currently at position `index`.
        2. Insert the new node BEFORE that node.
        3. If index equals the list length, insertion occurs before the dummy tail.

        Time Complexity: O(n)
        """

        if index < 0:
            print("Index must be greater than -1")
            return

        prev_node = self.head
        current = self.head.next

        # Traverse forward until reaching the desired index
        for _ in range(index):
            if current is self.tail:
                print("Invalid index")
                return
            prev_node = current
            current = current.next

        # current now points to the node currently at position "index"
        # The new node will be inserted BEFORE current

        next_node = current

        node.next = next_node
        prev_node.next = node


    def get_node(self, index):
        """
        Return the node at the given index.

        Algorithm:
        1. Start at the first real node (head.next).
        2. Traverse forward `index` steps.
        3. If traversal reaches the dummy tail early, the index is invalid.
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
            if current is self.tail:
                print("Invalid index")
                return
            current = current.next

        if current is self.tail:
            print("Invalid index")
            return

        # current now points to the node at the requested index
        return current


    def set_node(self, index, value):
        """
        Update the data stored in the node at the given index.

        Algorithm:
        1. Retrieve the node at the given index.
        2. Replace the data stored in that node.

        Time Complexity: O(n)
        """

        node = self.get_node(index)

        if node:
            node.data = value


    def delete_node_index(self, index):
        """
        Delete the node at the given index.

        Algorithm:
        1. Traverse to the node at the given index.
        2. Store references to the nodes before and after it.
        3. Update pointers so the previous node skips the deleted node.

        Time Complexity: O(n)
        """

        if index < 0:
            print("Index must be greater than -1")
            return

        # Start at the first real node
        # (self.head is a dummy/sentinel node)
        prev_node = self.head
        current = self.head.next

        # Traverse forward until reaching the desired index
        for _ in range(index):
            if current is self.tail:
                print("Invalid index")
                return
            prev_node = current
            current = current.next

        if current is self.tail:
            print("Invalid index")
            return

        # Store references to the nodes before and after
        # the node being deleted
        next_node = current.next

        # Skip over the node being deleted
        # prev_node -> current -> next_node
        # becomes
        # prev_node -> next_node
        prev_node.next = next_node


    def delete_head(self):
        """
        Delete the first real node (head.next).

        Algorithm:
        1. Check if the list is empty.
        2. Store the first real node.
        3. Move head.next to the second node.

        Time Complexity: O(1)
        """

        # If the list is empty, nothing to delete
        if self.head.next is self.tail:
            return

        first = self.head.next

        self.head.next = first.next


    def delete_tail(self):
        """
        Delete the last real node in the list.

        Algorithm:
        1. Check if the list is empty.
        2. Traverse to the node before the tail.
        3. Disconnect the last node.

        Time Complexity: O(n)
        """

        # If the list is empty, nothing to delete
        if self.head.next is self.tail:
            return

        prev_node = self.head
        current = self.head.next

        while current.next is not self.tail:
            prev_node = current
            current = current.next

        prev_node.next = self.tail


    def print_list(self):
        """
        Print all values in the linked list.

        Algorithm:
        Traverse from the first real node until reaching the dummy tail.

        Time Complexity: O(n)
        """

        current = self.head.next

        # Stop when we reach the dummy tail
        while current is not self.tail:
            print(current.data, end=" ")
            current = current.next

        print()


# ----------------------------------------------------------
# Example usage demonstrating ALL LinkedList operations
# ----------------------------------------------------------

linked_list = LinkedList()

print("Initial list:")
linked_list.print_list()


# ----------------------------------------------------------
# add_at_head
# ----------------------------------------------------------
print("\nAdding nodes at head:")
linked_list.add_at_head(Node(10))
linked_list.add_at_head(Node(20))
linked_list.add_at_head(Node(30))

# List should now be: 30 20 10
linked_list.print_list()


# ----------------------------------------------------------
# add_at_tail
# ----------------------------------------------------------
print("\nAdding nodes at tail:")
linked_list.add_at_tail(Node(40))
linked_list.add_at_tail(Node(50))

# List should now be: 30 20 10 40 50
linked_list.print_list()


# ----------------------------------------------------------
# add_at_index
# ----------------------------------------------------------
print("\nInsert at index 2:")
linked_list.add_at_index(2, Node(99))

# List should now be: 30 20 99 10 40 50
linked_list.print_list()


# ----------------------------------------------------------
# get_node
# ----------------------------------------------------------
print("\nGet node at index 3:")
node = linked_list.get_node(3)

if node:
    print("Value:", node.data)


# ----------------------------------------------------------
# set_node
# ----------------------------------------------------------
print("\nUpdate value at index 1:")
linked_list.set_node(1, 111)

# List should now be: 30 111 99 10 40 50
linked_list.print_list()


# ----------------------------------------------------------
# delete_node_index
# ----------------------------------------------------------
print("\nDelete node at index 2:")
linked_list.delete_node_index(2)

# List should now be: 30 111 10 40 50
linked_list.print_list()


# ----------------------------------------------------------
# delete_head
# ----------------------------------------------------------
print("\nDelete head:")
linked_list.delete_head()

# List should now be: 111 10 40 50
linked_list.print_list()


# ----------------------------------------------------------
# delete_tail
# ----------------------------------------------------------
print("\nDelete tail:")
linked_list.delete_tail()

# List should now be: 111 10 40
linked_list.print_list()