# # character hasing using list
s = "jchalsaahscgsbbbdbbshbbshbsbxbsv"
q = ['a', 'b','s','h','x']

# hash_list = [0]*26
# for ch in s:
#      ascii_val = ord(ch)
#      index = ascii_val-97
#      hash_list[index]+=1

# for ch in q:
#      ascii_val = ord(ch)
#      index = ascii_val-97
#      print(hash_list[index])






# character hashing in dict
freq_map = dict()

for ch in s:
     if ch in freq_map:
          freq_map[ch]+=1
     else:
          freq_map[ch]=1

for ch in q:
     if ch in freq_map:
          print(freq_map[ch])
     else:
          print(0)
