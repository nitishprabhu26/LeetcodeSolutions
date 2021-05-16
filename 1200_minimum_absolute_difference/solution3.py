class Solution:
    def minimumAbsDifference(self, arr: [int]) -> [[int]]:
        arr.sort()
        min_diff = min(arr[i+1]-arr[i] for i in range(len(arr) - 1))
        return [[arr[i],arr[i+1]] for i in range(len(arr) - 1) if arr[i+1] - arr[i] == min_diff]

inp = [3,8,-10,23,19,-4,-14,27]
# inp = [4,2,1,3]
obj = Solution()
print(obj.minimumAbsDifference(inp))


# Statements:
# sort array in O(nlogn) runtime complexity and O(1) space complexity
# find min diff in O(n) runtime complexity and O(1) space complexity using generator comprehension
# return all pairs matching min diff in O(n) runtime complexity and O(n) space complexity using list comprehension