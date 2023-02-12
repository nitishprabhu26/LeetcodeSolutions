# Approach 4: Sliding Window II
# https://leetcode.com/problems/fruit-into-baskets/solution/

# Intuition:
# In the previous approach, we keep the window size non-decreasing. However, we might run into cases where the 
# window contains O(n) types of fruits and takes O(n) space.
# This can be optimized by making sure that there are always at most 2 types of fruits in the window. After adding 
# a new fruit from the right side right, if the current window has more than 2 types of fruit, we keep removing 
# fruits from the left side left until the current window has only 2 types of fruit. Note that the window size may 
# become smaller than before, thus we cannot rely on left and right to keep track of the maximum number of fruits 
# we can collect. Instead, we can just use a variable max_picked to keep track of the maximum window size we 
# encountered.
# https://leetcode.com/problems/fruit-into-baskets/solution/ (description and animation)


# Algorithm:
# 1. Initialize max_picked = 0 as the maximum fruits we can collect, and use hash map basket to record the types 
#    of fruits in the current window.
# 2. Start with an empty window having left = 0 and right = 0 as its left and right index.
# 3. We iterate over right and add fruits[right] to this window.
#    -  If there are no more than 2 types of fruits, this subarray is valid.
#    -  Otherwise, we need to keep removing fruits from the left side until there are only 2 types of fruits in 
#       the window.
#       Then we update max_picked as max(max_picked, right - left + 1).
# 4. Once we finish iterating, return max_picked as the maximum number of fruits we can collect.


from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # We use a hash map 'basket' to store the number of each type of fruit.
        basket = {}
        max_picked = 0
        left = 0
        
        # Add fruit from the right index (right) of the window.
        for right in range(len(fruits)):
            basket[fruits[right]] = basket.get(fruits[right], 0) + 1
            
            # If the current window has more than 2 types of fruit,
            # we remove fruit from the left index (left) of the window,
            # until the window has only 2 types of fruit.
            while len(basket) > 2:
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1
            
            # Update max_picked.
            max_picked = max(max_picked, right - left + 1)
        
        # Return max_picked as the maximum number of fruits we can collect.
        return max_picked


fruits = [1,2,3,2,2]
obj = Solution()
print(obj.totalFruit(fruits))


# Complexity Analysis:
# Let n be the length of the input array fruits.
# Time Complexity: O(n).
# - Similarly, both indexes left and right are only monotonically increasing during the iteration, thus we have at 
#   most 2⋅n steps,
# - At each step, we update the hash set by addition or deletion of one fruit, which takes constant time. Note 
#   that the number of additions or deletions does not exceed n.
#   To sum up, the overall time complexity is O(n)
# Space Complexity: O(1).
# - We maintain the number of fruit types contained in the window in time. Therefore, at any given time, there are 
#   at most 3 types of fruits in the window or the hash map basket.
#   In summary, the space complexity is O(1).