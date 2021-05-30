import re
class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        longest_1=0
        longest_0=0
        try:
            longest_1 = len(max(re.findall("11*",s)))
            longest_0 = len(max(re.findall("00*",s)))
        except:
            None
            print(longest_1,longest_0)
            
        return True if longest_1>longest_0 else False
            
s = "1011"
obj = Solution()
print(obj.checkZeroOnes(s))
