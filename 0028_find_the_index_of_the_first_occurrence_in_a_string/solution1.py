# Approach : Using inbuilt methods - Find/Index
# https://www.geeksforgeeks.org/difference-between-find-and-index-in-python/
# So we use find method, instead of index
# Note: The index() method is similar to find(). The only difference is find() returns -1 if the searched string 
# is not found and index() throws an exception in this case.


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


haystack = "sadbutsad"
needle = "sad"
obj = Solution()
print(obj.strStr(haystack, needle))


# Complexity Analysis:
# Time Complexity: O(N^2) or O(N*M), Even if you had turned the strings into lists before checking them, you are 
# doing an O(n) comparison inside an O(n) loop. Your code would still be O(n^2) 
# (more generally O(M*N) where M is the length of needle, N is the length of haystack)
# Space Complexity: O(1).