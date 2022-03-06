# Neetcode: Sliding window O(n)
# https://youtu.be/gqXU1UyA8pk

# Theres another way without having to look at the entire hashmap everytime to find the most common charecter 
# i.e. without 'max(count.values())'
# O(n) instead of O(26.n) 
# we can have a maxf variable - which has the count of the most frequent charecter at any given time
# https://youtu.be/gqXU1UyA8pk?t=730
# (maxf is only increased, and not decreased)
# result is maximised as we get a new maxf, since windowLen - maxf <= k
# we want to minimize the LHS, 
# i.e for the result to increase, we need a bigger windowLen and a bigger maxf, and ensure that 
# windowLen - maxf <= k, where k is a constant

# eg:  windowLen - maxf <= k
# 6 - 4 <= 2
# res = 6

# now result can increase to 7, only when windowLen is increased to 7, and also maxf has to be increased to 5
# to maintain 7 - 5 <= 2
# if maxf is decreased, our result is never going to change to res = 7
# so we dont need to look through hashmap and find the maxf, and hence we dont decrement maxf value (wont effect)


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        
        # initialize left pointer to 0
        l = 0
        maxf = 0
        # right pointer is increased by 1 evry loop
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            
            # for O(N) - optimization
            # replacing max(count.values()) with maxf in while loop, reducing from O(26N) to O(N).
            maxf = max(maxf, count[s[r]])
            
            # to check if current window is valid, run loop until current window is not valid
            # (length of window - count of the most freq charecter) is greater than k
            # loop runs only once, so we can use a if condition instead
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            
            # https://leetcode.com/problems/longest-repeating-character-replacement/discuss/278271/JavaC++Python-Sliding-Window-just-O(n)
            # if (r - l + 1) - maxf > k:
            #     count[s[l]] -= 1
            #     l += 1

            # max of (result or the size of the window), updating result as soon as window becomes valid
            res = max(res, r - l + 1)
        return res


s = "ABAB"
k = 2
obj = Solution()
print(obj.characterReplacement(s, k))


# Complexity Analysis:
# Time Complexity: O(N).
# Space Complexity: O(26). The dictionary 'count' which holds the frequency of charecters, has a max length of 
# 26 (26 alphabets)