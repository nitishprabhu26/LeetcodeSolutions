# Approach 1: Brute Force (Time Limit Exceeded)

from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        ret, n = 0, len(time)
        for i in range(n):
            # j starts with i+1 so that i is always to the left of j
            # to avoid repetitive counting
            for j in range(i + 1, n):
                ret += (time[i] + time[j]) % 60==0
        return ret


time = [30,20,150,100,40]
obj = Solution()
print(obj.numPairsDivisibleBy60(time))

# Complexity Analysis:
# Time complexity: O(n^2), when n is the length of the input array. For each item in time, we iterate through 
# the rest of the array to find a qualified complement taking O(n) time.
# Space complexity: O(1).