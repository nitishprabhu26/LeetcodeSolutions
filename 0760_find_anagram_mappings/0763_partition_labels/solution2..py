class Solution:
    def anagramMappings(self, A: [int], B: [int]) -> [int]:
        D = {x: i for i, x in enumerate(B)}
        return [D[x] for x in A]
            
A = [12, 28, 46, 32, 50]
B = [50, 12, 32, 46, 28]
obj = Solution()
print(obj.anagramMappings(A,B))

# Complexity Analysis
# Time Complexity: O(N), where N is the length of A.
# Space Complexity: O(N).
