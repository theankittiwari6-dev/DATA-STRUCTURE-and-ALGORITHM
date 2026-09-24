class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_beginning(self, data):
        new_node = Node(data)

        if self.head is not None:
            new_node.next = self.head
            self.head.prev = new_node

        self.head = new_node

    # Insert at end
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    # Delete a node
    def delete(self, data):
        temp = self.head

        while temp is not None:
            if temp.data == data:

                # If deleting head
                if temp.prev is None:
                    self.head = temp.next

                    if self.head is not None:
                        self.head.prev = None

                else:
                    temp.prev.next = temp.next

                    if temp.next is not None:
                        temp.next.prev = temp.prev

                return

            temp = temp.next

        print("Element not found")

    # Display forward
    def display_forward(self):
        temp = self.head

        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("None")

    # Display backward
    def display_backward(self):
        temp = self.head

        if temp is None:
            return

        # Go to last node
        while temp.next is not None:
            temp = temp.next

        # Traverse backwards
        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.prev

        print("None")