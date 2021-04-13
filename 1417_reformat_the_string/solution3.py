# The idea is to swap a and b such that len(a) > len(b)

class Solution:
    def reformat(self, s: str) -> str:
        l = [c for c in s if c.isalpha()]
        d = [c for c in s if c.isdigit()]
        
        if len(l) < len(d): l,d = d,l
        if len(l) - len(d)> 1 : return ""
        
        result=[]
        while l:
            result.append(l.pop())
            if d: result.append(d.pop())   
        return ''.join(result)

num1 = "abcde123456"
obj = Solution()
print(obj.reformat(num1))