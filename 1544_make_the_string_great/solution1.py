# Approach 1: Iteration.
# https://leetcode.com/problems/make-the-string-great/solution/ (go through overview as well)

# Intuition
# Since the answer is guaranteed to be unique, we don't need to worry about the order of deletion, we just keep 
# deleting pairs until no more pairs can be found.
# One thing to note is that to judge if two adjacent characters make a pair? We do easily tell that patterns like 
# aA, Bb, cC are pairs, but how to implement the code? We can use the their ASCII values as reference, each 
# character has a unique ASCII value:
# a = 97, A = 65
# b = 98, B = 66
# c = 99, C = 67 ...
# z = 122, Z = 90
# Thus we can tell that two characters make a pair, when and only when their ASCII values differ by 32 (Since 
# the sentence only contains letters of alphabet, we do not need to consider about other speical characters).

# Algorithm
# 1.If the size of string s is smaller than 2, return s directly.
# 2.Iterate over all adjacent characters in s.
# - If we find a pair, remove it from s, and start over from step 2.
# - Otherwise, we don't need to iterate. Move to step 3.
# 3.Return s as the final good string.


class Solution:
    def makeGood(self, s: str) -> str:
        # if s has less than 2 characters, we just return itself.
        while len(s) > 1:
            # 'find' records if we find any pair to remove.
            find = False
            
            # Check every two adjacent characters, curr_char and next_char.
            for i in range(len(s) - 1):
                curr_char, next_char = s[i], s[i + 1]
                
                # If they make a pair, remove them from 's' and let 'find = True'.
                if abs(ord(curr_char) - ord(next_char)) == 32:
                    s = s[:i] + s[i + 2:]
                    find = True
                    break
            
            # If we cannot find any pair to remove, break the loop. 
            if not find:
                break
        return s
        

s = "leEeetcode"
obj = Solution()
print(obj.makeGood(s))


# Complexity Analysis:
# Let n be the length of the input string s.
# Time complexity: O(n^2).
# - Each iteration for s takes O(n) time.
# - In the worst-case scenario, we can remove one pair in each iteration, there might be O(n) pairs.
# - In summary, the time complexity is O(n^2).
# Space complexity: O(n). 
# - After we remove a pair, we concatenate the rest strings into a new string and start iterating again. Making 
#   copies of the rest of s requires O(n) space.
# - Therefore, the space complexity is O(n).