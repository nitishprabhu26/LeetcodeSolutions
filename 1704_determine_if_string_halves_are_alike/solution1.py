# Approach 1: Count Vowels

# Algorithm
# Step 1: Initialize substring a and substring b.
# Step 2: Iterate over a and b, and count the number of vowels respectively.
# Step 3: Return if the numbers of vowels equal.


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)

        a = s[:n//2]
        b = s[n//2:]

        a_vowel_count = 0
        for c in a:
            if c in "aeiouAEIOU":
                a_vowel_count += 1

        b_vowel_count = 0
        for c in b:
            if c in "aeiouAEIOU":
                b_vowel_count += 1

        return a_vowel_count == b_vowel_count
        

s = "textbook"
obj = Solution()
print(obj.halvesAreAlike(s))


# Complexity Analysis:
# Let N be the length of s.
# Time Complexity: O(N), since we need to iterate substring a and b.
# Space complexity : O(N), since we need to store substring a and b.