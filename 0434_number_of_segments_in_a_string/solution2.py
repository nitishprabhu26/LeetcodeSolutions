# Approach #2 In-place [Accepted]

# Intuition:
# If we cannot afford to allocate linear additional space, a fairly simple algorithm can deduce the number of 
# segments in linear time and constant space.

# Algorithm:
# To count the number of segments, it is equivalent to count the number of string indices at which a segment begins.
# Therefore, by formally defining the characteristics of such an index, we can simply iterate over the string and 
# test each index in turn. Such a definition is as follows: a string index begins a segment if it is preceded by 
# whitespace (or is the first index) and is not whitespace itself, which can be checked in constant time. Finally, 
# we simply return the number of indices for which the condition is satisfied.


class Solution:
    def countSegments(self, s: str) -> int:
        segment_count = 0

        for i in range(len(s)):
            if (i == 0 or s[i-1] == ' ') and s[i] != ' ':
                segment_count += 1

        return segment_count


# OR
# one liner


class Solution:
    def countSegments(self, s: str) -> int:
        return sum(s[i] != ' ' and (i == 0 or s[i-1] == ' ') for i in range(len(s)))
        

s = "Hello, my name is John"
obj = Solution()
print(obj.countSegments(s))


# Complexity Analysis:
# Time Complexity: We do constant time check for each of the string's n indices, so the runtime is overall linear.
# Space Complexity: There are only a few integers allocated, so the memory footprint is constant.