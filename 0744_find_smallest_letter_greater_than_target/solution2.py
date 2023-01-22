# Approach #2: Linear Scan [Accepted]

# Intuition and Algorithm:
# Since letters are sorted, if we see something larger when scanning form left to right, it must be the answer. 
# Otherwise, (since letters is non-empty), the answer is letters[0].


from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for c in letters:
            if c > target:
                return c
        return letters[0]
            

letters = ["c","f","j"]
target = "a"
obj = Solution()
print(obj.nextGreatestLetter(letters, target))


# Complexity Analysis:
# Time Complexity: O(N), where N is the length of letters. We scan every element of the array.
# Space Complexity: O(1), as we maintain only pointers.