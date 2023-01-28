# Approach: O(N) approach using while loop


class Solution:
    def alternateDigitSum(self, n: int) -> int:
        len_n = len(str(n))
        total = 0
        
        while len_n > 0:
            digit = n % 10
            n = n // 10
            
            if len_n % 2 == 0:
                total -= digit    
            else:
                total += digit  
            len_n -= 1
            
        return total


n = 521
obj = Solution()
print(obj.alternateDigitSum(n))


# Complexity Analysis:
# Time complexity : O(N).
# Space complexity : O(1).