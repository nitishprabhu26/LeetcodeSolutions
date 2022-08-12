# Approach #1 (Linear Scan) [Time Limit Exceeded]
# The straight forward way is to brute force it by doing a linear scan.


# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

def isBadVersion(version):
    #defined by leetcode
    # returns True or False
    pass

class Solution:
    def firstBadVersion(self, n: int) -> int:
        for i in range(1, n):
            if isBadVersion(i):
                return i
        return n


n = 5
obj = Solution()
print(obj.firstBadVersion(n))


# Complexity analysis:
# Time complexity : O(n). Assume that isBadVersion(version) takes constant time to check if a version is bad. It 
# takes at most n - 1 checks, therefore the overall time complexity is O(n).
# Space complexity : O(1).