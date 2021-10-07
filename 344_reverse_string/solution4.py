# Approach 2: Two Pointers, Iteration, O(1) Space
# but using for loop

class Solution:
    def reverseString(self, s):
        n = len(s)
        for i in range(0, (n)//2):
            s[i], s[n-i-1] = s[n-i-1], s[i]
        return s


s = ["h", "e", "l", "l", "o"]
obj = Solution()
print(obj.reverseString(s))

# Complexity analysis:
# Time complexity : O(N) to swap N/2 element.
# Space complexity : O(1), it's a constant space solution.
