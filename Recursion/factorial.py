# factorial of n 

# def fun (fact,x,n):
#      if x>n:
#           print(fact)
#           return
#      fun(fact*x,x+1,n)

# fun(1,1,5)




# using functional recursion 

def fun (n):
     if n==0:
          return 1
     return n * fun(n-1)

print(fun(5))