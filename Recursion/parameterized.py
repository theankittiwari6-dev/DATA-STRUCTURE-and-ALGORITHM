# recusion using parameter 


# print name n times using head recursion

# def fun(x,n):
#      if n==0:
#           return
#      print("ankit")
#      fun(x,n-1)

# fun("ankit",10)


# print name n times using tail recursion 

def fun(x,n):
     if n==0:
          return
     fun(x,n-1)
     print("ankit")
     

fun("ankit",10)
