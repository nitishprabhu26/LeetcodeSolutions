# Using Queue
# Append 5 to the left, append 10 to the right. Chose where to pop. We don't have to append 20

class Solution:
    def lemonadeChange(self, bills: [int]) -> bool:
        five = ten = 0
        for i in bills:
            if i == 5: five += 1
            elif i == 10: five, ten = five - 1, ten + 1
            elif ten > 0: five, ten = five - 1, ten - 1
            else: five -= 3
            if five < 0: return False
        return True
        
bills = [5,5,5,10,20,5,10]
obj = Solution()
print(obj.lemonadeChange(bills))
