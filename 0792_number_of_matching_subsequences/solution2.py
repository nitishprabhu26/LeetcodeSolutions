# Approach : Using 2 pointers as used in problem 392 [Time Limit Exceeded]


from typing import List

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def isSubsequence(s, t) -> bool:
            LEFT_BOUND, RIGHT_BOUND = len(s), len(t)

            p_left = p_right = 0
            while p_left < LEFT_BOUND and p_right < RIGHT_BOUND:
                # move both pointers or just the right pointer
                if s[p_left] == t[p_right]:
                    p_left += 1
                p_right += 1

            return p_left == LEFT_BOUND

        return sum(isSubsequence(word, s) for word in words)


s = "abcde"
words = ["a","bb","acd","ace"]
obj = Solution()
print(obj.numMatchingSubseq(s, words))