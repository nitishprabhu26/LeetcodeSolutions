# Brute force approach:
# https://youtu.be/I8NNSCpDt3U
# OR
# https://youtu.be/DQW-R52pp-M

# Intuition:
# The substring must start with the first charecter. 
# Also the max length of substring could be len(input)//2. Because if the substring is any more than half of the 
# string, then appending it twice would surpass the length of the input string. 
# So to solve: identify each substring; for each substring check if appending multiple copies of the substring 
# together can create the given input string.


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        rep = ''
        length_s = len(s)
        
        for i in range(length_s // 2):
            rep += s[i]
            if length_s % len(rep) ==0:
                if rep * (length_s // len(rep)) == s:
                    return True
        return False

# OR
# https://youtu.be/DQW-R52pp-M

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        substring = ''
        length_s = len(s)
        
        for i in range(length_s // 2):
            substring = s[:i + 1]
            if length_s % len(substring) == 0:
                no_of_rep = length_s // len(substring)
                new_str = ''
                while no_of_rep > 0:
                    new_str += substring
                    no_of_rep -= 1
                if s == new_str:
                    return True
        return False


s = "abcabcabcabc"
obj = Solution()
print(obj.repeatedSubstringPattern(s))


# Complexity Analysis:
# Let n be the length of the input string 's'.
# Time Complexity: O(n^2).
# Space Complexity: O(n).