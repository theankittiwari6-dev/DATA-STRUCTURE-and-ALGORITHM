# # brute force
# n = 216
# num = n
# factor = [ ]

# for i in range (1, num+1):
#      if num%i == 0:
#           factor.append(i)

# print(factor) 




# # better approach
# n = 216
# num = n 
# result = []

# for i in range(1,int(num/2)+1):
#      if num%i == 0:
#           result.append(i)

# result.append(n)
# print(result)





# optimal solution
from math import sqrt
n = 216
num = n
result = []

for i in range (1,int(sqrt(num))+1):
     if num%i == 0:
          result.append(i)
          if num//i != 0:
               result.append(num//i)

print(result)