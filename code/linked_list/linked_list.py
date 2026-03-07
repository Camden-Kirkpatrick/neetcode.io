class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, head):
        self.head = head

    def add_node(self, node):
        current = self.head
        while current:
            if not current.next:
                current.next = node
                break
            else:
                current = current.next
    
    def get_node(self, index):
        if index < 0:
            print("Index must be greater than -1")
            return
        
        current = self.head
        for _ in range(index):
            if current is None:
                print("Invalid index")
                return
            current = current.next
        
        return current

    def set_node(self, index, value):
        if index < 0:
            print("Index must be greater than -1")
            return
        
        current = self.head
        for _ in range(index):
            if current is None:
                print("Invalid index")
                return
            current = current.next

        current.data = value

    def delete_node(self, index):
        if index < 0:
            print("Index must be greater than -1")
            return
        if not self.head:
            print("Linked list is empty")
            return
        if index == 0:
            self.head = self.head.next
            return

        current = self.head
        for _ in range(index - 1):
            current = current.next
            if current is None:
                print("Invalid index")
                return

        if current.next is None:
            print("Invalid index")
            return
        
        current.next = current.next.next
    
    def print_list(self):
        current = self.head
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

linked_list.delete_node(4)
linked_list.print_list()