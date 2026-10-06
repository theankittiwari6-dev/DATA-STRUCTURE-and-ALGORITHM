class Queue:
     def __init__(self):
          self.item = []

     def is_empty(self):
          return len(self.item) == 0


     def enqueue(self, el):
          self.item.append(el)

     def dequeue(self):
          if len(self.item) == 0:
               return "queue is empty"
          x = self.item.pop(0)
          return x

     def size(self):
          return len(self.item)

     def front(self):
          if len(self.item) == 0:
               return "queue is empty"
          return self.item[0]

     def rear(self):
          if len(self.item) == 0:
               return "queue is empty"
          return self.item[-1]


Queue = Queue()

Queue.enqueue(21)
Queue.enqueue(34)
Queue.enqueue(25)
Queue.enqueue(78)
Queue.enqueue(34)
Queue.enqueue(12)
Queue.dequeue()
Queue.dequeue()

print(Queue.item)
print(Queue.rear())


