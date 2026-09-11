# in brute force we can use sorting 

# better solotion /

nums = [23,45,67,89,99,88,67,77,79,97,34,0]
largest = float("-inf")
sec_largest = float("-inf")
n = len(nums)

for i in range(0,n):
     if nums[i]>largest:
          largest = nums[i]
     if nums[i]>sec_largest and nums[i]!=largest:
          sec_largest = nums[i]
print(sec_largest)



# # optimal solution 
# nums = [23,45,67,89,99,88,67,77,79,97,34,0]
# largest = float("-inf")
# sec_largest = float("-inf")
# n = len(nums)

# for i in range(0,n):
#      if nums[i]>largest:
#           sec_largest = largest
#           largest = nums[i]
#      elif nums[i]>sec_largest and nums[i]<largest:
#           sec_largest = nums[i]
# print(sec_largest)