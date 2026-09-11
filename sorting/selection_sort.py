# sorting an array using selection_sort in assending order 

def selection_sort(nums):
     n = len(nums)
     for i in range (0,n):
          min_ind = i
          for j in range (i+1, n):
               if nums[j]<nums[min_ind]:
                    min_ind = j

          nums[i],nums[min_ind]=nums[min_ind],nums[i]
          print(nums)

nums = [4,35,2,5,75,4,563,4567,4,356,4,33254534,4534]
selection_sort(nums)


# soring array into desending order 

def selection_sorta(nums):
     n = len(nums)
     for i in range (0,n):
          max_idx = i
          for j in range (i+1,n):
               if nums[j]>nums[max_idx]:
                    max_idx = j
          nums[i],nums[max_idx]=nums[max_idx],nums[i]
          print(nums)

num = [4,35,2,5,75,4,563,4567,4,356,4,33254534,4534]
selection_sorta(num)
     