# Approach 1: Count and Write [Accepted]

# Intuition:
# Let's first write to our answer the elements of T that occur in S, in order of S. After, we'll write any 
# elements of T we didn't write. This obviously keeps all the ordering relationships we wanted.
# In the second write, the order doesn't matter because those elements aren't in S, so there are no ordering 
# relationships these elements have to satisfy.

# Algorithm:
# The trick is to count the elements of T. After we have some 
# count[char] = (the number of occurrences of char in T), we can write these elements in the order we want. The 
# order is S + (characters not in S in any order).


import collections

class Solution(object):
    def customSortString(self, S, T):
        # count[char] will be the number of occurrences of
        # 'char' in T.
        count = collections.Counter(T)
        ans = []

        # Write all characters that occur in S, in the order of S.
        for c in S:
            ans.append(c * count[c])
            # Set count[c] = 0 to denote that we do not need
            # to write 'c' to our answer anymore.
            count[c] = 0

        # Write all remaining characters that don't occur in S.
        # That information is specified by 'count'.
        for c in count:
            ans.append(c * count[c])

        return "".join(ans)


S = "cba"
T = "abcd"
obj = Solution()
print(obj.customSortString(S, T))


# Complexity Analysis:
# Time Complexity: O(S.length+T.length), the time it takes to iterate through S and T
# Space Complexity: O(T.length). We count at most 26 different lowercase letters, but the final answer has the 
# same length as T.