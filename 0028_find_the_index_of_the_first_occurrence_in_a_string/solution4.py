# Neetcode : Knuth–Morris–Pratt (KMP) Approach
# https://youtu.be/JoF0Z7nVSrA


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        # LPS portion - setting up LPS array
        lps = [0] * len(needle)

        # prevLPS - Previous Longest Prefix Suffix; i - current charecter (starts at index 1)
        # eg. considered in video(to get LPS array): needle = "AAACAAAA"
        prevLPS, i = 0, 1
        while i < len(needle):
            if needle[i] == needle[prevLPS]:
                lps[i] = prevLPS + 1
                prevLPS += 1
                i += 1
            else:
                if prevLPS == 0:
                    lps[i] = 0
                    i += 1
                else:
                    prevLPS = lps[prevLPS - 1]

        # Actual code
        i = 0 # ptr for haystack
        j = 0 # ptr for needle
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i, j = i + 1, j + 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j - 1]
            if j == len(needle):
                return i - len(needle)
        return -1


haystack = "sadbutsad"
needle = "sad"
obj = Solution()
print(obj.strStr(haystack, needle))


# Complexity Analysis:
# Time Complexity: O(n + m), n is length of needle and m is length of haystack.
# for LPS: O(2.n)
# Space Complexity: O(n). To store the LPS (Longest Prefix Suffix) array.