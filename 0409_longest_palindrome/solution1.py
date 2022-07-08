# Approach #1: Greedy [Accepted]

# Intuition:
# A palindrome consists of letters with equal partners, plus possibly a unique center (without a partner). The 
# letter i from the left has its partner i from the right. For example in 'abcba', 'aa' and 'bb' are partners, 
# and 'c' is a unique center.

# Algorithm:
# For each letter, say it occurs v times. We know we have v // 2 * 2 letters that can be partnered for sure. For 
# example, if we have 'aaaaa', then we could have 'aaaa' partnered, which is 5 // 2 * 2 = 4 letters partnered.
# At the end, if there was any v % 2 == 1, then that letter could have been a unique center. Otherwise, every 
# letter was partnered. To perform this check, we will check for v % 2 == 1 and ans % 2 == 0 (center case needs 
# only one unique charecter), the latter meaning we haven't yet added a unique center to the answer.
# for center case:
# We need not use all the characters of the given input.
# Eg: aaaaabbb. Expected answer: 7 because output string is : aaaabbb or aababaa
# Not all characters of the letter 'a' or 'b' needs to be considered in the final answer.


import collections

class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        for v in collections.Counter(s).values():
            ans += v // 2 * 2
            if ans % 2 == 0 and v % 2 == 1:
                ans += 1
        return ans


# OR
# https://youtu.be/ci4PIq1NWoU


class Solution:
    def longestPalindrome(self, s: str) -> int:
        letters = {}
        
        for char in s:
            if char not in letters:
                letters[char] = 1
            else:
                letters[char] += 1
                
        res, odd = 0, 0
        
        if len(letters) == 1:
            return letters[s[0]]
        
        for i in letters.values():
            if i % 2 == 0:
                res += i
            else:
                # make it even by subtracting 'i' by 1
                res += i - 1
                odd += 1
        if odd > 0:
            res += 1
            
        return res
            

s = "abccccdd"
obj = Solution()
print(obj.longestPalindrome(s))


# Complexity Analysis:
# Let N be the number of nodes in the tree.
# Time complexity : O(N), where N is the length of s. We need to count each letter.
# Space complexity : O(1), the space for our count, as the alphabet size of s is fixed. We should also consider 
# that in a bit complexity model, technically we need O(logN) bits to store the count values.