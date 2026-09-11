n = 153
num = n
count = 0
while num > 0:
     count += 1
     num = num//10

num = n
total = 0
while num > 0:
     ld = num%10
     total = total+(ld**count)
     num = num//10

if n == total:
     print("armstrong num")
else:
     print("not a armstrong")


