# Approach 1: Divide and Conquer with Greedy
# https://leetcode.com/problems/is-subsequence/solution/

# Let us start from the first characters of each string, i.e. source[0], target[0]. By comparing them, there could 
# be two cases as follows:
# Case 1): they are identical, i.e. source[0] == target[0]
# - In this case, the best strategy would be to cross out the first characters in both strings, and then continue 
#   with the matching job.
#   i.e. isSubsequence(source, target) = isSubsequence(source[1:], target[1:])
# Case 2): they are not identical, i.e. source[0] != target[0]
# - In this case, the only thing we can do is to skip (cross out) the first character in the target string, and 
#   keep on searching in the target string in the hope that we would find a letter that could match the first 
#   character in the source string.
#   i.e. isSubsequence(source, target) = isSubsequence(source, target[1:])

# In this problem, we have two particular base cases:
# - The source becomes empty, i.e. we found matches for all the letters in the source string. Hence, the source 
#   string is a subsequence of the target string.
# - The target becomes empty, i.e. we exhaust the target string, yet there are still some letters left unmatched 
#   in the source string. Hence, the source string is not a subsequence of the target string.

# Note, the below implementations happen to comply with a particular form of recursion, called tail recursion.


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        LEFT_BOUND, RIGHT_BOUND = len(s), len(t)

        def rec_isSubsequence(left_index, right_index):
            # base cases
            if left_index == LEFT_BOUND:
                return True
            if right_index == RIGHT_BOUND:
                return False
            # consume both strings or just the target string
            if s[left_index] == t[right_index]:
                left_index += 1
            right_index += 1

            return rec_isSubsequence(left_index, right_index)

        return rec_isSubsequence(0, 0)


s = "abc"
t = "ahbgdc"
obj = Solution()
print(obj.isSubsequence(s, t))


# Complexity Analysis:
# Let |S| be the length of the source string, and |T| be the length of the target string.
# Time complexity : O(∣T∣). i.e. O(n).
# - At each invocation of the rec_isSubsequence() function, we would consume one character from the target string 
#   and optionally one character from the source string.
# - The recursion ends when either of the strings becomes empty. In the worst case, we would have to scan the 
#   entire target string. As a result, the overall time complexity of the algorithm is \O(∣T∣).
# - Note, even when the source string is longer than the target string, the recursion would end anyway when we 
#   exhaust the target string. Hence, the number of recursions is not bounded by the length of the source string.
# Space complexity : O(∣T∣). i.e. O(n).
# - The recursion incurs some additional memory consumption in the function call stack. As we discussed previously,
#   in the worst case, the recursion would happen |T| times. Therefore, the overall space complexity is O(∣T∣).
# - With the optimization of tail recursion, this extra space overhead could be exempted, due to the fact that the 
#   call stack is reused for all consecutive recursions. However, Python and Java do not support tail recursion. 
#   Hence, this overhead cannot be waived.
# https://leetcode.com/explore/learn/card/recursion-i/256/complexity-analysis/2374/
