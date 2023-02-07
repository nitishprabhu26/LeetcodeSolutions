# Approach: Converting word to list of numbers (Python supports it)
# https://youtu.be/FFJVrXtqepo


from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        lookup = {c : ix for ix, c in enumerate(order)}
        
        words2 = []
        for w in words:
            tmp = []
            for c in w:
                tmp.append(lookup[c])
            words2.append(tmp)
            
        for i in range(1, len(words2)):
            # Python supports it
            # if words2[i - 1] = [1, 2, 3] and words2[i] = [1, 2]
            # then, words2[i - 1] > words2[i]
            if words2[i - 1] > words2[i]:
                return False
        
        return True


words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
obj = Solution()
print(obj.isAlienSorted(words, order))


# Complexity Analysis:
# Let N be the length of order, and M be the total number of characters in words.(not number of words)
# Time complexity: O(M).
# Space complexity: O(1).