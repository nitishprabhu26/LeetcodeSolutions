# Approach #1: Build String [Accepted]

# Intuition:
# Let's individually build the result of each string (build(S) and build(T)), then compare if they are equal.

# Algorithm:
# To build the result of a string build(S), we'll use a stack based approach, simulating the result of each 
# keystroke.


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(S):
            ans = []
            for c in S:
                if c != '#':
                    ans.append(c)
                elif ans:
                    ans.pop()
            return "".join(ans)
        
        return build(s) == build(t)


s = "ab#c" 
t = "ad#c"
obj = Solution()
print(obj.backspaceCompare(s, t))


# Complexity Analysis:
# Time Complexity: O(M + N), where M, N are the lengths of S and T respectively.
# Space Complexity: O(M + N).