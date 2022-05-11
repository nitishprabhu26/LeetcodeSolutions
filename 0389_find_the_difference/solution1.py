# Approach 1: Sorting

# sort(String t) = sort(shuffled(String s + Any character)).

# Algorithm:
# 1.Sort the string s and string t.
# 2.Iterate through the length of strings and do a character by character comparison. This just checks if the 
#   current character in string t is present in string s.
# 3.Once we encounter a character which is in string t but not in string s, we have found the extra character 
#   string t was hiding all this while.


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        # Sort both the strings
        sorted_s = sorted(s)
        sorted_t = sorted(t)

        # Character by character comparison
        i = 0
        while i < len(s):
            if sorted_s[i] != sorted_t[i]:
                return sorted_t[i]
            i += 1

        return sorted_t[i]


s = "abcd"
t = "abcde"
obj = Solution()
print(obj.findTheDifference(s, t))


# Complexity Analysis:
# Time complexity: O(Nlog(N)), where N is length of the strings. Sorting is the most expensive operation of this 
# algorithm. Sorting would take O(Nlog(N)) time. Iterating both the strings for character by character comparison 
# would take another O(N) time.
# Space complexity: O(N). The sorted character arrays would take O(N) each.