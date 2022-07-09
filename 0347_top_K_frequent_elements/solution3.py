# Approach 1: (Similar)
# https://youtu.be/Gj4-8sRi7W0

# Using sorted on dictionaries:
# https://towardsdatascience.com/sorting-a-dictionary-in-python-4280451e1637
# Using lambda function: https://youtu.be/zk15irJMms0


import heapq
from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        # dictionary with value->frequency
        c = Counter(nums)

        # sort the dictionary, key is the no of times it appears(i.e. the value inside the dictionary i.e. freq)
        # reverse it so that most freq elements are on top (descending order)
        c = sorted(c, key = lambda x : c[x], reverse = True)

        # extra: if dictionary is sorted, then it sorts the key by default, and returns keys as a list
        # c = sorted(c)

        return c[:k]


# OR using c.items() - an iterable which give tuples
# https://towardsdatascience.com/sorting-a-dictionary-in-python-4280451e1637

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
         
        # dictionary with value->frequency
        c = Counter(nums)
        
        # x[1] is to consider 2nd element in tuple, i.e. value in key->value of a dictionary
        c = [key for key, val in sorted(c.items(), key = lambda x : x[1], reverse = True)]

        return c[:k]


# OR (using heap)

from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        c = Counter(nums) 
        
        # negative to make it max heap
        c = [(-v, k) for k, v in c.items()]
        # https://www.geeksforgeeks.org/time-complexity-of-building-a-heap/
        heapq.heapify(c)
        output = []
        
        for _ in range(k):
            # removes smallest number from heap every time in python, 
            # but we have made it as a max heap by negating frequency
            item = heapq.heappop(c)
            output.append(item[1])
        
        return output


nums = [1,1,1,2,2,3]
k = 2
obj = Solution()
print(obj.topKFrequent(nums, k))


# Complexity analysis:
# Time complexity : O(N logN) or O(N) for the heapify function.(check below link)
# https://www.geeksforgeeks.org/time-complexity-of-building-a-heap/
# and for the loop which loops 'k' times, and each time o(log N) for heappop. Therefore O(k log N)
# Space complexity : O(N + k) to store heap with N elements and a output with k elements.

