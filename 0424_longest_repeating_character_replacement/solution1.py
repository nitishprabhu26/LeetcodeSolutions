# Neetcode: Sliding window O(26.n)
# https://youtu.be/gqXU1UyA8pk

# Brute force way is to check for all substrings O(n^2) - not so efficient
# we can use the number of replacements(k) to find if a substring has same charecter

# Algorithm:
# In a substring we will replace the charecter which occurs less frequent with the one which occurs most common 
# in that substring. We can use a hashmap which stores the charecter frequency, and use it to find the most 
# common charecter in that substring window
# eg: s="ABABBA" and k = 2
# while checking for window -> 'BABB', we can replace 'A' with 'B'
# To check if window is valid -> windowLen - count[B] = 4 - 3 = 1
# So, the number of charecers in the window -> 'BABB' that we need to replace, so as to match the most frequent 
# charecter 'B' is 1. To make it 'BBBB'.
# So we confirm with,
# windowLen - count[B] <= k (To check if we have enough replacements available)
# i.e.      4 - 3 <= 2
# i.e.          1 <= k

# Also the dictionary 'count' which holds the frequency of charecters, has a max length of 26 (26 alphabets)
# so every time to check the count of most frequent charecter, we need O(26) (Less efficient but still Linear)

# We use a sliding window technique, expand to right as long as the condition is valid: windowLen - count[B] <= k
# Once its invalid, then shift(increment) the left pointer until the string becomes valid again
# We dont need a while loop, because from one for-loop iteration to the next, (r - l + 1) - max(count.values()) 
# can grow by at most 1, and each while-loop iteration decreases it by 1. 
# So we can also use if condition instead. It also means that your window never shrinks (reduces by one in while 
# loop iteration but increases by 1 in the next iteration of for loop), 
# so you can just return the length of the final window.


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        # initialize left pointer to 0
        l = 0
        # right pointer is increased by 1 evry loop
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            
            # to check if current window is valid, run loop until current window becomes valid
            # (length of window - count of the most freq charecter) is greater than k
            # loop runs only once, so we can use a if condition instead
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            # if (r - l + 1) - max(count.values()) > k:
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
# Time Complexity: O(26.N).
# Space Complexity: O(26). The dictionary 'count' which holds the frequency of charecters, has a max length of 
# 26 (26 alphabets)