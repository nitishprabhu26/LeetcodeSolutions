from typing import List
class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        return [B.index(A[i]) for i in range(len(A))]
            
A = [12, 28, 46, 32, 50]
B = [50, 12, 32, 46, 28]
obj = Solution()
print(obj.anagramMappings(A,B))

