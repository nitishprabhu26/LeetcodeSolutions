# Approach : Neetcode
# https://youtu.be/Gjkhm1gYIMw

# Brute force approach:

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        h,n = len(haystack), len(needle)
        
        for i in range(h + 1 - n):
            for j in range(n):
                # checking/matching each index until the last
                # if doesnt break until last index, then strings matches
                # if charecters doesnt match at any point, then directrly break and move with next index
                if haystack[i + j] != needle[j]:
                    break
                if j == n - 1:
                    return i
        return -1


# OR

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        h,n = len(haystack), len(needle)
        
        for i in range(h + 1 - n):
            if haystack[i : i + n] == needle:
                return i
        return -1


haystack = "sadbutsad"
needle = "sad"
obj = Solution()
print(obj.strStr(haystack, needle))


# Complexity Analysis:
# Time Complexity: O(h * n), n is length of needle and h is length of haystack.
# Space Complexity: O(1). No extra space used.