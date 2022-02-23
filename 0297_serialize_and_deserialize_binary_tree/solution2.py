# Neetcode: https://youtu.be/u4JAi2JJhI8

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        res = []
        
        def dfs(node):
            if not node:
                res.append('N')
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ",".join(res)
        

    def deserialize(self, data):
        vals = data.split(',')
        self.i = 0
        
        def dfs():
            if vals[self.i] == 'N':
                self.i += 1
                return None
                
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()
        
# OR
# for deserialize, changed i to global variable

# class Codec:
#     def deserialize(self, data):
#         vals = data.split(',')
#         i = 0
        
#         def dfs():
#             nonlocal i
#             if vals[i] == 'N':
#                 i += 1
#                 return None
                
#             node = TreeNode(int(vals[i]))
#             i += 1
#             node.left = dfs()
#             node.right = dfs()
#             return node

#         return dfs()


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
