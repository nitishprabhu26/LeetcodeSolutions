# Approach 1: Brute Force

# Intuition:
# We can generate all 2^{2n} sequences of '(' and ')' characters. Then, we will check if each one is valid.

# Algorithm:
# To generate all sequences, we use a recursion. All sequences of length n is just '(' plus all sequences of 
# length n-1, and then ')' plus all sequences of length n-1.
# To check whether a sequence is valid, we keep track of balance, the net number of opening brackets minus closing 
# brackets. If it falls below zero at any time, or doesn't end in zero, the sequence is invalid - otherwise it is 
# valid.


from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(A = []):
            if len(A) == 2*n:
                if valid(A):
                    ans.append("".join(A))
            else:
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()

        def valid(A):
            bal = 0
            for c in A:
                if c == '(': bal += 1
                else: bal -= 1
                if bal < 0: return False
            return bal == 0
        
        ans = []
        generate()
        return ans


n = 3
obj = Solution()
print(obj.generateParenthesis(n))


# Complexity Analysis:
# Time complexity: O([2^{2n}].n). For each of 2^{2n} sequences, we need to create and validate the sequence, 
# which takes O(n) work.
# Space complexity: O([2^{2n}].n). Naively, every sequence could be valid.