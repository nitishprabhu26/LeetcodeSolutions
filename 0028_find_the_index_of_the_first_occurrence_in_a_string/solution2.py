# Approach : Using Array Slicing.
# Checking for a match, starting from every index


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h,n = len(haystack), len(needle)
        
        for i in range(h-n+1):
            if haystack[i:i+n] == needle:
                return i
        return -1


haystack = "sadbutsad"
needle = "sad"
obj = Solution()
print(obj.strStr(haystack, needle))


# Complexity Analysis:
# Time Complexity: O(H*N), doing O(N) comparisons inside an O(H) loop.
# Space Complexity: O(1).