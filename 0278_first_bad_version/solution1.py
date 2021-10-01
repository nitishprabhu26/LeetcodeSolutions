# Approach #1 (Linear Scan) [Time Limit Exceeded]

# so we go with:
# Approach #2 (Binary Search) [Accepted]

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer

def isBadVersion(version):
    #defined by leetcode
    # returns True or False
    pass

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        mid = 0
        while left <= right:
            mid = left + (right-left) // 2
            
            if isBadVersion(mid):
                right = mid-1
            else:
                left = mid + 1
        return left


n = 5
obj = Solution()
print(obj.firstBadVersion(n))

# https://leetcode.com/problems/first-bad-version/solution/

# Complexity analysis:
# Time complexity : O(logn). The search space is halved each time, so the time complexity is O(logn).
# Space complexity : O(1).