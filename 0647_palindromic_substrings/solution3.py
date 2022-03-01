# Neetcode: https://youtu.be/4RACzI5-du8


class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        
        for i in range(len(s)):

            # odd length palindrome, single character center
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

            # even length palindrome, consecutive characters center
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        
        return res


# OR condensing the above


class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        
        for i in range(len(s)):

            # odd length palindrome, single character center
            res += self.countPalindromes(s, i, i)

            # even length palindrome, consecutive characters center
            res += self.countPalindromes(s, i, i + 1)
        
        return res
    
    def countPalindromes(self, s, l, r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res



s = "abc"
s = "aaa"
obj = Solution()
print(obj.countSubstrings(s))


# Complexity Analysis:
# Time complexity: O(N^2) for input string of length N. 
# The total time taken in this approach is dictated by two variables:
# - The number of possible palindromic centers we process.
# - How much time we spend processing each center.
# The number of possible palindromic centers is 2N−1: there are N single character centers and N−1 consecutive 
# character pairs as centers.
# Each center can potentially expand to the length of the string, so time spent on each center is linear on 
# average. Thus total time spent is N⋅(2N−1) ≃ N^2.
# Space complexity : O(1). We don't need to allocate any extra space since we are repeatedly iterating on the 
# input string itself.
