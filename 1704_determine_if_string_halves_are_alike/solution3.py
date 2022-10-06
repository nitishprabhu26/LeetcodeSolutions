# Approach 3: Count Vowels (In Place + Function)

# Algorithm:
# Step 1: Initialize a function that counts vowels.
# Step 2: Count the number of vowels of the first half of s (i.e., a) and the second half of s (i.e., b) with that 
# function.
# Step 3: Return if the number of vowels equals.


class Solution:
    def halvesAreAlike(self, s: str) -> bool:

        def countVowel(start, end, s):
            answer = 0
            for i in range(start, end):
                if s[i] in "aieouAIEOU":
                    answer += 1
            return answer

        n = len(s)

        return countVowel(0, n//2, s) == countVowel(n//2, n, s)
        

s = "textbook"
obj = Solution()
print(obj.halvesAreAlike(s))


# Complexity Analysis:
# Let N be the length of s.
# Time Complexity: O(N), since we need to iterate substring a and b.
# Space complexity : O(1), since we do not need extra space. Here we do not take the input s into consideration.