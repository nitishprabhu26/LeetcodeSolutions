# Approach 1: Depth First Search (DFS)
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/solution/

# The serialization of a Binary Search Tree is essentially to encode its values and more importantly its structure.
# One can traverse the tree to accomplish the above task. And it is well know that we have two general strategies 
# to do so:

# Breadth First Search (BFS):
# We scan through the tree level by level, following the order of height, from top to bottom. The nodes on higher 
# level would be visited before the ones with lower levels.

# Depth First Search (DFS):
# In this strategy, we adopt the depth as the priority, so that one would start from a root and reach all the way 
# down to certain leaf, and then back to root to reach another branch.
# The DFS strategy can further be distinguished as preorder, inorder, and postorder depending on the relative order
# among the root node, left node and right node.

# We use preorder DFS strategy.
# The preorder DFS traverse follows recursively the order of
# root -> left subtree -> right subtree.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        def rserialize(root, string):
            # check base case
            if root is None:
                string += 'None,'
            else:
                string += str(root.val) + ','
                string = rserialize(root.left, string)
                string = rserialize(root.right, string)
            return string
        
        return rserialize(root, '')
        

    def deserialize(self, data):
        
        def rdeserialize(l):
            if l[0] == 'None':
                l.pop(0)
                return None
                
            root = TreeNode(l[0])
            l.pop(0)
            root.left = rdeserialize(l)
            root.right = rdeserialize(l)
            return root

        data_list = data.split(',')
        root = rdeserialize(data_list)
        return root
        
# OR

# same solution but playing with variables [for arrays, no need to define them as nonlocal]
# changes done for desweialize as well


# class Codec:
#     def serialize(self, root):
#         string = ''
#         def rserialize(root):
#             nonlocal string
#             # check base case
#             if root is None:
#                 string += 'None,'
#             else:
#                 string += str(root.val) + ','
#                 string = rserialize(root.left)
#                 string = rserialize(root.right)
#             return string
        
#         return rserialize(root)
        

#     def deserialize(self, data):
#         data_list = data.split(',')
        
#         def rdeserialize():
#             if data_list[0] == 'None':
#                 data_list.pop(0)
#                 return None
                
#             root = TreeNode(data_list[0])
#             data_list.pop(0)
#             root.left = rdeserialize()
#             root.right = rdeserialize()
#             return root

        
#         root = rdeserialize()
#         return root


# OR

# class Codec:
#     def serialize(self, root):
#         string = ''
#         def rserialize(root):
#             nonlocal string
#             # check base case
#             if root is None:
#                 string += 'None,'
#             else:
#                 string += str(root.val) + ','
#                 rserialize(root.left)
#                 rserialize(root.right)
        
#         rserialize(root)
#         return string

# OR
# using as an array

# class Codec:
#     def serialize(self, root):
#         string_array = []
#         def rserialize(root):
#             # check base case
#             if root is None:
#                 string_array.append('None')
#             else:
#                 string_array.append(str(root.val))
#                 rserialize(root.left)
#                 rserialize(root.right)
#             return string_array
        
#         rserialize(root)
#         return ','.join(string_array)

# OR
# no need of return as well

# class Codec:
#     def serialize(self, root):
#         string_array = []
#         def rserialize(root):
#             # check base case
#             if root is None:
#                 string_array.append('None')
#             else:
#                 string_array.append(str(root.val))
#                 rserialize(root.left)
#                 rserialize(root.right)
        
#         rserialize(root)
#         return ','.join(string_array)


root = [1,2,3,None,None,4,5]
ser = Codec()
deser = Codec()
ans = deser.deserialize(ser.serialize(root))
print(ans)


# Complexity Analysis
# Time Complexity: O(N). In both serialization and deserialization functions, we visit each node exactly once, 
# where N is the number of nodes, i.e. the size of tree.
# Space Complexity :  O(N). In both serialization and deserialization functions, we keep the entire tree, either 
# at the beginning or at the end, therefore, the space complexity is O(N).
