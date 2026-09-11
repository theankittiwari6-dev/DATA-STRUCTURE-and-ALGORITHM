# rotate a array by one place 

nums = [1,2,3,4,5,6,7,8,9]
# using slicing 

# n = len(nums)
# nums[:] = nums[n-1:]+nums[0:n-1]
# print(nums)

# without slicing 
# n = len(nums)
# tem = nums[n-1]

# for i in range(n-2,-1,-1):
#      nums[i+1] = nums[i]
# nums[0] = tem     

# print(nums)


# rotate an array by k place 
# brute force 
# n = len(nums)
# k = int(input("enter k: "))
# x = k % n
# for _ in range (0,x):
#      e = nums.pop()
#      nums.insert(0,e)

# print(nums)



# right rotate array by k places 
# bettet solutin using slicing 


# k = 23
# n = len(nums)
# k = k%n
# nums[:] = nums[n-k:]+nums[:n-k]
# print(nums)


# optimal solution 
k = 234
n = len(nums)
k = n%k
def reverse(nums, left, right):
     while left<right:
          nums[left],nums[right]=nums[right],nums[left]
          left +=1
          right -+1

reverse(nums,n-k,n-1)
reverse(nums,0,n-k-1)
reverse(nums,0,n-1)

reverse(nums,0,n-1)
print(nums)