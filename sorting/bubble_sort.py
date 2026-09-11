# for assending order 
nums  = [2,453,5,67,89,43,3,6,6,4,4,4544,5,4,5,4]

# n = len(nums)

# for i in range (n-2,-1,-1):
#      for j in range(0,i+1):
#           if nums[j] > nums[j+1]:
#                nums[j],nums[j+1]=nums[j+1],nums[j]
#      print(nums)


# # for decending order 

# for i in range (n-2,-1,-1):
#      for j in range (0,i+1):
#           if nums[j]<nums[j+1]:
#                nums[j],nums[j+1]=nums[j+1],nums[j]
#      print(nums)


# using function 

def bubble_sort(nums):
     n = len(nums)
     for i in range (n-2,-1,-1):
          for j in range (0,i+1):
               if nums[j]<nums[j+1]:
                   nums[j],nums[j+1]=nums[j+1],nums[j]
     print(nums)


bubble_sort(nums)