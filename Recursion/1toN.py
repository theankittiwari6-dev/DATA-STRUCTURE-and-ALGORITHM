# print n to n using recursion 


# def fun(x,n):
#      if x>n:
#           return
#      print(x)
#      fun(x+1,n)

# fun(100,1000)



# print n to 1 


def fun(n):
     if n==0:
          return
     print(n)
     fun(n-1)

fun(123)