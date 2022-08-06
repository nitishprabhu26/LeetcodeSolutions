# Approach #4 Single Pass [Accepted]:

# Instead of first traversing over the string s for finding the number of occurrences of each element and then 
# determining the count of characters with odd number of occurrences in s, we can determine the value of count 
# on the fly while traversing over s.

# We start of with a count value of 0. If the value of the entry just updated in map happens to be odd, we 
# increment the value of count to indicate that one more character with odd number of occurrences has been found. 
# But, if this entry happens to be even, we decrement the value of count to indicate that the number of characters 
# with odd number of occurrences has reduced by one.

# But, in this case, we need to traverse till the end of the string to determine the final result, unlike the last 
# approaches, where we could stop the traversal over map as soon as the count exceeded 1.


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        char_count_array = [0] * 128
        count = 0
        
        for i in s:
            char_count_array[ord(i)] = char_count_array[ord(i)] + 1
            
            if char_count_array[ord(i)] % 2 == 0:
                count -= 1
            else:
                count += 1
            
        return count <= 1


s = "code"
obj = Solution()
print(obj.canPermutePalindrome(s))


# Complexity Analysis:
# Time complexity : O(n). We traverse over the string s of length n once only.
# Space complexity : O(1). A map of constant size(128) is used.