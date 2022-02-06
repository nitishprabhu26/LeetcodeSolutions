# Approach 3: Using Breadth-First-Search
# https://leetcode.com/problems/word-break/solution/

# Algorithm:
# Another approach is to use Breadth-First-Search. Visualize the string as a tree where each node represents 
# the prefix upto index 'end'. Two nodes are connected only if the substring between the indices linked with 
# those nodes is also a valid string which is present in the dictionary. In order to form such a tree, we start 
# with the first character of the given string (s) which acts as the root of the tree being formed and find 
# every possible substring starting with that character which is a part of the dictionary. Further, the ending 
# index (say i) of every such substring is pushed at the back of a queue which will be used for Breadth First 
# Search. Now, we pop an element out from the front of the queue and perform the same process considering the 
# string s(i+1,end) to be the original string and the popped node as the root of the tree this time. This 
# process is continued, for all the nodes appended in the queue during the course of the process. If we are 
# able to obtain the last element of the given string as a node (leaf) of the tree, this implies that the given 
# string can be partitioned into substrings which are all a part of the given dictionary.

from collections import deque
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        # stores all the starting positions
        q = deque()
        visited = set()

        # initial start point
        q.append(0)
        while q:
            start = q.popleft()
            if start in visited:
                continue
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in word_set:
                    q.append(end)
                    if end == len(s):
                        return True
            visited.add(start)
        return False
            
s = "leetcode"
wordDict = ["leet","code"]
obj = Solution()
print(obj.wordBreak(s, wordDict))

# Complexity Analysis:
# n is the length of the input string.
# Time Complexity: O(n^3). For every starting index, the search can continue till the end of the given string.
# Space Complexity: O(n). Queue of at most n size is needed.