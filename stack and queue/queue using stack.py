class Queue:
     def __init__(self):
          self.stack1 = []
          self.stack2 = []

     def enqueue(self, x):
          while self.stack1:
               self.stack2.append(self.stack1.pop())
          self.stack1.append(x)
          while self.stack2:
               self.stack1.append(self.stack2.pop())

     def dequeue(self):
          if len(self.stack1) == 0:
               return "queue is empty"
          return self.stack1.pop()

     def front(self):
          if len(self.stack1) == 0:
                    return "queue is empty"
          return self.stack1[0]

     
     def rear(self):
          if len(self.stack1) == 0:
               return "queue is empty"
          return self.stack1[-1]


Queue = Queue()

Queue.enqueue(21)
Queue.enqueue(34)
Queue.enqueue(25)
Queue.enqueue(78)
Queue.enqueue(34)
Queue.enqueue(12)
Queue.dequeue()
Queue.dequeue()

print(Queue.stack1)
print(Queue.rear())

          
          