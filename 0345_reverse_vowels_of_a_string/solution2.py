# Approach 1: Two Pointers

# Intuition:
# We will initialize two pointers, one pointer (referred as left) pointing to the left end of the input string and 
# the other pointer (named as right) pointing to the right end of the string.
# The only difference compared to the problem 344 Reverse String is that we don't want to swap all characters 
# instead we want to swap just the vowels. So the left and right pointers as we discussed should be pointing to 
# the vowels only.
# To achieve this, we would initialize a left pointer to '0' and keep incrementing it until we get a vowel. 
# Similarly, we initialize the right pointer to the last index and keep decrementing it until it points to a vowel.
# At each such iteration where both the pointers are pointing to the vowel, we would swap the characters at these 
# pointers.

# Algorithm
# 1.Initialize the left pointer start to 0, and the right pointer end to s.size() - 1.
# 2.Keep iterating until the left pointer catches up with the right pointer:
#   -   Keep incrementing the left pointer start until it's pointing to a non-vowel character.
#   -   Keep decrementing the right pointer end until it's pointing to a non-vowel character.
#   -   Swap the characters at the start and end.
#   -   Increment the start pointer and decrement the end pointer.
# 3. Return the string s.


class Solution:
    def reverseVowels(self, s: str) -> str:
        def isVowel(c):
            return c in "aeiouAEIOU"
        
        def swap(x, y):
            s_list[x], s_list[y] = s_list[y], s_list[x]
            
            
        # Convert String to array as String is immutable in Python
        s_list = list(s)
        # initialize two pointers
        start = 0
        end = len(s) - 1
        
        
        # While we still have characters to traverse
        while start < end:
            # Find the leftmost vowel
            while start < len(s) and not isVowel(s_list[start]):
                start += 1
                
            # Find the rightmost vowel
            while end >= 0 and not isVowel(s_list[end]):
                end -= 1
            
            # Swap them if start is left of end
            if start < end:
                swap(start, end)
                start += 1
                end -= 1
                
                
        # Converting array back to String
        return "".join(s_list)


s = "leetcode"
obj = Solution()
print(obj.reverseVowels(s))


# Complexity analysis:
# Here, N is the length of the string s.
# Time complexity : O(N).It might be tempting to say that there are two nested loops and hence the complexity 
# would be O(N^2). However, if we observe closely the pointers start and end will only traverse the index once. 
# Each element of the string s will be iterated only once either by the left or right pointer and not both. We 
# swap characters when both pointers point to vowels which are O(1) operation. Hence the total time complexity 
# will be O(N).
# Space complexity : O(N). we need to convert the string to an array that would take O(N) space.

