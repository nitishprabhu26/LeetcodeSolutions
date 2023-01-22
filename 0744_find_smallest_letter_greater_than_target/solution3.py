# Approach #3: Binary Search [Accepted]

# Intuition and Algorithm:
# Like in Approach #2, we want to find something larger than target in a sorted array. This is ideal for a binary 
# search: Let's find the rightmost position to insert target into letters so that it remains sorted.
# Our binary search (a typical one) proceeds in a number of rounds. At each round, let's maintain the loop 
# invariant that the answer must be in the interval [lo, hi]. Let mi = (lo + hi) // 2. 
# If letters[mi] <= target, then we must insert it in the interval [mi + 1, hi]. 
# Otherwise, we must insert it in the interval [lo, mi].
# At the end, if our insertion position says to insert target into the last position letters.length, we return 
# letters[0] instead. This is what the modulo operation does.


import bisect
from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        index = bisect.bisect(letters, target)
        return letters[index % len(letters)]
            

# OR

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        lo, hi = 0, len(letters) 
        while lo < hi:
            mi = lo + (hi - lo) // 2
            
            if letters[mi] <= target:
                lo = mi + 1
            else:
                hi = mi
            
        return letters[lo % len(letters)]


# OR
# https://youtu.be/uZKCnU0ynNw

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        res = letters[0]
        left, right = 0, len(letters) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if letters[mid] < target:
                left = mid + 1
            elif letters[mid] == target:
                left = mid + 1
            else:
                res = letters[mid]
                right = mid - 1
        
        return res


letters = ["c","f","j"]
target = "a"
obj = Solution()
print(obj.nextGreatestLetter(letters, target))


# Complexity Analysis:
# Time Complexity: O(logN), where N is the length of letters. We peek only at logN elements in the array.
# Space Complexity: O(1), as we maintain only pointers.