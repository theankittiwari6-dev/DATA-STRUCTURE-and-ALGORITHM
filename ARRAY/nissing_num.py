nums = [0,1,2,3,4,6,7,8,9]

# breyte force 


# def fun(nums):
#      n = len(nums)
#      for i in range(0,n+1):
#           if i not in nums:
#                return i

# print(fun(nums))



# better solution 


# n = len(nums)
# freq = {}
# for i in range(0,n+1):
#      freq[i] = 0
# for i in nums:
#      freq[i] = 1
# for i,j in freq.items():
#      if j == 0:
#           print(i)


# optimal solution 



n = len(nums)
answer = (n*(n+1))/2  - sum(nums)
print(answer)