# Approach #2 Using HashMap [Accepted]

# We need to count the number of characters with odd number of occurrences in the given string s. To do so, we can 
# also make use of a hashmap. This map takes the form (character, number of occurrences of character).


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        char_count_map = {}
        count = 0
        
        for i in s:
            char_count_map[i] = char_count_map.get(i,0) + 1
        
        for ch, cnt in char_count_map.items():
            if cnt % 2 == 1:
                count += 1
            
        return count <= 1


s = "code"
obj = Solution()
print(obj.canPermutePalindrome(s))


# Complexity Analysis:
# Time complexity : O(n). We traverse over the given string s with n characters once. We also traverse over the 
# map which can grow up to a size of n in case all characters in s are distinct.
# Space complexity : O(1). The map can grow up to a maximum number of all distinct elements. However, the number 
# of distinct characters are bounded, so as the space complexity.