# Approach 2: Two-Pointers
# https://leetcode.com/problems/is-subsequence/solution/
# OR
# Neetocde: https://youtu.be/99RVfqklbCE


# Intuition:
# Following the same intuition above, we could further optimize the space complexity of the previous solutions, by 
# replacing the recursion with the iteration.

# Algorithm:
# We designate two pointers for iteration, with the left pointer referring to the source string and the right 
# pointer to the target string.
# We move the pointers accordingly on the following two cases:
# - If source[left] == target[right]: we found a match. Hence, we move both pointers one step forward.
# - If source[left] != target[right]: no match is found. We then move only the right pointer on the target string.
# The iteration would terminate, when either of the pointers exceeds its boundary.
# At the end of the iteration, the result solely depends on the fact that whether we have consumed all the 
# characters in the source string. If so, we have found a suitable match for each character in the source string. 
# Therefore, the source string is a subsequence of the target string.


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        LEFT_BOUND, RIGHT_BOUND = len(s), len(t)

        p_left = p_right = 0
        while p_left < LEFT_BOUND and p_right < RIGHT_BOUND:
            # move both pointers or just the right pointer
            if s[p_left] == t[p_right]:
                p_left += 1
            p_right += 1

        return p_left == LEFT_BOUND


s = "abc"
t = "ahbgdc"
obj = Solution()
print(obj.isSubsequence(s, t))


# Complexity Analysis:
# Let |S| be the length of the source string, and |T| be the length of the target string.
# Time complexity : O(∣T∣). i.e. O(n).
# - The analysis is the same as the previous approach.
# Space complexity : O(1).
# - We replace the recursion with iteration. In the iteration, a constant memory is consumed regardless of input.
