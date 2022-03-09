# Approach 2: Iterations
# We could also convert the above recursion into iteration, with the help of stack. DFS would be better than BFS 
# here since it works faster except the worst case. In the worst case the path root->leaf with the given sum is 
# the last considered one and in this case DFS results in the same productivity as BFS.

# Idea is to visit each node with the DFS strategy, while updating the remaining sum to cumulate at each visit.

# So we start from a stack which contains the root node and the corresponding remaining sum which is 
# sum - root.val. Then we proceed to the iterations: pop the current node out of the stack and return True if the 
# remaining sum is 0 and we're on the leaf node. If the remaining sum is not zero or we're not on the leaf yet 
# then we push the child nodes and corresponding remaining sums into stack.


from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        targetSum -= root.val
        if not root.left and not root.right:  # if reach a leaf
            return targetSum == 0
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)


obj = Solution()
root = [5,4,8,11,None,13,4,7,2,None,None,None,1]
targetSum = 22
print(obj.hasPathSum(root, targetSum))


# Complexity Analysis:

# Time complexity : the same as the recursion approach O(N).
# Space complexity : O(N) since in the worst case, when the tree is completely unbalanced, e.g. each node has only 
# one child node, we would keep all N nodes in the stack. But in the best case (the tree is balanced), the height 
# of the tree would be log(N). Therefore, the space complexity in this case would be O(log(N)).