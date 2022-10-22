# Approach: Using count method


class Solution:
    def customSortString(self, S: str, T: str) -> str:
        ans = []
        
        # all the elements of T that occur in S, in order of S
        for i in S:
            ans.append( i * T.count(i))
            
        # write any elements of T we didn't write before (in any order)
        for i in T:
            if i not in S:
                ans.append(i)
                
        return ''.join(ans)


S = "cba"
T = "abcd"
obj = Solution()
print(obj.customSortString(S, T))


# Complexity Analysis:
# Time Complexity: O(S + (T * S)).
# Space Complexity: O(1). No extra space used.