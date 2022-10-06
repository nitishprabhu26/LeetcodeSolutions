# Approach: Count Vowels using while loop


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set('aeiouAEIOU')
        a = b = 0
        i, j = 0, len(s) - 1
        
        while i < j:
            a += s[i] in vowels
            b += s[j] in vowels
            i += 1
            j -= 1
            
        return a == b
        

s = "textbook"
obj = Solution()
print(obj.halvesAreAlike(s))


# Complexity Analysis:
# Let N be the length of s.
# Time Complexity: O(N), since we need to iterate once.(or N/2 to be exact)
# Space complexity : O(N), for the set.