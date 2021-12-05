# Neetcode
# https://youtu.be/XYQecbcd6_c

# Approach 4: Expand Around Center
# In fact, we could solve it in O(n^2) time using only constant space.
# We observe that a palindrome mirrors around its center. Therefore, a palindrome can be expanded from its 
# center, and there are only 2n−1 such centers.

# why there are 2n−1 but not n centers? The reason is the center of a palindrome can be in between two letters. 
# Such palindromes have even number of letters (such as "abba") and its center are between the two 'b's.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):

            # odd length
            # initialize left and right pointers to i
            l,r = i,i
            while l>=0 and r<len(s) and s[l] == s[r]:
                if (r-l+1)>resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                l-=1
                r+=1
            
            # even length
            l,r = i,i+1
            while l>=0 and r<len(s) and s[l] == s[r]:
                if (r-l+1)>resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                l-=1
                r+=1

        return res


s = "babad"
obj = Solution()
print(obj.longestPalindrome(s))

# Complexity Analysis:
# Time complexity : O(n^2). Since expanding a palindrome around its center could take O(n) time, the overall 
# complexity is O(n^2)
# Space complexity : O(1).
