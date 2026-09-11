n = 123321
num = n
result = 0
while num>0:
     ld = num%10
     result= (result*10)+ld
     num = num//10

if n==result:
     print("palindrome")
else:
     print("not a palindrome")  