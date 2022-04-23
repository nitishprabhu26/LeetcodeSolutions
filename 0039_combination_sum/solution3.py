# Approach : Backtracking
# Neetcode: https://youtu.be/GBKI9VSKdGg


from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
    
        def dfs(i, cur, total):
            
            # base case for success
            if total == target:
                # since we use a single variable 'cur' for all combinations, we add a copy instead
                # res.append(list(cur))
                # OR
                res.append(cur.copy())
                return
            
            # base case - if not possible to find a combination
            if i >= len(candidates) or total > target:
                return

            # two decissions at every point (check video)
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            dfs(i + 1, cur, total)
            
        dfs(0, [], 0)
        return res

        
candidates = [2,3,6,7]
target = 7
obj = Solution()
print(obj.combinationSum(candidates, target))


# Complexity Analysis:
# Time Complexity: O(2^target)