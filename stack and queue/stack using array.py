class stack:
     def __init__(self):
          self.item = []

     def is_empty(self):
          return len(self.item) == 0

     def push(self, el):
          self.item.append(el)

     def pop(self):
          if len(self.item) == 0:
               return "stack is empty"
          x = self.item.pop()
          return x

     def top(self):
          if len(self.item) == 0:
               return "stack is empty"
          return self.item[-1]

     def size(self):
          return len(self.item)



stack = stack()
stack.push(10)
stack.push(11)
stack.push(35)

print(stack.item)