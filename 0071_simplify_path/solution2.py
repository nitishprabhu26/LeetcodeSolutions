# Approach: Neetcode
# https://youtu.be/qYlHrAKJfyA


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        curr = ""
        
        for c in path + "/":
            if c == "/":
                if curr == "..":
                    if stack: stack.pop()
                elif curr != "" and curr != ".":
                    stack.append(curr)
                curr = ""
            else:
                curr += c
        return "/" + "/".join(stack)


path = "/home/"
path = "/../"
path = "/home//foo/"
obj = Solution()
print(obj.simplifyPath(path))


# Complexity Analysis:
# Time complexity : O(N).
# Space complexity : O(N).