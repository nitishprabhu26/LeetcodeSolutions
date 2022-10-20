# Approach #2: Simple Check [Accepted]

# Intuition and Algorithm:
# All rotations of A are contained in A+A. Thus, we can simply check whether B is a substring of A+A. We also need 
# to check A.length == B.length, otherwise we will fail cases like A = "a", B = "aa".


class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        return len(A) == len(B) and B in A+A


s = "abcde"
goal = "cdeab"
obj = Solution()
print(obj.rotateString(s, goal))


# Complexity Analysis:
# Time Complexity: O(N^2), where N is the length of A.
# Space Complexity: O(N), the space used building A+A.