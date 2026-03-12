# Go to "\code", then run: python -m deque.deque

from linked_list.doubly_linked_list import LinkedList


class Deque:
    """
    Deque implementation using the doubly linked list
    defined in doubly_linked_list.py.

    Deque rule:
    - enqueue_front adds at the head
    - enqueue_back adds at the tail
    - dequeue_front removes from the head
    - dequeue_back removes from the tail

    Because the linked list uses dummy head and tail nodes,
    all adding and deleting run in O(1) time.
    """

    def __init__(self):
        self.data = LinkedList()

    
    def size(self):
        return self.data.size()
    

    def __len__(self):
        return self.data.size()


    def is_empty(self):
        return self.data.head.next is self.data.tail
    

    def enqueue_front(self, data):
        """
        Add a value to the front of the Deque.


        Time Complexity: O(1)
        """
        self.data.add_at_head(data)


    def enqueue_back(self, data):
        """
        Add a value to the back of the Deque.

        Time Complexity: O(1)
        """
        self.data.add_at_tail(data)


    def dequeue_front(self):
        """
        Remove and return the value at the front of the Deque.

        Algorithm:
        1. Check if the Deque is empty.
        2. Read the first real node (head.next).
        3. Delete the head node from the linked list.
        4. Return the removed value.

        Time Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Cannot dequeue from empty Deque")

        first = self.data.head.next
        self.data.delete_head()
        return first.data
    

    def dequeue_back(self):
        """
        Remove and return the value at the end of the Deque.

        Algorithm:
        1. Check if the Deque is empty.
        2. Read the last real node (tail.prev).
        3. Delete the tail node from the linked list.
        4. Return the removed value.

        Time Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Cannot dequeue from empty Deque")

        last = self.data.tail.prev
        self.data.delete_tail()
        return last.data


    def print_deque(self):
        """
        Print the Deque from front to back.

        Time Complexity: O(n)
        """
        self.data.print_list()



if __name__ == "__main__":
    print("===== BASIC DEQUE OPERATIONS =====")
    d = Deque()

    print("Initial deque:")
    d.print_deque()
    print("Size:", d.size())
    print()

    d.enqueue_front(10)
    d.enqueue_front(20)
    d.enqueue_back(30)
    d.enqueue_back(40)

    print("After enqueue_front 10, 20 and enqueue_back 30, 40:")
    d.print_deque()
    print("d.size():", d.size())
    print("len(d):", len(d))
    print()

    first = d.dequeue_front()
    print("Dequeued from front:", first)
    d.print_deque()
    print()

    last = d.dequeue_back()
    print("Dequeued from back:", last)
    d.print_deque()
    print()

    print("Dequeued from front:", d.dequeue_front())
    print("Dequeued from back:", d.dequeue_back())
    d.print_deque()

    print("===== ERROR HANDLING EXAMPLES =====")

    try:
        print("Trying to dequeue_front from empty deque:")
        print(d.dequeue_front())
    except IndexError as e:
        print("Error:", e)

    try:
        print("Trying to dequeue_back from empty deque:")
        print(d.dequeue_back())
    except IndexError as e:
        print("Error:", e)

    print()
    print("===== LINKED LIST ERROR TEST =====")

    try:
        print("Trying to delete head from empty underlying linked list:")
        d.data.delete_head()
    except IndexError as e:
        print("Error:", e)

    try:
        print("Trying to delete tail from empty underlying linked list:")
        d.data.delete_tail()
    except IndexError as e:
        print("Error:", e)

    try:
        print("Trying to get an invalid node from underlying linked list:")
        d.data.get_node(0)
    except IndexError as e:
        print("Error:", e)

    print()
    print("===== MORE DEQUE TESTING =====")

    d2 = Deque()
    d2.enqueue_front(100)
    d2.enqueue_back(200)
    d2.enqueue_front(50)
    d2.enqueue_back(300)

    print("Deque 2 after mixed enqueue operations:")
    d2.print_deque()

    print("Dequeued from front:", d2.dequeue_front())
    print("Dequeued from back:", d2.dequeue_back())

    print("Deque 2 now:")
    d2.print_deque()

    d2.enqueue_front(25)
    d2.enqueue_back(400)

    print("After enqueue_front 25 and enqueue_back 400:")
    d2.print_deque()

    print("Dequeued from front:", d2.dequeue_front())
    print("Dequeued from back:", d2.dequeue_back())

    try:
        d2.dequeue_front()
        d2.dequeue_front()
        d2.dequeue_front()
    except IndexError as e:
        print("Error:", e)