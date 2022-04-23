# Approach 1: Backtracking
# https://leetcode.com/problems/combination-sum/solution/ (check example)

# Intuition:
# Backtracking is a general algorithm for finding all (or some) solutions to some computational problems. The idea 
# is that it incrementally builds candidates to the solutions, and abandons a candidate ("backtrack") as soon as 
# it determines that this candidate cannot lead to a final solution.
# Specifically, to our problem, we could incrementally build the combination, and once we find the current 
# combination is not valid, we backtrack and try another option.

# Algorithm:
# As one can see, the above backtracking algorithm is unfolded as a DFS (Depth-First Search) tree traversal, which 
# is often implemented with recursion. Here we define a recursive function of backtrack(remain, comb, start), 
# which populates the combinations, starting from the current combination (comb), the remaining sum to fulfill 
# (remain) and the current cursor (start) to the list of candidates.
# 1.For the first base case of the recursive function, if the remain == 0, i.e. we fulfill the desired target sum, 
#   therefore we can add the current combination to the final list.
# 2.As another base case, if remain < 0, i.e. we exceed the target value, we will cease the exploration here.
# 3.Other than the above two base cases, we would then continue to explore the sublist of candidates as 
#   [start ... n]. For each of the candidate, we invoke the recursive function itself with updated parameters.
#   - Specifically, we add the current candidate into the combination.
#   - With the added candidate, we now have less sum to fulfill, i.e. remain - candidate.
#   - For the next exploration, still we start from the current cursor start.
#   - At the end of each exploration, we backtrack by popping out the candidate out of the combination.


class Solution(object):
    def combinationSum(self, candidates, target):
        results = []

        def backtrack(remain, comb, start):
            if remain == 0:
                # make a deep copy of the current combination
                results.append(list(comb))
                return
            elif remain < 0:
                # exceed the scope, stop exploration.
                return

            for i in range(start, len(candidates)):
                # add the number into the combination
                comb.append(candidates[i])
                # give the current number another chance, rather than moving on
                backtrack(remain - candidates[i], comb, i)
                # backtrack, remove the number from the combination
                comb.pop()

        backtrack(target, [], 0)

        return results


candidates = [2,3,6,7]
target = 7
obj = Solution()
print(obj.combinationSum(candidates, target))