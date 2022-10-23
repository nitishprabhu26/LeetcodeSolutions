# Approach: Brute force [Time Limit Exceeded]
# Swap all possible indices of 's'


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        s_list = list(s)
        for i in range(len(s_list)):
            for j in range(i + 1, len(s_list)):
                newS = s_list.copy()
                newS[i], newS[j] = newS[j], newS[i] 
                if ''.join(newS) == goal:
                    return True
        return False


s = "ab"
goal = "ba"
obj = Solution()
print(obj.buddyStrings(s, goal))


# Complexity Analysis:
# Time Complexity: O(N^2), where N is the length of s.
# Space Complexity: O(N). to store lists, newS and s_list.