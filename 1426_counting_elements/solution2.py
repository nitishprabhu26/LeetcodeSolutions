# Approach 2: Search with HashSet

# Intuition:
# Recall that a HashSet removes duplicates. 
# Consider a case like arr = [1, 1, 2]. The HashSet will be {1, 2}. 
# So we need to loop over arr, but do the existence checks using the HashSet.


from ast import Or
from typing import List


class Solution:
    def countElements(self, arr: int) -> int:
        hash_set = set(arr)
        count = 0
        for x in arr:
            if x + 1 in hash_set:
                count += 1
        return count


# OR
# one pass solution 


class Solution:
    def countElements(self, arr: List[int]) -> int:
        frequency_map = {}
        count = 0
        for elem in arr:
            if elem not in frequency_map:
                frequency_map[elem] = 1
            else:
                frequency_map[elem] += 1
            if elem+1 in frequency_map:
                count += 1
            if elem-1 in frequency_map and frequency_map[elem]==1:
                count += frequency_map[elem-1]
        return count
        
arr = [1,2,3]
obj = Solution()
print(obj.countElements(arr))


# Complexity Analysis:
# Let N be the length of the input array, arr.
# Time complexity : O(N).
# Creating a HashSet from N integers takes O(N) time. We then need to loop over each of the N integers like before, except this time we 
# check for x + 1 by seeing if it is in the HashSet; an O(1) operation. This gives us a total time complexity of 
# O(N) + N.O(1) = O(N) + O(N) = O(N).
# Space complexity : O(N).
# The HashSet needs to store each unique integer from arr. In the worst case, all the integers in arr will be unique, meaning that the 
# HashSet has a space complexity of O(N).