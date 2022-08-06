# Approach #1 Brute Force [Accepted]

# If a string with an even length is a palindrome, every character in the string must always occur an even number 
# of times. If the string with an odd length is a palindrome, every character except one of the characters must 
# always occur an even number of times. Thus, in case of a palindrome, the number of characters with odd number of 
# occurrences can't exceed 1(1 in case of odd length and 0 in case of even length).

# The given string could contain almost all the ASCII characters from 0 to 127. Thus, we iterate over all the 
# characters from 0 to 127. For every character chosen, we again iterate over the given string s and find the 
# number of occurrences, ch, of the current character in s. We also keep a track of the number of characters in 
# the given string s with odd number of occurrences in a variable count.

# If, for any character currently considered, its corresponding count, ch, happens to be odd, we increment the 
# value of count, to reflect the same. In case of even value of ch for any character, the count remains unchanged.

# If, for any character, the count becomes greater than 1, it indicates that the given string s can't lead to the 
# formation of a palindromic permutation based on the reasoning discussed above. But, if the value of count remains 
# lesser than 2 even when all the possible characters have been considered, it indicates that a palindromic 
# permutation can be formed from the given string s.


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count = 0
        
        # iterate over all the characters from 0 to 127
        for i in range(128):
            # break condition when count > 1
            if count <= 1:
                ct = 0
                for j in range(len(s)):
                    if ord(s[j]) == i:
                        ct += 1
            else:
                return False
            # increment count if, no of occurence of charecter ch is odd
            count += ct % 2
        
        return count <= 1


s = "code"
obj = Solution()
print(obj.canPermutePalindrome(s))


# Complexity Analysis:
# Time complexity : O(n). We iterate constant number of times (128) over the string s of length n, 
# i.e. O(128 ⋅ n) = O(n).
# Space complexity : O(1). Constant extra space is used.