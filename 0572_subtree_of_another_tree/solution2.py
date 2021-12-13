# converting into strings

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def convert(p):
            return "^" + str(p.val) + "#" + convert(p.left) + convert(p.right) if p else "$"

        # print(convert(root))
        # print(convert(subRoot))
        # ^3#^4#^1#$$^2#$$^5#$$
        # ^4#^1#$$^2#$$
        return convert(subRoot) in convert(root)

root = [3,4,5,1,2]
subRoot = [4,1,2]

obj = Solution()
print(obj.isSubtree(root, subRoot))