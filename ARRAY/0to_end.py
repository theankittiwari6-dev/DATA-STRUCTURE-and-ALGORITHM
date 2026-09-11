# brute force 

nums = [2,3,4,6,0,5,8,9,0,0,3,4,5,6]

# n = len(nums)
# arr = []

# for i in range(0,n):
#      if nums[i] != 0:
#           arr.append(nums[i])

# z = len(arr)
# for i in range(0,z):
#      nums[i]=arr[i]
# for i in range(z,n):
#      nums[i]=0

# print
# (nums)


# optimal solution 
def move_zeros(nums):
     if len(nums)==1:
          return

     n = len(nums)

     i = 0

     while i<n:
          if nums[i]==0:
               break
          i+=1

     if i == len(nums):
          return
     j = i+1

     while j<n:
          if nums[j]!=0:
               nums[i],nums[j]=nums[j],nums[i]
               i+=1
          j+=1
     return print(nums)

move_zeros(nums) 



     
