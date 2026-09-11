# hashing is technique to store and retrive data very quickly
# q1. 

n = [2, 5, 7, 2, 9, 1, 5, 8, 2, 6]
m = [4, 2, 6, 9, 2, 7, 4, 1, 8, 2]
# constraint
# 1<=n<=10
# brute force

# for i in m:
#      count = 0
#      for j in n:
#           if j == i:
#                count += 1

# print(count)




# optimal solution using list

# hash_list = [0]*11

# for i in n:
#      hash_list[i] += 1
# for j in m:
#      if j < 1 or j > 10:
#           print(0)
#      else:
#           print(hash_list[j])     



# solution using dict

freq_map = dict()

for x in n:
     if x in freq_map:
          freq_map[x]+=1
     else:
          freq_map[x]=1

for x in m:
     if x in freq_map:
          print(freq_map[x])
     else:
          print(0)