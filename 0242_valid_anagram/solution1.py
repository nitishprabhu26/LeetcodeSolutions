# Approach 1: Sorting


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)


# converting to list
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_array = list(s)
        t_array = list(t)
        s_array.sort()
        t_array.sort()
        return s_array == t_array


s = "anagram"
t = "nagaram"
obj = Solution()
print(obj.isAnagram(s, t))


# Complexity analysis:
# Time complexity : O(n logn). used sorted method
# Space complexity : O(1).
