# Approach 2: Reverse the Whole String and Then Reverse Each Word
# Benefits: could be done in-place for the languages with mutable strings.
# for Java/Python (= immutable strings)

# In the case of immutable strings one has first to convert string into mutable data structure, and hence it makes 
# sense to trim all spaces during that conversion.


class Solution:
    def trim_spaces(self, s: str) -> list:
        left, right = 0, len(s) - 1
        # remove leading spaces
        while left <= right and s[left] == ' ':
            left += 1
        
        # remove trailing spaces
        while left <= right and s[right] == ' ':
            right -= 1
        
        # reduce multiple spaces to single one
        output = []
        while left <= right:
            if s[left] != ' ':
                output.append(s[left])
            elif output[-1] != ' ':
                output.append(s[left])
            left += 1
        
        return output
            
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
            
    def reverseWords(self, s: str) -> str:
        # converst string to char array 
        # and trim spaces at the same time
        l = self.trim_spaces(s)
        
        # reverse the whole string
        self.reverse(l, 0, len(l) - 1)
        
        # reverse each word
        self.reverse_each_word(l)
        
        return ''.join(l)


s = "the sky is blue"
obj = Solution()
print(obj.reverseWords(s))


# Complexity Analysis:
# Time complexity: O(N), where N is a number of characters in the input string.
# Space complexity: O(N).