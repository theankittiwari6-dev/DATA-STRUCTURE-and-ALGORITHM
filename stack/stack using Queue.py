from collections import deque
class stack:
     def __init__(self):
          self.queue = deque()

     def push(self, item):
          self.queue.append(item)
          for _ in range(len(self.queue) - 1):
               self.queue.append(self.queue.popleft())

     def pop(self):
          if len(self.queue)== 0:
               return "'stack is empty"  
          return self.queue.popleft()

     def peek(self):
          if len(self.queue)== 0:
               return "'stack is empty"  
          return self.queue[0]


stack = stack()
stack.push(90)
stack.push(90)
stack.push(90)
stack.push(90)
stack.push(90)
stack.pop()
stack.pop()
stack.pop()
stack.pop()

print(stack.queue)
     

