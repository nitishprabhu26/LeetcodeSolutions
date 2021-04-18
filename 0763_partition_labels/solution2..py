class Solution:
    def partitionLabels(self, S: str) ->[int]:
        sizes = []
        while S:
            i = 1
            while set(S[:i]) & set(S[i:]):
                i += 1
            sizes.append(i)
            S = S[i:]
        return sizes
            
S = "ababcbacadefegdehijhklij"
obj = Solution()
print(obj.partitionLabels(S))

# Complexity Analysis:
# Time Complexity: O(N), where N is the length of S.
# Space Complexity: O(1) to keep data structure last of not more than 26 characters.


# Comment:
# As strings are immutable (https://developers.google.com/edu/python/strings), for each iteration we are creating a new string.
# So for a string of length of 500 characters, we are actually creating 500 strings in memory.
# - This solution is extremely inefficient. code doesn't even beat 5%. O(n)^3?

# Intersection should really be thought of as O(min(len(front), len(back))). Plus the sets can have at most 26 elements, 
# so in that sense it's even O(1).
# But building the two sets takes Ω(len(S)) and should be thought of as O(len(S)), also with a low hidden constant. 
# Overall algorithm thus O(n)^2 with low hidden constant (where N is the original given string's length).
# The data structure behind sets is a hash table.

# Average:     O(min(len(s), len(t))
# Worst case:  O(len(s) * len(t))
# https://wiki.python.org/moin/TimeComplexity#set