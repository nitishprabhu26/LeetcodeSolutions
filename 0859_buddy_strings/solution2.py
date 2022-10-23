# Approach: https://youtu.be/5DNijHoMjzg


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        # End goal: We have to swap s, so that s == goal
        
        if len(s) != len(goal): 
            return False
        
        # Return True, if s == goal && at least one charecter in 'a' is repeated (at least twice)
        # s = "ab", goal = "ab" -- False
        # s = "aa", goal = "aa" -- True
        # s = "aba", goal = "aba" -- True
        if s == goal and len(set(s)) < len(s):
            return True
             
        # making a swap
        # s = "ab", goal = "ba"
        # Traverse each index of s and goal simultaneously, and compare them
        # add them to differences array if they are different values
        # at the end, there should be exactly 2 differences (so that only one swap is possible)
        # also if the values of dfferences are reversed, then they should match 
        # if one differences is (x,y), then other has to be (y,x)
        differences = []
        for x in range(len(s)):
            if s[x] != goal[x]:
                differences.append([s[x], goal[x]])
        
        if len(differences) == 2 and differences[0] == differences[1][::-1]:
            return True
        
        return False


s = "ab"
goal = "ba"
obj = Solution()
print(obj.buddyStrings(s, goal))


# Complexity Analysis:
# Time Complexity: O(N), where N is the length of s and goal.
# Space Complexity: O(1).