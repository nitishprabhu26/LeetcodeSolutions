# Approach #3 Using Array [Accepted]

# Instead of making use of the inbuilt Hashmap, we can make use of an array as a hashmap. For this, we make use of 
# an array map with length 128. Each index of this map corresponds to one of the 128 ASCII characters possible.

# We traverse over the string s and put in the number of occurrences of each character in this map appropriately 
# as done in the last case. Later on, we find the number of characters with odd number of occurrences to determine 
# if a palindromic permutation is possible for the string s or not as done in previous approaches.


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        char_count_array = [0] * 128
        count = 0
        
        for i in s:
            char_count_array[ord(i)] = char_count_array[ord(i)] + 1
        
        for cnt in char_count_array:
            if cnt % 2 == 1:
                count += 1
            
        return count <= 1


s = "code"
obj = Solution()
print(obj.canPermutePalindrome(s))


# Complexity Analysis:
# Time complexity : O(n). We traverse once over the string s of length n. Then, we traverse over the map of length 
# 128(constant).
# Space complexity : O(1). Constant extra space is used for map of size 128.