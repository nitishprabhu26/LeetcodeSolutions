# Approach 1: Enumerate Cases

# Intuition:
# If the characters at the index of i in both strings are identical, i.e. s[i] == goal[i], we call the characters 
# at the index i as matched.
# If swapping s[i] and s[j] would demonstrate that s and goal are buddy strings, 
# then s[i] == goal[j] and s[j] == goal[i]. 
# That means among the four free variables s[i], s[j], goal[i], goal[j], there are only two cases: 
# either s[i] == s[j] or not.

# Algorithm:
# Let's work through the cases.
# - In the case s[i] == s[j] == goal[i] == goal[j], then the strings s and goal are equal. So if s == goal, 
#   we should check each index i for two matches with the same value.
# - In the case s[i] == goal[j], s[j] == goal[i], (s[i] != s[j]), the rest of the indices match. So if s and goal 
#   have only two unmatched indices (say i and j), we should check that the equalities 
#   s[i] == goal[j] and s[j] == goal[i] hold.


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        
        if len(s) != len(goal): 
            return False
        
        # Return True, if s == goal && at least one charecter in 'a' is repeated (at least twice)
        # s = "ab", goal = "ab" -- False
        # s = "aa", goal = "aa" -- True
        # s = "aba", goal = "aba" -- True
        if s == goal:
            seen = set()
            for a in s:
                if a in seen:
                    return True
                seen.add(a)
            return False

        # making a swap
        # s = "ab", goal = "ba"
        # Traverse each index of s and goal simultaneously, and compare them
        # add them to differences array if they are different values
        # at the end, there should be exactly 2 differences (so that only one swap is possible)
        # also if the values of dfferences are reversed, then they should match 
        # if one differences is (x,y), then other has to be (y,x)
        pairs = []
        for a, b in zip(s, goal):
            if a != b:
                pairs.append((a, b))
            if len(pairs) >= 3: 
                return False

        return len(pairs) == 2 and pairs[0] == pairs[1][::-1]


s = "ab"
goal = "ba"
obj = Solution()
print(obj.buddyStrings(s, goal))


# Complexity Analysis:
# Time Complexity: O(N), where N is the length of s and goal.
# Space Complexity: O(1). to store lists, newS and s_list.