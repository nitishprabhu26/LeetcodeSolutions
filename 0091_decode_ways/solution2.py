# Approach 1: Recursive Approach with Memoization
# https://leetcode.com/problems/decode-ways/solution/


# Algorithm
# Enter recursion with the given string i.e. start with index 0.
# For the terminating case of the recursion we check for the end of the string. If we have reached the end of the string we return 1.
# Every time we enter recursion it's for a substring of the original string. For any recursion if the first character is 0 then 
# terminate that path by returning 0. Thus this path won't contribute to the number of ways.
# Memoization helps to reduce the complexity which would otherwise be exponential. We check the dictionary memo to see if the result 
# for the given substring already exists.
# If the result is already in memo we return the result. Otherwise the number of ways for the given string is determined by making a 
# recursive call to the function with index + 1 for next substring string and index + 2 after checking for valid 2-digit decode. 
# The result is also stored in memo with key as current index, for saving for future overlapping subproblems.

class Solution:
    def recursiveWithMemo(self, index, s):
        # Have we already seen this substring
        if index in self.memo:
            return self.memo[index]
        

        # If you reach the end of the string
        # Return 1 for success.
        if index == len(s):
            return 1

        # If the string starts with a zero, it can't be decoded
        if s[index] == '0':
            return 0

        # we have already checked if the last digit is 0 above, if not 0, then boundary condition for i+2 below
        if index == len(s)-1:
            return 1
        
        answer = self.recursiveWithMemo(index + 1, s)
        if int(s[index : index + 2]) <= 26:
            answer += self.recursiveWithMemo(index + 2, s)
        
        # Save for memoization
        self.memo[index] = answer
        return answer
    
    def numDecodings(self, s: str) -> int:
        self.memo = {}
        return self.recursiveWithMemo(0, s)

s = "12"
s = "226"
# s = "11106"
# s = "0"
# s = "06"
s = "11111110111311121111"
obj = Solution()
print(obj.numDecodings(s))


# Complexity Analysis:
# Time Complexity: O(N), where N is length of the string. Memoization helps in pruning the recursion tree and hence decoding for an 
# index only once. Thus this solution is linear time complexity.
# Space Complexity: O(N). The dictionary used for memoization would take the space equal to the length of the string. There would be 
# an entry for each index value. The recursion stack would also be equal to the length of the string.