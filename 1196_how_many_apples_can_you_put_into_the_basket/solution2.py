# Approach 2: Min-Heap

# Intuition:
# Another approach to select the lightest apple at each time is using a min-heap. We can transform the input array 
# arr into a min-heap; we then keep popping the first element from it, which is the lightest apple due to 
# min-heap's nature.

# Algorithm:
# - Transform arr into a min-heap, and initialize two integer variables: apples to count the number of apples we 
#   have put in the basket and units to record the current weight of the basket.
# - Before units reaches 5000 and while there are remaining elements in the min-heap:
#   -   increment apple by 1;
#   -   increment units by the popped element from the min-heap;


import heapq
from typing import List

class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        heapq.heapify(weight)
        apples = units = 0

        # note that weight[0] always represents the smallest
        # element in the min-heap
        while weight and units + weight[0] <= 5000:
            units += heapq.heappop(weight)
            apples += 1
        return apples
        

weight = [900,950,800,1000,700,800]
obj = Solution()
print(obj.maxNumberOfApples(weight))


# Complexity Analysis:
# Time complexity : O(N + klogN), where N is the length of the input array and k is the number of apples that will 
# be put into the basket. This is because: transforming an array into a heap takes O(N) time; each pop operation 
# on the heap takes O(logN), and it will called for k times.
# Space complexity : O(N), as we construct a min-heap and put all apples into it. Note that for Python, the space 
# complexity is O(1) because, as stated in the Python docs, heapify(x) transforms list x into a heap, in-place, in 
# linear time.