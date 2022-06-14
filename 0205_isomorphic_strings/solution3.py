# Approach : Neetcode
# https://youtu.be/7yF-U1hLEqQ


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapST, mapTS = {}, {}
        
        for c1, c2 in zip(s, t):
            if ((c1 in mapST and mapST[c1] != c2) or (c2 in mapTS and mapTS[c2] != c1)):
                return False
            mapST[c1] = c2
            mapTS[c2] = c1
            
        return True
        

s = "egg"
t = "add"
obj = Solution()
print(obj.isIsomorphic(s, t))


# Complexity analysis:
# Here N is the length of each string (if the strings are not the same length, then they cannot be isomorphic).
# Time Complexity: O(N). We process each character in both the strings exactly once to determine if the strings 
# are isomorphic.
# Space Complexity: O(1) since the size of the ASCII character set is fixed and the keys in our dictionary are all 
# valid ASCII characters according to the problem statement.
