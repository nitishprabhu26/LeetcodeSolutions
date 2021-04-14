# https://www.geeksforgeeks.org/find-the-nth-row-in-pascals-triangle/
# Efficient Approach: 
# Follow the steps below to optimize the above approach:

# Unlike the above approach, we will just generate only the numbers of the Nth row.
# We can observe that the Nth row of the Pascals triangle consists of following sequence:
# NC0, NC1, ......, NCN - 1, NCN
# Since, NC0 = 1, the following values of the sequence can be generated by the following equation:
# Formula: nth row and rth column
# NCr = ( NC(r - 1) * (N - r + 1)) / r where 1 ≤ r ≤ N

class Solution:
    def getRow(self, rowIndex: int) -> [int]:
        result=[1]
        prev=1
        for i in range(1,rowIndex+1):
            curr=(prev*(rowIndex-i+1))//i
            result.append( curr )
            prev=curr
        return result

row = 277
obj = Solution()
print(obj.getRow(row))

# Complexity Analysis:
# Time complexity : O(k). Each term is calculated once, in constant time.
# Space complexity : O(k). No extra space required other than that required to hold the output.
# Further Thoughts
# The symmetry of a row in Pascal's triangle allows us to get away with computing just half of each row.