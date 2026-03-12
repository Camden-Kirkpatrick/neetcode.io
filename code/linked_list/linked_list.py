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

        self.length = 0


    def size(self):
        return self.length
    

    def __len__(self):
        return self.length


    def is_empty(self):
        return self.head.next is self.tail


    def add_at_tail(self, data):
        """
        Append a node to the end of the list.

        Algorithm:
        1. The new node is inserted before the dummy tail node.
        2. Traverse until reaching the node before the tail.
        3. Connect the new node between (prev_node) and (tail).

        Time Complexity: O(n)
        """

        node = Node(data)

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

        node.next = next_node
        prev_node.next = node

        self.length += 1


    def add_at_head(self, data):
        """
        Insert a node at the beginning of the list.

        Algorithm:
        1. The new node is inserted after the dummy head node.
        2. The first real node is stored in head.next.
        3. Connect the new node between (head) and (head.next).

        Time Complexity: O(1)
        """

        node = Node(data)

        # Example before:
        # head -> A -> B -> tail
        #
        # After inserting X:
        # head -> X -> A -> B -> tail

        prev_node = self.head
        next_node = self.head.next

        node.next = next_node
        prev_node.next = node

        self.length += 1


    def add_at_index(self, index, data):
        """
        Insert a node at the specified index.

        Algorithm:
        1. Traverse the list until reaching the node currently at position `index`.
        2. Insert the new node BEFORE that node.
        3. If index equals the list length, insertion occurs before the dummy tail.

        Time Complexity: O(n)
        """

        if index < 0 or index > self.length:
            raise IndexError("Invalid index")
        
        node = Node(data)

        prev_node = self.head
        current = self.head.next

        # Traverse forward until reaching the desired index
        for _ in range(index):
            if current is self.tail:
                raise IndexError("Invalid index")
            prev_node = current
            current = current.next

        # current now points to the node currently at position "index"
        # The new node will be inserted BEFORE current

        next_node = current

        node.next = next_node
        prev_node.next = node

        self.length += 1


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

        if index < 0 or index >= self.length:
            raise IndexError("Invalid index")

        current = self.head.next

        # Move forward index times
        # Each iteration moves one node ahead
        for _ in range(index):
            if current is self.tail:
                raise IndexError("Invalid index")
            current = current.next

        if current is self.tail:
            raise IndexError("Invalid index")

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
        node.data = data


    def delete_at_index(self, index):
        """
        Delete the node at the given index.

        Algorithm:
        1. Traverse to the node at the given index.
        2. Store references to the nodes before and after it.
        3. Update pointers so the previous node skips the deleted node.

        Time Complexity: O(n)
        """

        if index < 0 or index >= self.length:
            raise IndexError("Invalid index")

        # Start at the first real node
        # (self.head is a dummy/sentinel node)
        prev_node = self.head
        current = self.head.next

        # Traverse forward until reaching the desired index
        for _ in range(index):
            if current is self.tail:
                raise IndexError("Invalid index")
            prev_node = current
            current = current.next

        if current is self.tail:
            raise IndexError("Invalid index")

        # Store references to the nodes before and after
        # the node being deleted
        next_node = current.next

        # Skip over the node being deleted
        # prev_node -> current -> next_node
        # becomes
        # prev_node -> next_node
        prev_node.next = next_node

        self.length -= 1


    def delete_head(self):
        """
        Delete the first real node (head.next).

        Algorithm:
        1. Check if the list is empty.
        2. Store the first real node.
        3. Move head.next to the second node.

        Time Complexity: O(1)
        """

        if self.is_empty():
            raise IndexError("Cannot delete from empty list")

        first = self.head.next

        self.head.next = first.next

        self.length -= 1


    def delete_tail(self):
        """
        Delete the last real node in the list.

        Algorithm:
        1. Check if the list is empty.
        2. Traverse to the node before the tail.
        3. Disconnect the last node.

        Time Complexity: O(n)
        """

        if self.is_empty():
            raise IndexError("Cannot delete from empty list")

        prev_node = self.head
        current = self.head.next

        while current.next is not self.tail:
            prev_node = current
            current = current.next

        prev_node.next = self.tail

        self.length -= 1


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
if __name__ == "__main__":
    linked_list = LinkedList()

    print("Initial list:")
    linked_list.print_list()
    print("Size:", linked_list.size())
    print()

    print("===== INSERT OPERATIONS =====")

    linked_list.add_at_head(10)
    linked_list.add_at_head(20)
    linked_list.add_at_head(30)

    print("After adding 10, 20, and 30 at head:")
    linked_list.print_list()
    print("linked_list.size():", linked_list.size())
    print("len(linked_list):", len(linked_list))
    print()

    linked_list.add_at_tail(40)
    linked_list.add_at_tail(50)

    print("After adding 40 and 50 at tail:")
    linked_list.print_list()
    print()

    linked_list.add_at_index(2, 99)

    print("After inserting 99 at index 2:")
    linked_list.print_list()
    print()

    print("===== ACCESS / UPDATE =====")

    node = linked_list.get_node(3)
    print("Value at index 3:", node.data)
    print()

    linked_list.set_node(1, 111)

    print("After setting index 1 to 111:")
    linked_list.print_list()
    print()

    print("===== DELETE OPERATIONS =====")

    linked_list.delete_at_index(2)

    print("After deleting index 2:")
    linked_list.print_list()
    print()

    linked_list.delete_head()

    print("After deleting head:")
    linked_list.print_list()
    print()

    linked_list.delete_tail()

    print("After deleting tail:")
    linked_list.print_list()
    print()

    print("===== ERROR HANDLING EXAMPLES =====")

    try:
        linked_list.get_node(100)
    except IndexError as e:
        print("Error:", e)

    try:
        linked_list.set_node(-1, 500)
    except IndexError as e:
        print("Error:", e)

    try:
        linked_list.add_at_index(100, 42)
    except IndexError as e:
        print("Error:", e)

    try:
        linked_list.delete_at_index(100)
    except IndexError as e:
        print("Error:", e)

    empty_list = LinkedList()

    try:
        empty_list.delete_head()
    except IndexError as e:
        print("Error:", e)

    try:
        empty_list.delete_tail()
    except IndexError as e:
        print("Error:", e)