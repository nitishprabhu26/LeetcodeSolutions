# Approach 2: Use an Array to Store Frequencies (PENDING)
# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/solution/

# Intuition:
# Let's dive deep into the condition (time[i] + time[j]) % 60 == 0 to examine the relation between time[i] and
# time[j]. Assuming that a and b are two elements in the input array time, we have:
# (a+b) % 60 = 0
#       ⇓
# ((a % 60)+(b % 60)) % 60=0
#       ⇓
# Therefore, either
#   a % 60 = 0
#   b % 60 = 0,
#  or
#   (a % 60)+(b % 60)=60
# Hence, all we need would be finding the pairs of elements in time so they meet these conditions.


# Algorithm:
# We would iterate through the input array time and for each element a, we want to know the number of elements
# b such that:
# 1. b % 60 = 0, if a % 60 = 0
# 2. b % 60 = 60 − (a % 60), if a % 60 != 0

# We can use Approach 1 (brute force) to implement this logic by repeatedly examining the rest of time again 
# and again for each element a. However, we are able to improve the time complexity by consuming more space - 
# we can store the frequencies of the remainder a % 60, so that we can find the number of the complements 
# in O(1) time.

# We would initiate an array remainders with size 60 to record the frequencies of each remainder - as the
# range of remainders is [0,59]. Then we can loop through the array once and for each element a we would:

# 1. if a % 60 = 0, add remainders[0] to the result; else, add remainders[60 - t % 60] to the result;
# 2. update remainders[a % 60].

from typing import List
import collections


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remainders = collections.defaultdict(int)
        ret = 0
        for t in time:
            if t % 60 == 0:  # check if a%60==0 && b%60==0
                ret += remainders[0]
            else:  # check if a%60+b%60==60
                ret += remainders[60-t % 60]
            remainders[t % 60] += 1  # remember to update the remainders
        return ret


time = [30, 20, 150, 100, 40]
obj = Solution()
print(obj.numPairsDivisibleBy60(time))

# Complexity Analysis:
# Time complexity: O(n), when n is the length of the input array, because we would visit each element in
# time once.
# Space complexity: O(1), because the size of the array remainders is fixed with 60.
