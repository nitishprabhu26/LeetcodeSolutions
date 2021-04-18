# Approach 1: Greedy

# Intuition:
# Let's try to repeatedly choose the smallest left-justified partition. Consider the first label, say it's 'a'. 
# The first partition must include it, and also the last occurrence of 'a'. However, between those two occurrences of 'a', 
# there could be other labels that make the minimum size of this partition bigger. For example, in "abccaddbeffe", 
# the minimum first partition is "abccaddb". This gives us the idea for the algorithm: For each letter encountered, 
# process the last occurrence of that letter, extending the current partition [anchor, j] appropriately.

# Algorithm:
# We need an array last[char] -> index of S where char occurs last. Then, let anchor and j be the start and end of the 
# current partition. If we are at a label that occurs last at some index after j, we'll extend the partition j = last[c]. 
# If we are at the end of the partition (i == j) then we'll append a partition size to our answer, and set the start of our 
# new partition to i+1.

class Solution:
    def partitionLabels(self, S: str) ->[int]:
        last = { x:i for i,x in enumerate(S)}
        result = []
        anchor = j = 0
        
        for i,x in enumerate(S):
            j = max(j, last[x])
            if i == j:
                result.append( i-anchor+1 )
                anchor = i + 1
        return result
            
S = "ababcbacadefegdehijhklij"
obj = Solution()
print(obj.partitionLabels(S))

# Complexity Analysis:
# Time Complexity: O(N), where N is the length of S.
# Space Complexity: O(1) to keep data structure last of not more than 26 characters.