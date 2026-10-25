# brute force

class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        n = len(fruits)
        maxi = 0
        for i in range (n):
            my_set = set()
            for j in range(i, n):
                my_set.add(fruits[j])
                if len(my_set) >2:
                    break
                maxi = max(maxi, j-i+1)
        return maxi



        



# better Solution


class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        n = len(fruits)
        maxi = 0
        right = 0
        left = 0
        my_dict = {}
        while right < n:
            my_dict[fruits[right]] = my_dict.get(fruits[right],0) +1
            while len(my_dict) > 2:
                my_dict[fruits[left]] -= 1
                if my_dict[fruits[left]]==0:
                    del my_dict[fruits[left]]
                left+=1
            if len(my_dict) <= 2:
                maxi = max(maxi, right-left+1)
            right+=1
        return maxi




        

# optimal solution 


class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        n = len(fruits)
        maxi = 0
        right = 0
        left = 0
        my_dict = {}
        while right < n:
            my_dict[fruits[right]] = my_dict.get(fruits[right],0) +1
            if len(my_dict) > 2:
                my_dict[fruits[left]] -= 1
                if my_dict[fruits[left]]==0:
                    del my_dict[fruits[left]]
                left+=1
            if len(my_dict) <= 2:
                maxi = max(maxi, right-left+1)
            right+=1
        return maxi




        