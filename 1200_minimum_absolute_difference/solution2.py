# using single for loop:
class Solution:
    def minimumAbsDifference(self, arr: [int]) -> [[int]]:
        result = []
        arr.sort()
        min_value = float("inf")
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i] == min_value:
                result.append([ arr[i] , arr[i+1] ])
            elif arr[i+1]-arr[i] < min_value:
                result=[]
                min_value = arr[i+1]-arr[i]
                result.append([ arr[i] , arr[i+1] ])
        return result

# inp = [3,8,-10,23,19,-4,-14,27]
inp = [4,2,1,3]
obj = Solution()
print(obj.minimumAbsDifference(inp))