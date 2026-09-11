# sum of 1 to n using parameerized recursion 

def fun(sum,x,n):
     if x>n:
          print(sum)
          return
     fun(sum+x,x+1,n)

fun(0,1,98)



# sum of 1 to n using funcional recursion

# def fun(n):
#      if n == 0:
#           return 0
#      return n + fun(n-1)

# print(fun(10))