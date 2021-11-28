# Approach 1: Recursive Approach without Memoization
# https://leetcode.com/problems/decode-ways/solution/
# Time Limit Exceeded for longer inputs

class Solution:
    def recursiveWithoutMemo(self, index, s):
        # If you reach the end of the string
        # Return 1 for success.
        if index == len(s):
            return 1

        # If the string starts with a zero, it can't be decoded
        if s[index] == '0':
            return 0

        if index == len(s)-1:
            return 1
        
        answer = self.recursiveWithoutMemo(index + 1, s)
        if int(s[index : index + 2]) <= 26:
            answer += self.recursiveWithoutMemo(index + 2, s)

        return answer
    
    def numDecodings(self, s: str) -> int:
        return self.recursiveWithoutMemo(0, s)

s = "12"
s = "226"
s = "11106"
# s = "0"
# s = "06"
# Time Limit Exceeded
s = "11111110111311121111"
obj = Solution()
print(obj.numDecodings(s))