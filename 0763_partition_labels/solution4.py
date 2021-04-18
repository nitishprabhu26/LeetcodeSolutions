# Figure out the rightmost index first and use it to denote the start of the next section.
# Reset the left pointer at the start of each new section.
# Store the difference of right and left pointers + 1 as in the result for each section.

class Solution:
    def partitionLabels(self, S: str) ->[int]:
        rightmost = {c:i for i, c in enumerate(S)}
        left, right = 0, 0

        result = []
        for i, letter in enumerate(S):

            right = max(right,rightmost[letter])
        
            if i == right:
                result += [right-left + 1]
                left = i+1

        return result
            
S = "ababcbacadefegdehijhklij"
obj = Solution()
print(obj.partitionLabels(S))

# Complexity Analysis:
# Time Complexity: O(N), where N is the length of S.
# Space Complexity: O(1) to keep data structure last of not more than 26 characters.