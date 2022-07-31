# Approach 2: One Map
# Filter function - https://www.geeksforgeeks.org/filter-in-python/
# Python Dictionary | setdefault() - https://www.geeksforgeeks.org/python-dictionary-setdefault-method/

# Intuition and Algorithm:
# As in Approach 1, we can have some forward map m1 : L → L, where L is the set of letters.
# However, instead of keeping track of the reverse map m2, we could simply make sure that every value m1(x) in the 
# codomain is reached at most once. This would guarantee the desired permutation exists.
# So our algorithm is this: after defining m1(x) in the same way as Approach 1 (the forward map of the permutation),
# afterwards we make sure it reaches distinct values.


from typing import List

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def match(word):
            P = {}
            for x, y in zip(pattern, word):
                if P.setdefault(x, y) != y:
                    return False
            return len(set(P.values())) == len(P.values())

        return list(filter(match, words))


words = ["abc","deq","mee","aqq","dkd","ccc"]
pattern = "abb"
obj = Solution()
print(obj.findAndReplacePattern(words, pattern))


# Complexity Analysis
# Time Complexity: O(N * K), where N is the number of words, and K is the length of each word.
# Space Complexity: O(N * K), the space used by the answer.