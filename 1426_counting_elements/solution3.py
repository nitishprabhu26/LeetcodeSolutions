# Approach 3: Search with Sorted Array
# https://leetcode.com/problems/counting-elements/solution/

# Intuition:
# Another way of changing the data storage to allow for more efficient searching is to sort it. Sorting has a time complexity of O(NlogN), 
# and searching for integers in a sorted array, using binary search, has a cost of O(logN). This will give us a total time complexity of 
# O(NlogN).
# The main challenge of this approach would be needing to implement your own binary search.
# However, we don't actually need to use binary search! If we iterate over the sorted arr, then we know that if x + 1 exists, it will be 
# after all the copies of x.
# Each copy of x should be counted if at least one copy of x + 1 exists. Therefore, we can iterate down the sorted arr, keeping track of 
# how many times the current x has appeared. When we get to a different integer, we can check if it's x + 1, and if it is, then the number 
# of x we saw should be added to count.


from typing import List


class Solution:
    def countElements(self, arr: List[int]) -> int:
        arr.sort()
        count = 0
        run_length = 1
        for i in range(len(arr)):
            if arr[i - 1] != arr[i]:
                if arr[i - 1] + 1 == arr[i]:
                    count += run_length
                run_length = 0
            run_length += 1
        return count

arr = [1,2,3]
obj = Solution()
print(obj.countElements(arr))


# Complexity Analysis:
# Let N be the length of the input array, arr.
# Time complexity : O(NlogN).
# Sorting using a built-in sorting algorithm has a cost of O(NlogN). After that, we do a single pass through arr, which has a cost of O(N),
# giving us a total time complexity of O(NlogN) + O(N) = O(NlogN).
# Space complexity : varies from O(N) to O(1).
# The space complexity of this approach is dependent on the space complexity of the sorting algorithm you're using. The space complexity 
# of sorting algorithms built into programming languages is generally anywhere from O(N) to O(1).