# Approach: Using Counters
# https://youtu.be/wA3ZE0iZgG8


from collections import Counter

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        c1, c2 = Counter(s), Counter(goal)
        
        # different lengths, different charecters
        if c1 != c2: 
            return False
        
        # check how many indexes between s and goal are different
        diff = sum([1 for i in range(len(s)) if s[i] != goal[i]])
        
        if diff == 2:
            return True
        elif diff == 0:
            # check if we have more than one repeated charecter
            return any([cnt > 1 for char, cnt in c1.items()])
        else:
            return False


s = "ab"
goal = "ba"
obj = Solution()
print(obj.buddyStrings(s, goal))


# Complexity Analysis:
# Time Complexity: O(N), where N is the length of s and goal.
# Space Complexity: O(1). Even considering couter, which has limited number of characters.