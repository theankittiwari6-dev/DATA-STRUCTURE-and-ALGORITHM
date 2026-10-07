class Solution:
     def preToInfix(self, s):
          stack = []
          for ch in s[::-1]:
               if ch.isalnum():
                    stack.append(ch)
               else:
                    operand1 = stack.pop()
                    operand2 = stack.pop()
                
                    new_exp = f"({operand1}{ch}{operand2})"
                
                    stack.append(new_exp)
        
          return stack[-1]





class Solution:
     def preToInfix(self, s):
          stack = []
          n = len(s)
          for i in range(n-1,-1,-1):
               ch = s[i]
               if ch.isalnum():
                    stack.append(ch)
               else:
                    operand1 = stack.pop()
                    operand2 = stack.pop()
                
                    new_exp = f"({operand1}{ch}{operand2})"
                
                    stack.append(new_exp)
        
          return stack[-1]