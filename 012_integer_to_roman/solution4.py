# Using while loop
class Solution:
    def intToRoman(self, num: int) -> str:
        d = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC',
             50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
        
        ans=""  
        
        while(num>0):
            for i in d:
                if i<=num:
                    ans+=(d[i])*int(num/i)
                    num = num % i
                    break
        return ans


num = 29
obj = Solution()
print(obj.intToRoman(num))