# if we consider duplicate values in the list
# we get solution as [1,5,4,2,0,3]
# unlike before where we used to get [1,5,4,2,0,4] or [1,5,3,2,0,3] (same index for duplicate values)

# here we store key value pairs in dictionary where value is an array of indexes
from typing import List


class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        dict = {}
        output = []
        for i, x in enumerate(B):
            if x in dict:
                dict[x].append(i)
            else:
                dict[x] = [i]

        # print(dict)

        for i, x in enumerate(A):
            output.append(dict[x][-1])
            dict[x] = dict[x][:-1]

            # print(dict)
        return output


A = [12, 28, 46, 32, 50, 46]
B = [50, 12, 32, 46, 46, 28]
obj = Solution()
print(obj.anagramMappings(A, B))
