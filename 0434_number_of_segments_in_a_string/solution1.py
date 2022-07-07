# Approach #1 Using Language Builtins [Accepted]

class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())
        

s = "Hello, my name is John"
obj = Solution()
print(obj.countSegments(s))


# Complexity Analysis:
# Time Complexity: O(n). All builtin language functionality used here runs in either O(n) or O(1) time, so the 
# entire algorithm runs in linear time.
# Space Complexity: O(n). Split returns an array/list of O(n) length, so the algorithm uses linear additional space.