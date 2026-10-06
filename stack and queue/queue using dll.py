class node:
     def __init__(self, data):
          self.data = data
          self.next = None
          self.prev = None

class Queue:
     def __init__(self):
          self.head = None
          self.tail = None
          self.count = 0

     def enqueue(self, data):
          new_node = node(data)

          if self.head is None:
               self.head = self. tail = new_node
          else:
               new_node.prev = self.tail
               self.tail.next = new_node
               self.tail = new_node

          self.count +=1

     def dequeue(self):
          if self.count == 0:
               return "stack is empty"
          data = self.head.data

          if self.head == self.tail:
               self.head = self.tail = None
          else:
               self.head = self.head.next
               self.head.prev = None

          self.count -=1
          return data


     def front(self):
          if self.count == 0:
               return "stack is empty"
          return self.head.data

     def rear(self):
          if self.count == 0:
               return "stack is empty"
          return self.tail.data
     
     def size(self):
          return self.count

     def display(self):
        current = self.head

        while current:
            print(current.data, end=" ")
            current = current.next

        print()


Queue = Queue()

Queue.enqueue(21)
Queue.enqueue(34)
Queue.enqueue(25)
Queue.enqueue(78)
Queue.enqueue(34)
Queue.enqueue(12)
Queue.dequeue()
Queue.dequeue()

print(Queue.display())
print(Queue.rear())
