class Solution:
    def anagramMappings(self, A: [int], B: [int]) -> [int]:
        result = [0] * len(A)
        return [B.index(A[i]) for i in range(len(A))]
            
A = [12, 28, 46, 32, 50]
B = [50, 12, 32, 46, 28]
obj = Solution()
print(obj.anagramMappings(A,B))

