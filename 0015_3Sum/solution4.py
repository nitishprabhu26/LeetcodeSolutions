# Approach 3: "No-Sort"

# What if you cannot modify the input array, and you want to avoid copying it due to memory constraints?
# We can adapt the hashset approach above to work for an unsorted array. We can put a combination of three 
# values into a hashset to avoid duplicates. Values in a combination should be ordered (e.g. ascending). 
# Otherwise, we can have results with the same values in the different positions.

# Algorithm:
# The algorithm is similar to the hashset approach above. We just need to add few optimizations so that it works 
# efficiently for repeated values:
# 1. Use another hashset dups to skip duplicates in the outer loop.
#    -  Without this optimization, the submission will time out for the test case with 3,000 zeroes. This case 
#       is handled naturally when the array is sorted.
# 2. Instead of re-populating a hashset every time in the inner loop, we can use a hashmap and populate it once. 
#    Values in the hashmap will indicate whether we have encountered that element in the current iteration. When 
#    we process nums[j] in the inner loop, we set its hashmap value to i. This indicates that we can now use 
#    nums[j] as a complement for nums[i].
#    -  This is more like a trick to compensate for container overheads. The effect varies by language, e.g. for 
#       C++ it cuts the runtime in half. Without this trick the submission may time out.


from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res, dups = set(), set()
        seen = {}
        for i, val1 in enumerate(nums):
            if val1 not in dups:
                dups.add(val1)
                for j, val2 in enumerate(nums[i+1:]):
                    complement = -val1 - val2
                    if complement in seen and seen[complement] == i:
                        res.add(tuple(sorted((val1, val2, complement))))
                    seen[val2] = i
        return res


inp_nums = [-1,0,1,2,-1,-4]
obj = Solution()
print(obj.threeSum(inp_nums))


# Complexity Analysis:
# Time Complexity: O(n^2). We have outer and inner loops, each going through n elements.
# Space Complexity: O(n) for the hashset/hashmap.
# For the purpose of complexity analysis, we ignore the memory required for the output. However, in this 
# approach we also store output in the hashset for deduplication.