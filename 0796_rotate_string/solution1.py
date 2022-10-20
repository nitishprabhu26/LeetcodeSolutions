# Approach #1: Brute Force [Accepted]

# Intuition:
# For each rotation of A, let's check if it equals B.

# Algorithm:
# More specifically, say we rotate A by s. Then, instead of A[0], A[1], A[2], ..., 
# we have A[s], A[s+1], A[s+2], ...; and we should check that A[s] == B[0], A[s+1] == B[1], A[s+2] == B[2], etc.


class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        if len(A) == 0:
            return True

        for s in range(len(A)):
            if all(A[(s+i) % len(A)] == B[i] for i in range(len(A))):
                return True
        return False


# OR
# By creating a new String

class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        if len(A) == 0:
            return True
        
        newStr = A
        for s in range(len(A)):
            newStr = newStr[1:] + newStr[0]
            if newStr == B:
                return True
        
        return False


s = "abcde"
goal = "cdeab"
obj = Solution()
print(obj.rotateString(s, goal))


# Complexity Analysis:
# Time Complexity: O(N^2), where N is the length of A. For each rotation s, we check up to N elements in A and B.
# Space Complexity: O(1). We only use pointers to elements of A and B.