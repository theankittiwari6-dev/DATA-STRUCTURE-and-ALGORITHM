# # wihout hashing
# nums = [3,34,34,4,33,23,2,23,2,2,23,2,2]

# frq_map = dict()

# for i in range (0, len(nums)):
#      if nums[i] in frq_map:
#           frq_map[nums[i]]+=1
#      else:
#           frq_map[nums[i]]=1

# print(frq_map)



# with hashing
nums = [3,34,34,4,33,23,2,23,2,2,23,2,2]
n = len(nums)
hash_map = dict()

for i in range (0,n):
     hash_map[nums[i]] = hash_map.get(nums[i],0)+1

print(hash_map)
