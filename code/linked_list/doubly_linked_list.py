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
    - Dummy (sentinel) tail node
    - prev pointers for reverse traversal and O(1) deletion by reference
    """

    def __init__(self):
        # head is a dummy/sentinel node.
        # The first real node is stored at head.next.
        # If head.next is tail, the list is empty.
        self.head = Node()

        # tail is also a dummy/sentinel node
        # This replaces the need for None at the end of the list.
        # The last real node will always be stored at tail.prev.
        self.tail = Node()

        # Connect the two sentinel nodes
        # head <-> tail represents an empty list
        self.head.next = self.tail
        self.tail.prev = self.head


    def is_empty(self):
        return self.head.next is self.tail


    def add_at_tail(self, data):
        """
        Append a node to the end of the list.

        Algorithm:
        1. The new node is inserted before the dummy tail node.
        2. The previous last node is stored in tail.prev.
        3. Connect the new node between (tail.prev) and (tail).

        Time Complexity: O(1)
        """

        node = Node(data)

        # The node before insertion
        # head <-> A <-> B <-> tail
        #                ^
        #            prev_node

        prev_node = self.tail.prev
        next_node = self.tail

        # Insert node between prev_node and next_node
        node.next = next_node
        node.prev = prev_node

        next_node.prev = node
        prev_node.next = node

    
    def add_at_head(self, data):
        """
        Insert a node at the beginning of the list.

        Algorithm:
        1. The new node is inserted after the dummy head node.
        2. The first real node is stored in head.next.
        3. Connect the new node between (head) and (head.next).

        Time Complexity: O(1)
        """

        # Example before:
        # head <-> A <-> B <-> tail
        #
        # After inserting X:
        # head <-> X <-> A <-> B <-> tail

        node = Node(data)

        prev_node = self.head
        next_node = self.head.next

        node.next = next_node
        node.prev = prev_node

        next_node.prev = node
        prev_node.next = node


    def add_at_index(self, index, data):
        """
        Insert a node at the specified index.

        Algorithm:
        1. Traverse the list until reaching the node currently at position `index`.
        2. Insert the new node BEFORE that node.
        3. If index equals the list length, insertion occurs before the dummy tail.

        Time Complexity: O(n)
        """

        if index < 0:
            return
        
        node = Node(data)

        current = self.head.next

        # Traverse forward until reaching the desired index
        for _ in range(index):
            if current is self.tail:
                return
            current = current.next

        # current now points to the node currently at position "index"
        # The new node will be inserted BEFORE current

        prev_node = current.prev
        next_node = current

        node.next = next_node
        node.prev = prev_node

        next_node.prev = node
        prev_node.next = node


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
            return None

        current = self.head.next

        # Move forward index times
        # Each iteration moves one node ahead
        for _ in range(index):
            if current is self.tail:
                # With a dummy tail, reaching the tail means
                # we ran out of real nodes
                return None
            current = current.next

        if current is self.tail:
            return None

        # current now points to the node at the requested index
        return current


    def set_node(self, index, data):
        """
        Update the data stored in the node at the given index.

        Algorithm:
        1. Retrieve the node at the given index.
        2. Replace the data stored in that node.

        Time Complexity: O(n)
        """

        node = self.get_node(index)

        if node:
            node.data = data


    def delete_node_index(self, index):
        """
        Delete the node at the given index.

        Algorithm:
        1. Traverse to the node at the given index.
        2. Store references to the nodes before and after it.
        3. Update pointers so the previous node skips the deleted node.
        4. Fix the backward pointer of the next node.

        Time Complexity: O(n)
        """

        if index < 0:
            return

        # Start at the first real node
        # (self.head is a dummy/sentinel node)
        current = self.head.next

        for _ in range(index):
            if current is self.tail:
                return
            current = current.next

        if current is self.tail:
            return

        # Store references to the nodes before and after
        # the node being deleted
        prev_node = current.prev
        next_node = current.next

        # Skip over the node being deleted
        prev_node.next = next_node

        # With a dummy tail, next_node always exists
        # so we can safely update prev without checking for None
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
        if node is self.head or node is self.tail:
            return

        prev_node = node.prev
        next_node = node.next

        # Skip over the node being deleted
        prev_node.next = next_node

        # With a dummy tail, next_node is guaranteed to exist
        next_node.prev = prev_node


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

        if self.is_empty():
            return

        first = self.head.next

        self.head.next = first.next
        first.next.prev = self.head


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

        if self.is_empty():
            return

        last = self.tail.prev

        self.tail.prev = last.prev
        last.prev.next = self.tail


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


    def print_reverse(self):
        """
        Print the linked list in reverse order.

        Algorithm:
        1. Start at the tail.
        2. Traverse backwards using prev pointers.
        3. Stop when reaching the sentinel head.

        Time Complexity: O(n)
        """

        # Start from the last real node
        current = self.tail.prev

        while current is not self.head:
            print(current.data, end=" ")
            current = current.prev

        print()



# ----------------------------------------------------------
# Example usage demonstrating ALL LinkedList operations
# ----------------------------------------------------------
if __name__ == "__main__":
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
    # delete_node_reference
    # ----------------------------------------------------------
    print("\nDelete node by reference:")

    node_to_delete = linked_list.get_node(3)
    linked_list.delete_node_reference(node_to_delete)

    # List should now be: 30 111 10 50
    linked_list.print_list()


    # ----------------------------------------------------------
    # delete_head
    # ----------------------------------------------------------
    print("\nDelete head:")
    linked_list.delete_head()

    # List should now be: 111 10 50
    linked_list.print_list()


    # ----------------------------------------------------------
    # delete_tail
    # ----------------------------------------------------------
    print("\nDelete tail:")
    linked_list.delete_tail()

    # List should now be: 111 10
    linked_list.print_list()


    # ----------------------------------------------------------
    # print_reverse
    # ----------------------------------------------------------
    print("\nReverse order:")
    linked_list.print_reverse()