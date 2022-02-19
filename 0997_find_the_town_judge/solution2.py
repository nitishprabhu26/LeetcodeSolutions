# Approach 2: One Array
# https://leetcode.com/problems/find-the-town-judge/solution/

# The town judge is the only person who could possibly have (indegree - outdegree) equal to N - 1.
# Algorithm
# Each person gains 1 "point" for each person they are trusted by, and loses 1 "point" for each person they trust. 
# Then at the end, the town judge, if they exist, must be the person with N - 1 "points".

from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) < n - 1:
            return -1
    
        trust_scores = [0] * (n + 1)

        for a, b in trust:
            trust_scores[a] -= 1
            trust_scores[b] += 1
        
        # here i starts from 0, so returning i+1
        # for i, score in enumerate(trust_scores[1:]):
        #     if score == n - 1:
        #         return i + 1
        # return -1

        # or set index for enumerate to start from 1
        for i, score in enumerate(trust_scores[1:], 1):
            if score == n - 1:
                return i
        return -1


n = 3
trust = [[1,3],[2,3]]
obj = Solution()
print(obj.findJudge(n, trust))


# Complexity Analysis:
# Let N be the number of people, and E be the number of edges (trust relationships).

# Time Complexity : O(E).
# Same as previous solution. We still need to loop through the E edges in trust, and the argument about the 
# relationship between N and E still applies.

# Space Complexity : O(N).
# We allocated 1 array of length N + 1. So O(N).
