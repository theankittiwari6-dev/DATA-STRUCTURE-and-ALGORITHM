class Solution:
    def PostfixToinfix(self, s):
     stack = []
     for ch in s:
          if ("a" <= ch <= "z") or ("A" <= ch <= "Z") or ("0" <= ch <= "9"):
               stack.append(ch)
          else:
              operand1 = stack.pop()
              operand2 = stack.pop()

              new_exp = f"({operand2}{ch}{operand1})"

              stack.append(new_exp)
     return stack.pop()

     
          
          
          

                
            
        