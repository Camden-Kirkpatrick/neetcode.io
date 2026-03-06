class Node:
    
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
    def print_list(self):
        current = self
        while current:
            print(current.data, end=" ")
            current = current.next
        print()



n0 = Node(50)
n1 = Node(28)
n0.next = n1

n0.print_list()