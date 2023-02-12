# Approach 3: Sliding Window
# https://leetcode.com/problems/fruit-into-baskets/solution/

# Intuition:
# Can we further reduce the time complexity? The answer is Yes!
# https://leetcode.com/problems/fruit-into-baskets/solution/ (description and animation)


# Algorithm:
# 1. Start with an empty window with left and right as its left and right index.
# 2. We iterate over right and add fruits[right] to this window.
#    -  If the number is no larger than 2, meaning that we collect no more than 2 types of fruits, this subarray 
#       is valid.
#    -  Otherwise, it is not the right time to expand the window and we must keep its size. Since we have added 
#       one fruit from the right side, we should remove one fruit from the left side of the window, and increment 
#       left by 1.
# 3. Once we are done iterating, the difference between left and right stands for the longest valid subarray we 
#    encountered, i.e. the maximum number of fruits we can collect.


from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # Hash map 'basket' to store the types of fruits.
        basket = {}
        left = 0
        
        # Add fruit from the right index (right) of the window.
        for right, fruit in enumerate(fruits):
            basket[fruit] = basket.get(fruit, 0) + 1

            # If the current window has more than 2 types of fruit,
            # we remove one fruit from the left index (left) of the window.
            if len(basket) > 2:
                basket[fruits[left]] -= 1

                # If the number of fruits[left] is 0, remove it from the basket.
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1
        
        # Once we finish the iteration, the indexes left and right 
        # stands for the longest valid subarray we encountered.
        return right - left + 1


fruits = [1,2,3,2,2]
obj = Solution()
print(obj.totalFruit(fruits))


# Complexity Analysis:
# Let n be the length of the input array fruits.
# Time Complexity: O(n).
# - Both indexes left and right only monotonically increased during the iteration, thus we have at most 2⋅n steps,
# - At each step, we update the hash set by addition or deletion of one fruit, which takes constant time.
# - In summary, the overall time complexity is O(n),
# Space Complexity: O(n).
# - In the worst-case scenario, there might be at most O(n) types of fruits inside the window.