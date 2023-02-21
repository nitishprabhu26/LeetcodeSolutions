# Approach 1: Counting

# Intuition and Algorithm:
# Every uncommon word occurs exactly once in total. We can count the number of occurrences of every word, then 
# return ones that occur exactly once.


import collections
from typing import List

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        count = {}
        for word in s1.split():
            count[word] = count.get(word, 0) + 1
        for word in s2.split():
            count[word] = count.get(word, 0) + 1

        #Alternatively:
        #count = collections.Counter(s1.split())
        #count += collections.Counter(s2.split())

        return [word for word in count if count[word] == 1]
        
# OR

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        c = collections.Counter((s1 + " " + s2).split())
        return [w for w in c if c[w] == 1]
        

s1 = "this apple is sweet"
s2 = "this apple is sour"
obj = Solution()
print(obj.uncommonFromSentences(s1, s2))


# Complexity Analysis
# Time Complexity: O(M + N), where M, N are the lengths of s1 and s2 respectively.
# Space Complexity: O(M + N), the space used by count.