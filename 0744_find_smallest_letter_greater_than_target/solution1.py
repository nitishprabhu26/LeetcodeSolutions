# Approach #1: Record Letters Seen [Accepted]

# Intuition and Algorithm:
# Let's scan through letters and record if we see a letter or not. We could do this with an array of size 26, or 
# with a Set structure.
# Then, for every next letter (starting with the letter that is one greater than the target), let's check if we've 
# seen it. If we have, it must be the answer.


from typing import List

# using a Set structure.
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        seen = set(letters)
        for i in range(1, 26):
            cand = chr((ord(target) - ord('a') + i) % 26 + ord('a'))
            if cand in seen:
                return cand
            

# OR
# using array of size 26

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        seen = [None] * 26
        
        for c in letters:
            seen[ord(c) - ord('a')] = True
                    
        while True:
            target = chr(ord(target) + 1)
            
            if ord(target) > ord('z'):
                target = 'a'
            
            if seen[ord(target) - ord('a')]:
                return target



letters = ["c","f","j"]
target = "a"
obj = Solution()
print(obj.nextGreatestLetter(letters, target))


# Complexity Analysis:
# Time Complexity: O(N), where N is the length of letters. We scan every element of the array.
# Space Complexity: O(1), the maximum size of seen.