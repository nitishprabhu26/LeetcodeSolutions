# First we get lists of letters and digits seperately.
# Then we append the bigger list first. In this problem, 
# I use flag to keep track of which one to append, this will make the code cleaner.

class Solution:
    def reformat(self, s: str) -> str:
        letters = [c for c in s if c.isalpha()]
        digits = [c for c in s if c.isdigit()]
        
        if (abs(len(letters)-len(digits)))>1: return ""
        
        result=[]
        flag= len(letters)>len(digits)
        while (letters or digits):
            result.append(letters.pop() if flag else digits.pop())
            flag = not flag
        return ''.join(result)

num1 = "qpwn55656xxx1"
obj = Solution()
print(obj.reformat(num1))