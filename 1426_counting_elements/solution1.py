# Approach 1: Search with Array

# Intuition:
# The simplest way of solving this problem is to loop through each integer, x, checking whether or not it should be counted. This requires 
# checking whether or not x + 1 is in arr.


class Solution:
    def countElements(self, arr: int) -> int:
        count = 0
        for x in arr:
            if x + 1 in arr:
                count += 1
        return count

# Note that we could also do this as a one-liner generator comprehension. 
# return sum(1 for x in arr if x + 1 in arr)


arr = [1,2,3]
obj = Solution()
print(obj.countElements(arr))


# Complexity Analysis:
# Let N be the length of the input array, arr.
# Time complexity : O(N^2).
# We loop through each of the N integers x, checking whether or not x + 1 is also in arr. Checking whether or not x + 1 is in arr is done 
# using linear search, which requires checking through all N integers in arr. Because we're doing N operations N times, we get a time 
# complexity of O(N^2).
# Space complexity : O(1).
# We are only using a constant number of single-value variables (e.g. count), giving us a space complexity of O(1).