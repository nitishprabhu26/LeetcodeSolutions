# Approach 1: Character by Character

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        n = len(word)
            
        match1, match2, match3 = True, True, True

        # case 1: All capital
        for i in range(n):
            if not word[i].isupper():
                match1 = False
                break
        if match1:
            return True

        # case 2: All not capital
        for i in range(n):
            if word[i].isupper():
                match2 = False
                break
        if match2:
            return True

        # case 3: All not capital except first
        if not word[0].isupper():
            match3 = False
        if match3:
            for i in range(1, n):
                if word[i].isupper():
                    match3 = False
        if match3:
            return True

        # if not matching
        return False

# OR
# shorter version

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        n = len(word)

        if len(word) == 1:
            return True

        # case 1: All capital
        if word[0].isupper() and word[1].isupper():
            for i in range(2, n):
                if not word[i].isupper():
                    return False
        # case 2 and case 3
        else:
            for i in range(1, n):
                if word[i].isupper():
                    return False

        # if pass one of the cases
        return True

word = "USA"
obj = Solution()
print(obj.detectCapitalUse(word))

# Complexity Analysis:
# Time complexity : O(N), where n is the length of the word. We only need to check each char at most constant 
# times.
# Space complexity : O(1). We only need constant spaces to store our variables.
