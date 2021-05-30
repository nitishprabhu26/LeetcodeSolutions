class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        longest_1=0
        longest_0=0
        c1=0
        c0=0
        for i in range(len(s)):
            if s[i]=="1":
                c1+=1
                if c0 > longest_0:
                    longest_0 = c0
                c0=0
            else:
                c0+=1
                if c1 > longest_1:
                    longest_1 = c1
                c1=0
        if c1>longest_1:
            longest_1=c1
        if c0>longest_0:
            longest_0=c0
            
        return True if longest_1>longest_0 else False
            
s = "110100010111"
obj = Solution()
print(obj.checkZeroOnes(s))
