# Approach 1: Bit-by-Bit Computation

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = max(len(a), len(b))
        # https://www.w3schools.com/python/ref_string_zfill.asp
        a, b = a.zfill(n), b.zfill(n)

        carry = 0
        answer = []
        for i in range(n - 1, -1, -1):
            if a[i] == '1':
                carry += 1
            if b[i] == '1':
                carry += 1
                
            if carry % 2 == 1:
                answer.append('1')
            else:
                answer.append('0')
            
            carry //= 2
        
        if carry == 1:
            answer.append('1')
        answer.reverse()
        
        return ''.join(answer)
            

a = "11"
b = "1"
obj = Solution()
print(obj.addBinary(a, b))


# Complexity Analysis:
# Time complexity: O(max(N,M)), where N and M are lengths of the input strings a and b.
# Space complexity: O(max(N,M)) to keep the answer.