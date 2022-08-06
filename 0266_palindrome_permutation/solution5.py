# Approach #5 Using Set [Accepted]:

# Another modification of the last approach could be by making use of a set for keeping track of the number of 
# elements with odd number of occurrences in s. For doing this, we traverse over the characters of the string s. 
# Whenever the number of occurrences of a character becomes odd, we put its entry in the set. Later on, if we find 
# the same element again, lead to its number of occurrences as even, we remove its entry from the set. Thus, if 
# the element occurs again(indicating an odd number of occurrences), its entry won't exist in the set.

# Based on this idea, when we find a character in the string s that isn't present in the set(indicating an odd 
# number of occurrences currently for this character), we put its corresponding entry in the set. If we find a 
# character that is already present in the set(indicating an even number of occurrences currently for this 
# character), we remove its corresponding entry from the set.

# At the end, the size of set indicates the number of elements with odd number of occurrences in s. If it is 
# lesser than 2, a palindromic permutation of the string s is possible, otherwise not.


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        char_set = set()
        
        for i in s:
            if i not in char_set:
                char_set.add(i)
            else:
                char_set.remove(i)
            
        return len(char_set) <= 1


s = "code"
obj = Solution()
print(obj.canPermutePalindrome(s))


# Complexity Analysis:
# Time complexity : O(n). We traverse over the string s of length n once only.
# Space complexity : O(1). The set can grow up to a maximum number of all distinct elements. However, the number 
# of distinct characters are bounded, so as the space complexity.