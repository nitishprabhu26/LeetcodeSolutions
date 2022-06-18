# Approach 3: Deque of Words
# Two passes approach with a deque. Move along the string, word by word, and push each new word in front of the 
# deque. Convert the deque back into string. Benefits: two passes.


from collections import deque

class Solution:
    def reverseWords(self, s: str) -> str:
        left, right = 0, len(s) - 1
        # remove leading spaces
        while left <= right and s[left] == ' ':
            left += 1
        
        # remove trailing spaces
        while left <= right and s[right] == ' ':
            right -= 1
            
        d, word = deque(), []
        # push word by word in front of deque
        while left <= right:
            if s[left] == ' ' and word:
                d.appendleft(''.join(word))
                word = []
            elif s[left] != ' ':
                word.append(s[left])
            left += 1
        d.appendleft(''.join(word))
        
        return ' '.join(d)


s = "the sky is blue"
obj = Solution()
print(obj.reverseWords(s))


# Complexity Analysis:
# Time complexity: O(N), where N is a number of characters in the input string.
# Space complexity: O(N), to store the result of split by spaces.