# Approach : Backtracking
# https://youtu.be/qs1-iEla-5M


class Solution(object):
    def combinationSum(self, candidates, target):
        self.res = []
        self.candidates = candidates
        self.backtrack([], target, 0)
        return self.res
    
    def backtrack(self, path, target, index):
        
        if target == 0:
            self.res.append(path)
            return
        
        if target < 0:
            return
        
        for x in range(index, len(self.candidates)):
            self.backtrack(path + [self.candidates[x]], target - self.candidates[x], x)

        
candidates = [2,3,6,7]
target = 7
obj = Solution()
print(obj.combinationSum(candidates, target))