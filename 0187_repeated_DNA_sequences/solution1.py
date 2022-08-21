# Approach 1: Linear-time Slice Using Substring + HashSet
# https://leetcode.com/problems/repeated-dna-sequences/solution/
# - Linear-time window slice O(L) is easy stupid, just take a substring. Overall that would result in O((N−L).L) 
#   time complexity and huge space consumption in the case of large sequences.
# - Constant-time slice O(1) is where the fun starts, because the way you choose will show your actual background. 
#   There are two ways to proceed: (Not implemented)
#   -   Rabin-Karp = constant-time slice using rolling hash algorithm.
#   -   Bit manipulation = constant-time slice using bitmasks.
# - Last two approaches have O(N−L) time complexity and moderate space consumption even in the case of large 
#   sequences.

# Algorithm:
# - Move a sliding window of length L along the string of length N.
# - Check if the sequence in the sliding window is in the hashset of already seen sequences.
#   -   If yes, the repeated sequence is right here. Update the output.
#   -   If not, save the sequence in the sliding window in the hashset.


from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        L, n = 10, len(s)     
        seen, output = set(), set()

        # iterate over all sequences of length L
        for start in range(n - L + 1):
            tmp = s[start:start + L]
            if tmp in seen:
                output.add(tmp[:])
            seen.add(tmp)
        return output
            

s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
obj = Solution()
print(obj.findRepeatedDnaSequences(s))


# Complexity Analysis:
# Time Complexity: O((N−L).L), that is 'O(N)' for the constant L = 10. 
# In the loop executed (N - L + 1) times, one builds a substring of length L. Overall that results in O((N−L).L) 
# time complexity.
# Space Complexity: O((N−L).L) to keep the hashset, that results in 'O(N)' for the constant L = 10.