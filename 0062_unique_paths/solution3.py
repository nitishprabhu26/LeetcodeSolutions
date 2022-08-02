# Approach : Neetcode
# https://youtu.be/IlEsdxuD4lY


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # defining bottom row
        row = [1] * n
        
        # going through all rows, except for the last row
        for i in range(m - 1):
            newRow = [1] * n
            # go through every column , except the rightmost column
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
            
        return row[0]
        

m = 23
n = 12
obj = Solution()
print(obj.uniquePaths(m, n))


# Complexity Analysis:
# Time complexity: O(N × M).
# Space complexity: O(N). N - number of columns ie. the length of a row