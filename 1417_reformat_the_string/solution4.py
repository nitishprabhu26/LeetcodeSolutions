class Solution:
    def reformat(self, s: str) -> str:
        A = [c for c in s if c.isalpha()]
        B = [c for c in s if c.isdigit()]
        res = []
        while A and B:
            res += [A.pop(), B.pop()]
        
        return '' if abs(len(A) - len(B)) > 1 else ''.join(B + res + A)

num1 = "abcde13456"
obj = Solution()
print(obj.reformat(num1))