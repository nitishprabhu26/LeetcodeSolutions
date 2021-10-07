# Approach 1: Recursion, In-Place, O(N) Space

# Algorithm:
# Here is an example. Let's implement recursive function helper which receives two pointers, left and right, as arguments.
# Base case: if left >= right, do nothing.
# Otherwise, swap s[left] and s[right] and call helper(left + 1, right - 1).

class Solution:
    def reverseString(self, s):
        def helper(left, right):
            if left < right:
                s[left], s[right] = s[right], s[left]
                helper(left+1, right-1)

        helper(0, len(s)-1)
        return s


# OR
# using recursion outside of the given function, 'using self'

# class Solution:
#     def reverseString(self, s):
#         self.helper(s, 0, len(s)-1)
#         return s

#     def helper(self, s, left, right):
#         if left < right:
#             s[left], s[right] = s[right], s[left]
#             self.helper(s, left+1, right-1)


s = ["h", "e", "l", "l", "o"]
obj = Solution()
print(obj.reverseString(s))

# Does in-place mean constant space complexity?
# No. By definition, an in-place algorithm is an algorithm which transforms input using no auxiliary data structure.
# The tricky part is that space is used by many actors, not only by data structures. The classical example is to use recursive function
# without any auxiliary data structures.
# Is it in-place? Yes.
# Is it constant space? No, because of recursion stack.

# Complexity Analysis:
# Time complexity : O(N) time to perform N/2 swaps.
# Space complexity : O(N) to keep the recursion stack.
