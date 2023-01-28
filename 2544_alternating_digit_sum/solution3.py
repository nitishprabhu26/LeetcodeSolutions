# Approach: O(N) approach using flag and for loop


class Solution:
    def alternateDigitSum(self, n: int) -> int:
        n = str(n)
        total, flag = 0, True
        
        for ch in n:
            total += int(ch) if flag else -int(ch)
            flag = not flag
            
        return total


n = 521
obj = Solution()
print(obj.alternateDigitSum(n))


# Complexity Analysis:
# Time complexity : O(N).
# Space complexity : O(1).