# Go to "\code", then run: python -m queue.queue

from linked_list.doubly_linked_list import LinkedList, Node


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
        self.items = LinkedList()


    def is_empty(self):
        return self.items.head.next is self.items.tail


    def enqueue(self, data):
        """
        Add a value to the back of the queue.

        Algorithm:
        1. Wrap the value in a Node.
        2. Append that node to the tail of the linked list.

        Time Complexity: O(1)
        """
        self.items.add_at_tail(data)


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
            return

        first = self.items.head.next
        self.items.delete_head()
        return first.data


    def print_queue(self):
        """
        Print the queue from front to back.

        Time Complexity: O(n)
        """
        self.items.print_list()



if __name__ == "__main__":
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    q.print_queue()

    first = q.dequeue()
    print("first:", first)

    first = q.dequeue()
    print("first:", first)

    first = q.dequeue()
    print("first:", first)