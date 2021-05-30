# using Split method:
class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        split_1=s.split("0")
        split_0=s.split("1")
        longest_1 = max([len(i) for i in split_1])
        longest_0 = max([len(i) for i in split_0])
        
        return longest_1>longest_0
            
s = "110"
obj = Solution()
print(obj.checkZeroOnes(s))
