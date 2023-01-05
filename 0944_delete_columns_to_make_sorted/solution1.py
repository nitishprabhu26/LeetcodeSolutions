# Approach 1: Matrix Traversing

# Algorithm:
# 1. Iterate over the columns from 0 to K - 1, for each column col:
# -  Iterate over the rows row from 1 to N - 1:
# -  If the character at index col in the string strs[row] is smaller than the character at index col in the string strs[row - 1], then increment the counter variable answer. Also, we can break the inner loop here as we find the current column unsorted.
# -  Otherwise, we check the next row.
# 2. Return answer.


from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # number of columns
        K = len(strs[0])
        # Variable to store the count of columns to be deleted.
        answer = 0
        
        # Iterate over each index in the string. (columns)
        for col in range(K):
        # Iterate over the strings. (rows)
            for row in range(1, len(strs)):
                # Characters should be in increasing order, 
                # If not, increment the counter.
                if ord(strs[row][col]) < ord(strs[row - 1][col]):
                # OR
                # if strs[row][col] < strs[row - 1][col]:
                    answer += 1
                    break
                    
        return answer


strs = ["cba","daf","ghi"]
obj = Solution()
print(obj.minDeletionSize(strs))


# Complexity Analysis:
# Here N is the number of strings in the given list strs, and K is the length of each string.
# Time complexity: O(N * K).
# We are iterating over each of the K characters in all the N strings. Although we break early in the case where 
# we find the column unsorted, in the worst case when there is no unsorted column, we will have to iterate over 
# each character. Hence, the total time complexity is O(N * K).
# Space complexity: O(1).
# We don't need any extra space apart from the variable answer used to store the count of unsorted columns.