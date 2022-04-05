# Approach : Neetcode
# https://youtu.be/9UtInBqnCgA


from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
        
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
            
        for c in countS:
            # if c doesnt exixts in countT
            if countS[c] != countT.get(c, 0):
                return False
        return True

# OR

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


s = "anagram"
t = "nagaram"
obj = Solution()
print(obj.isAnagram(s, t))


# Complexity analysis:
# Time complexity : O(n). for loop
# Space complexity : O(n). to store dictionary. but since we have 26 charecters in alphabets, it could be 
# considered as O(1)
