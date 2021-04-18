class Solution:
    def partitionLabels(self, S: str) ->[int]:
        cuts = [i for i in range(len(S)+1) if set(S[:i]).isdisjoint(S[i:])]
        return [j - i for i, j in zip(cuts, cuts[1:])]
            
S = "ababcbacadefegdehijhklij"
obj = Solution()
print(obj.partitionLabels(S))