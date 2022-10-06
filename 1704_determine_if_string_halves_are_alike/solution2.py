# Approach 2: Count Vowels (In Place)

# Algorithm:
# Step 1: Iterate over the first half of s (i.e., a) and the second half of s (i.e., b). Count the number of 
# vowels respectively.
# Step 2: Return if the numbers of vowels equal.


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)

        a_vowel_count = 0
        for i in range(0, n//2):
            if s[i] in "aeiouAEIOU":
                a_vowel_count += 1

        b_vowel_count = 0
        for i in range(n//2, n):
            if s[i] in "aeiouAEIOU":
                b_vowel_count += 1

        return a_vowel_count == b_vowel_count
        

s = "textbook"
obj = Solution()
print(obj.halvesAreAlike(s))


# Complexity Analysis:
# Let N be the length of s.
# Time Complexity: O(N), since we need to iterate substring a and b.
# Space complexity : O(1), since we do not need extra space. Here we do not take the input s into consideration.