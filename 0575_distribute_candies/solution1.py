# Overview:
# Solving this problem efficiently requires a couple of key observations.

# 1.If the number of unique candies is less than or equal to half the length of candyType, then Alice can eat one 
#   of each type of candy and the answer is equal to the number of unique candies.
# 2.Otherwise, the number of candies she can eat is limited to half the length of candyType, and so the answer is 
#   equal to half the length of candyType.
# In essence, this problem boils down to finding the number of unique candies. We then return whichever value is 
# smaller out of the number of unique candies and half the length of candyType.


# Approach 1: Brute Force [Time Limit Exceeded]

# Intuition and Algorithm:
# One way to find the number of unique candies is to traverse over each element in 'candyType', checking whether or 
# not we've already seen a candy of this same type. We can do this check by iterating over all elements before the 
# current element. If any of those are of the same type, then this is not a unique candy. We should keep track of 
# the number of unique candies we find.


from typing import List

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        # We need to count how many unique candies are in the array.
        unique_candies = 0
        # For each candy, we're going to check whether or not we've already
        # seen a candy identical to it.
        for i in range(len(candyType)):
            # Check if we've already seen a candy the same as candyType[i].
            for j in range(0, i):
                # If this candy is the same as previous one, we don't need to 
                # check further.
                if candyType[i] == candyType[j]:
                    break
            # Confused? An "else" after a "for" is an awesome Python feature.
            # The code in the "else" only runs if the "for" loop runs without a break.
            # In this case, we know that if we didn't "break" out of the loop, then 
            # candyType[i] is unique.
            else:
                unique_candies += 1
        # The answer is the minimum out of the number of unique candies, and 
        # half the length of the candyType array.
        return min(unique_candies, len(candyType) // 2)


candyType = [1,1,2,2,3,3]
obj = Solution()
print(obj.distributeCandies(candyType))


# Complexity Analysis:
# Let N be the the length of candyType.
# Time Complexity: O(N^2). We traverse over each of the N elements of candyType, and for each, we check all of the 
# elements before it. Checking each item for each item is the classic O(N^2) time complexity pattern.
# Space Complexity: O(1). We don't allocate any additional data structures, instead only using constant space 
# variables.