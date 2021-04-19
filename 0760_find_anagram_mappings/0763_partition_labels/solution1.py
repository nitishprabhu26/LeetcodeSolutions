class Solution:
    def anagramMappings(self, A: [int], B: [int]) -> [int]:
        dict={}
        output=[]
        for i,x in enumerate(B):
            dict[x]=i
        for i,x in enumerate(A):
            output.append(dict[x])
        return output
            
A = [12, 28, 46, 32, 50]
B = [50, 12, 32, 46, 28]
obj = Solution()
print(obj.anagramMappings(A,B))
