# Approach 3: Using a Hash Set

# Intuition and Algorithm:
# Recall that a Set cannot contain duplicates, and attempting to add a duplicate item into a Set will do nothing.
# Therefore, the best way to find the number of unique elements is to simply insert all of the candyType elements 
# into a Hash Set. After that, the number of unique candies is simply the number of elements in the Hash Set.


from typing import List

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        # Count the number of unique candies by creating a set with
        # candyType, and then taking its length.
        unique_candies = len(set(candyType))
        # And find the answer in the same way as before.
        return min(unique_candies, len(candyType) // 2)


candyType = [1,1,2,2,3,3]
obj = Solution()
print(obj.distributeCandies(candyType))


# Complexity Analysis:
# Let N be the the length of candyType.
# Time Complexity: O(N). Adding an item into a Hash Set has an amortized time of O(1). Therefore, adding N items 
# requires O(N) time. All of the other operations we use are O(1).
# Space Complexity: O(N). The worst case for space complexity occurs when all N elements are unique. This will 
# result in a Hash Set containing N elements.