# Approach: https://youtu.be/rrWsOBDybZE


import collections

class Solution:
    def customSortString(self, S: str, T: str) -> str:
        s_counts = collections.Counter(T)
        
        string_builder = []

        # all the elements of T that occur in S, in order of S
        for char in S:
            if char in s_counts:
                string_builder.extend( [char] * s_counts[char])

                del s_counts[char]
            
        # write any elements of T we didn't write before (in any order)
        for char, counts in s_counts.items():
            string_builder.extend( [char] * counts)
                
        return ''.join(string_builder)


S = "cba"
T = "abcd"
obj = Solution()
print(obj.customSortString(S, T))


# Complexity Analysis:
# Time Complexity: O(S) + O(T).
# Space Complexity: O(S) + O(T). O(T) for string_builder, O(S) for counter.