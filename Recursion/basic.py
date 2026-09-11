# simple function
# def fun():
#      print("ankit tiwari")
#      return

# fun()


# Recursion without parameter
# it is also known as head recursion 
# in this function is used after the statement 

# count = 0
# def fun():
#      global count
#      if count == 4:
#           return
#      print("ankit")
#      count +=1
#      fun()
 
# fun()



# tail Recursion 
# in this fun is used before the statement 


count = 0
def fun():
     global count
     if count == 4:
          return
     count += 1
     fun()
     print("ankit")

fun()