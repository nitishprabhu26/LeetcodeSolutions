# Approach : using dictionary


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dict = {}
        for i in s:
            dict[i] = dict.get(i, 0) + 1

        for i in t:
            if not dict.get(i, 0):
                return False
            dict[i] = dict[i]-1
        return True


s = "anagram"
t = "nagaram"
obj = Solution()
print(obj.isAnagram(s, t))


# Complexity analysis:
# Time complexity : O(n). for loop
# Space complexity : O(n). to store dictionary. but since we have 26 charecters in alphabets, it could be 
# considered as O(1)