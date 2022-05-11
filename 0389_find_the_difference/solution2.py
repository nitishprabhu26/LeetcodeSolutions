# Approach 2: Using HashMap

# We might just think in worst case the string is of length N and each character has a frequency of 1. This would 
# result in a hash map of O(N) space.
# But, The problem states, string s and t consists of only lowercase letters.
# The above statement implies we only have 26 characters i.e. [a, z]. Thus, we have a space complexity for just 
# 26 characters.

# Algorithm:
# 1.Store all the characters of string s in a hash map called counterS. The key would be the character and value 
#   would be number of times the character appeared in the string.
# 2.Now, iterate through string t and for each character, check if it is present in the hash map counterS.
# 3.If the character is present in counterS then we just decrement the corresponding value by 1.
# 4.If the character is not present in counterS or has a frequency of zero in counterS it means we have found the 
#   extra character of string t.


from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # Prepare a counter for string s.
        # This holds the characters as keys and respective frequency as value.
        counter_s = Counter(s)

        # Iterate through string t and find the character which is not in s.
        for ch in t:
            if ch not in counter_s or counter_s[ch] == 0:
                return ch
            else:
                # Once a match is found we reduce frequency left.
                # This eliminates the possibility of a false match later.
                counter_s[ch] -= 1


s = "abcd"
t = "abcde"
obj = Solution()
print(obj.findTheDifference(s, t))


# Complexity Analysis:
# Time complexity: O(N), where N is length of the strings. Since, we iterate through both the strings once.
# Space complexity: O(1). The problem states string s and string t have lowercase letters. Thus, the total number 
# of unique characters and eventually buckets in the hash map possible are just 26.