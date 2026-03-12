# Go to "\code", then run: python -m queue.queue

from linked_list.doubly_linked_list import LinkedList


class Queue:
    """
    Queue implementation using the doubly linked list
    defined in doubly_linked_list.py.

    Queue rule:
    - enqueue adds at the tail
    - dequeue removes from the head

    Because the linked list uses dummy head and tail nodes,
    both enqueue and dequeue run in O(1) time.
    """

    def __init__(self):
        self.data = LinkedList()

    
    def size(self):
        return self.data.size()
    

    def __len__(self):
        return self.data.size()


    def is_empty(self):
        return self.data.head.next is self.data.tail


    def enqueue(self, data):
        """
        Add a value to the back of the queue.

        Algorithm:
        1. Wrap the value in a Node.
        2. Append that node to the tail of the linked list.

        Time Complexity: O(1)
        """
        self.data.add_at_tail(data)


    def dequeue(self):
        """
        Remove and return the value at the front of the queue.

        Algorithm:
        1. Check if the queue is empty.
        2. Read the first real node (head.next).
        3. Delete the head node from the linked list.
        4. Return the removed value.

        Time Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Cannot dequeue from empty queue")

        first = self.data.head.next
        self.data.delete_head()
        return first.data


    def print_queue(self):
        """
        Print the queue from front to back.

        Time Complexity: O(n)
        """
        self.data.print_list()



if __name__ == "__main__":
    print("===== BASIC QUEUE OPERATIONS =====")
    q = Queue()

    print("Initial queue:")
    q.print_queue()
    print("Size:", q.size())
    print()

    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    print("After enqueueing 10, 20, and 30:")
    q.print_queue()
    print("q.size():", q.size())
    print("len(q):", len(q))
    print()

    first = q.dequeue()
    print("Dequeued:", first)
    q.print_queue()
    print()

    first = q.dequeue()
    print("Dequeued:", first)
    q.print_queue()
    print()

    first = q.dequeue()
    print("Dequeued:", first)
    q.print_queue()

    print("===== ERROR HANDLING EXAMPLES =====")

    try:
        print("Trying to dequeue from empty queue:")
        print(q.dequeue())
    except IndexError as e:
        print("Error:", e)

    print()
    print("===== LINKED LIST ERROR TEST =====")

    try:
        print("Trying to delete head from empty underlying linked list:")
        q.data.delete_head()
    except IndexError as e:
        print("Error:", e)

    try:
        print("Trying to delete tail from empty underlying linked list:")
        q.data.delete_tail()
    except IndexError as e:
        print("Error:", e)

    try:
        print("Trying to get an invalid node from underlying linked list:")
        q.data.get_node(0)
    except IndexError as e:
        print("Error:", e)

    print()
    print("===== MORE QUEUE TESTING =====")

    q2 = Queue()
    q2.enqueue(100)
    q2.enqueue(200)
    q2.enqueue(300)

    print("Queue 2 after enqueueing 100, 200, 300:")
    q2.print_queue()

    print("Dequeued:", q2.dequeue())
    print("Dequeued:", q2.dequeue())

    print("Queue 2 now:")
    q2.print_queue()

    q2.enqueue(400)
    print("After enqueueing 400:")
    q2.print_queue()

    print("Dequeued:", q2.dequeue())
    print("Dequeued:", q2.dequeue())

    try:
        q2.dequeue()
    except IndexError as e:
        print("Error:", e)