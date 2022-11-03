# Two pointer approach:
# https://youtu.be/KOUtRfgslGM


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for l in range(n//2, 0, -1):
            if n % l == 0:
                i = 0
                while i + l < n and s[i] == s[i + l]:
                    i += 1
                if i + l == n:
                    return True
        return False


s = "abcabcabcabc"
obj = Solution()
print(obj.repeatedSubstringPattern(s))


# Complexity Analysis:
# Let n be the length of the input string 's'.
# Time Complexity: O(n^2) worst case.
# Space Complexity: O(1).