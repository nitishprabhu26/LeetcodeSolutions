# Approach: Using Stacks
# https://leetcode.com/problems/simplify-path/solution/

# Algorithm:
# 1. Initialize a stack, S that we will be using for our implementation.
# 2. Split the input string using / as the delimiter. This step is really important because no matter what, the 
#    given input is a valid path and we simply have to shorten it. So, that means that whatever we have between 
#    two / characters is either a directory name or a special character and we have to process them accordingly.
# 3. Once we are done splitting the input path, we will process one component at a time.
# 4. If the current component is a . or an empty string, we will do nothing and simply continue. Well if you 
#    think about it, the split string array for the string /a//b would be [a,,b]. yes, that's an empty string in 
#    between a and b. Again, from the perspective of the overall path, it doesn't mean anything.
# 5. If we encounter a double-dot .., we have to do some processing. This simply means go one level up in the 
#    current directory path. So, we will pop an entry from our stack if it's not empty.
# 6. Finally, if the component we are processing right now is not one of the special characters, then we will 
#    simply add it to our stack because it's a legitimate directory name.
# 7. Once we are done processing all the components, we simply have to connect all the directory names in our 
#    stack together using / as the delimiter and we will have our shortest path that leads us to the same 
#    directory as the one provided as an input.


class Solution:
    def simplifyPath(self, path: str) -> str:
        # Initialize a stack
        stack = []
        
        # Split the input string on "/" as the delimiter
        # and process each portion one by one
        for portion in path.split("/"):

            # If the current component is a "..", then
            # we pop an entry from the stack if it's non-empty
            if portion == "..":
                if stack:
                    stack.pop()
            elif portion == "." or not portion:
                # A no-op for a "." or an empty string
                continue
            else:
                # Finally, a legitimate directory name, so we add it
                # to our stack
                stack.append(portion)

        # Stich together all the directory names together
        final_str = "/" + "/".join(stack)
        return final_str


path = "/home/"
path = "/../"
path = "/home//foo/"
obj = Solution()
print(obj.simplifyPath(path))


# Complexity Analysis:
# Time complexity : O(N) if there are N characters in the original path. First, we spend O(N) trying to split 
# the input path into components and then we process each component one by one which is again an O(N) operation.
# Space complexity : O(N). Actually, it's 2N because we have the array that contains the split components and 
# then we have the stack.


# OR

# class Solution(object):
#     def simplifyPath(self, path):
#         places = [p for p in path.split("/") if p!="." and p!=""]
#         stack = []
#         for p in places:
#             if p == "..":
#                 if len(stack) > 0:
#                     stack.pop()
#             else:
#                 stack.append(p)
#         return "/" + "/".join(stack)