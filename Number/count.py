# n = 1234567890
# num = n
# count = 0
 
# while num > 0:
#      count+=1
#      num = num//10

# print(count)


from math import *

def countdigit(num):
     return int(log10(num)+1)

print(countdigit(1234567890))