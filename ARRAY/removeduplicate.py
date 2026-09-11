# in place 
# brute force 


nums  = [ 1,1,1,2,2,2,3,3,4,4,4,5,5,5,6,7,8,8,8,9,9]
# frq_map = {}
# n = len(nums)

# for i in range(0,n):
#      frq_map [nums[i]] = 0

# j = 0

# for k in frq_map:
#      nums[j]=k
#      j+=1

# print(j)



# optimal solution 

n = len(nums)
if n==1:
     print(1)
i=0
j=i+1

while j<n:
     if nums[j]!=nums[i]:
          i+=1
          nums[i],nums[j]=nums[j],nums[i]
     j+=1
print(i+1)

                     




