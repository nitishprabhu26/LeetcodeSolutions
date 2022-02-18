# O(n^2) approach: Using inbuilt count method

class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i, x in enumerate(s):
            if s.count(x) == 1:
                return i
        return -1


# using indexes : checking if both first and last occurence of a charecter are same
# [ O(n^2) complexity]
# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         for i in range(len(s)):
#             if s.index(s[i]) == s.rindex(s[i]):
#                 return i
#         return -1


s = "leetcode"
obj = Solution()
print(obj.firstUniqChar(s))

# Complexity Analysis:

# Time complexity : O(N^2) since we go through the string of length N once i.e. O(N), and we also use a inbuilt 
# method 'count' [or 'index' and 'rindex'] which does a linear search everytime it is called i.e. O(N).
# Space complexity : O(1) because no extra space is used.