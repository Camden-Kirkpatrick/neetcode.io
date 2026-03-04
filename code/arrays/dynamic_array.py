# Implementation of a Dynamic Array

class DynamicArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.length = 0
        self.arr = [None] * capacity
        print("array created")

    def is_full(self):
        return self.length == self.capacity

    def is_empty(self):
        return self.length == 0

    def resize(self):
        """
        Double the capacity of the array.
        """
        new_capacity = 2 * self.capacity
        new_arr = [None] * new_capacity

        for i in range(self.length):
            new_arr[i] = self.arr[i]

        self.arr = new_arr
        self.capacity = new_capacity
        print("Array resized")

    def add(self, value, i=None):
        """
        Insert value at index (default: end).
        """
        if i is None:
            i = self.length

        if self.is_full():
            self.resize()

        self.arr[i] = value
        print(value, "was added to the array")
        self.length += 1

    def print_array(self):
        print("Array: ", end="")
        for i in range(self.length):
            print(self.arr[i], end=" ")
        print()

    def insert_at(self, index, value):
        """
        Insert at specific index.
        """
        if index < 0 or index > self.length:
            print("Invalid index")
            return

        if self.is_full():
            self.resize()

        for i in range(self.length - 1, index - 1, -1):
            self.arr[i + 1] = self.arr[i]

        self.add(value, index)

    def insert_start(self, value):
        """
        Insert at beginning.
        """
        if self.is_full():
            self.resize()

        for i in range(self.length - 1, -1, -1):
            self.arr[i + 1] = self.arr[i]

        self.add(value, 0)

    def insert_end(self, value):
        """
        Insert at end (append).
        """
        self.add(value)

    def delete_at(self, index):
        """
        Delete element at index.
        """
        if index < 0 or index >= self.length:
            print("Invalid index")
            return

        if self.is_empty():
            print("Can't delete from empty array")
            return

        for i in range(index, self.length - 1):
            self.arr[i] = self.arr[i + 1]

        self.length -= 1
        self.arr[self.length] = None

    def delete_start(self):
        """
        Delete first element.
        """
        if self.is_empty():
            print("Can't delete from empty array")
            return

        for i in range(self.length - 1):
            self.arr[i] = self.arr[i + 1]

        self.length -= 1
        self.arr[self.length] = None

    def delete_end(self):
        """
        Delete last element.
        """
        if self.is_empty():
            print("Can't delete from empty array")
            return

        self.length -= 1
        self.arr[self.length] = None


arr = DynamicArray(2)

arr.add(20)
arr.add(74)
arr.print_array()

print()

arr.add(99)
arr.print_array()

print()

arr.insert_at(1, 10)
print("After inserting '10':")
arr.print_array()

print()

arr.insert_start(-16)
print("After inserting '-16' at the start:")
arr.print_array()

print()

arr.insert_end(0)
print("After inserting '0' at the end:")
arr.print_array()

print()

arr.delete_at(2)
print("After removing the third element:")
arr.print_array()

print()

arr.delete_start()
print("After removing the first element:")
arr.print_array()

print()

arr.delete_end()
print("After removing the last element:")
arr.print_array()