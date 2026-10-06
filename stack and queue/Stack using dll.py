class node:
     def __init__(self, data):
          self.data = data
          self.next = None
          self.prev = None

class stack:
     def __init__(self):
          self.head = None
          self.tail = None
          self.count = 0

     def push(self, data):
          new_node = node(data)

          if self.head is None:
               self.head = self. tail = new_node
          else:
               new_node.prev = self.tail
               self.tail.next = new_node
               self.tail = new_node

          self.count +=1

     def pop(self):
          if self.count == 0:
               return "stack is empty"
          data = self.tail.data

          if self.head == self.tail:
               self.head = self.tail = None
          else:
               self.tail = self.tail.prev
               self.tail.next = None

          self.count -=1
          return data


     def peek(self):
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




stack = stack()
stack.push(90)
stack.push(90)
stack.push(90)
stack.push(90)
stack.push(90)
stack.pop()
stack.pop()
stack.pop()

print(stack.display())



