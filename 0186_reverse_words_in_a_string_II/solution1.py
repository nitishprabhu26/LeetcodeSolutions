# Approach 1: Reverse the Whole String and Then Reverse Each Word

# Algorithm
# Let's first implement two functions:
# - reverse(l: list, left: int, right: int), which reverses array characters between left and right pointers. 
#   C++ users could directly use built-in std::reverse.
# - reverse_each_word(l: list), which uses two pointers to mark the boundaries of each word and previous function 
#   to reverse it.
# Now reverseWords(s: List[str]) implementation is straightforward:
# - Reverse the whole string: reverse(s, 0, len(s) - 1).
# - Reverse each word: reverse_each_word(s).


from typing import List


class Solution:
    def reverse(self, l: list, left: int, right: int) -> None:
        while left < right:
            l[left], l[right] = l[right], l[left]
            left, right = left + 1, right - 1
            
    def reverse_each_word(self, l: list) -> None:
        n = len(l)
        start = end = 0
        
        while start < n:
            # go to the end of the word
            while end < n and l[end] != ' ':
                end += 1
            # reverse the word
            self.reverse(l, start, end - 1)
            # move to the next word
            start = end + 1
            end += 1
            
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # reverse the whole string
        self.reverse(s, 0, len(s) - 1)
        
        # reverse each word
        self.reverse_each_word(s)
        

s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
obj = Solution()
obj.reverseWords(s)
print(s)


# Complexity Analysis:
# Time complexity: O(N), it's two passes along the string.
# Space complexity: O(1), it's a constant space solution.