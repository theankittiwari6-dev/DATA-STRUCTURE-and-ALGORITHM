nums = [23,45,67,89,45,67,34,45]

largest = nums[0]
n = len(nums)

for i in range(0,n):
     if nums[i]>largest:
          largest = nums[i]

print(largest)

