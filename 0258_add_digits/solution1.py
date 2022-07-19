# The value we're asked to compute is the so-called Digital Root.
# https://en.wikipedia.org/wiki/Digital_root
# Logarithmic time solution is easy to write:

class Solution:
    def addDigits(self, num: int) -> int:
        digital_root = 0
        
        while num > 0:
            digital_root += num % 10
            num = num //10
            
            if num == 0 and digital_root>9:
                num = digital_root
                digital_root = 0
            
        return digital_root


num = 38
obj = Solution()
print(obj.addDigits(num))


# Complexity Analysis:
# Time Complexity: O(log n).
# Space Complexity: O(1).