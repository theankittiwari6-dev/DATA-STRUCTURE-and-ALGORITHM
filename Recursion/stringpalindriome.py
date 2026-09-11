# using loop 

# s = "nitin"
# l = 0
# r = len(s)-1

# while l<r:
#      if s[l] != s[r]:
#           print("false")
#           break
#           l + 1, r - 1
#      else:
#           print("true")
#           break



# using recursion 

def fun(s , l , r):
     if l>=r:
          return True
     if s[l] != s[r]:
          return False
     return fun(s,l+1,r-1)
s= "nitin"
print(fun(s,0,len(s)-1))


     
     
     
     


