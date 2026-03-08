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