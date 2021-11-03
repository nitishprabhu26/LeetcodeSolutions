from typing import List


class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        dict = {}
        output = []
        for i, x in enumerate(B):
            dict[x] = i
        for i, x in enumerate(A):
            output.append(dict[x])
        return output


A = [12, 28, 46, 32, 50]
B = [50, 12, 32, 46, 28]
obj = Solution()
print(obj.anagramMappings(A, B))

# Complexity Analysis:
# Time Complexity: O(N), where N is the length of A.
# Space Complexity: O(N).
