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

# Explanation:
# Count the number of $5 and $10 in hand.

# if (customer pays with $5) five++;
# if (customer pays with $10) ten++, five--;
# if (customer pays with $20) ten--, five-- or five -= 3;

# Check if five is positive, otherwise return false.

# Time Complexity:
# Time O(N) for one iteration
# Space O(1)