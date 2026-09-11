# assending order 
nums = [4,5,6,3,89,1,2,0,45,67,4,5]
n = len(nums)

for i in range (1, n):
     key = nums[i]
     j = i-1
     while j>=0 and nums[j]>key:
          nums[j+1]=nums[j]
          j-=1

     nums[j+1]=key
print(nums)