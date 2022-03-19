# Approach 2: Greedy - Solving with Stack
# https://leetcode.com/problems/remove-duplicate-letters/solution/
# OR
# https://youtu.be/nsnpeb_0Hfw

# Algorithm:
# We use idea number two from the intuition. We will keep a stack to store the solution we have built as we 
# iterate over the string, and we will delete characters off the stack whenever it is possible and it makes our 
# string smaller.
# Each iteration we add the current character to the solution if it hasn't already been used. We try to remove as 
# many characters as possible off the top of the stack, and then add the current character
# The conditions for deletion are:
# - The character is greater than the current characters
# - The character can be removed because it occurs later on
# At each stage in our iteration through the string, we greedily keep what's on the stack as small as possible.


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []

        # this lets us keep track of what's in our solution in O(1) time
        seen = set()

        # this will let us know if there are no more instances of s[i] left in s
        last_occurrence = {c: i for i, c in enumerate(s)}
        
        for i, c in enumerate(s):

            # we can only try to add c if it's not already in our solution
            # this is to maintain only one of each character
            if c not in seen:
                # if the last letter in our solution:
                #    1. exists
                #    2. is greater than c so removing it will make the string smaller
                #    3. it's not the last occurrence
                # we remove it from the solution to keep the solution optimal
                while stack and c < stack[-1] and i < last_occurrence[stack[-1]]:
                    seen.discard(stack.pop())
                seen.add(c)
                stack.append(c)
        return ''.join(stack)
        
# OR

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # contains max index number for each charecter
        lookup = {}
        for i in range(len(s)):
            lookup[s[i]] = i
            
        stack = []
        # keeps track if we have seen it already, i.e. if its in stack or not
        seen = set()

        for i in range(len(s)):
            if s[i] in seen:
                continue
            while stack and stack[-1] > s[i] and lookup[stack[-1]] > i:
                seen.remove(stack[-1])
                stack.pop()
            stack.append(s[i])
            seen.add(s[i])
            
        return ''.join(stack)

s = "bcabc"
s = "cbacdcbc"
s = "zcabc"
obj = Solution()
print(obj.removeDuplicateLetters(s))


# Complexity Analysis:
# Time complexity : O(N). Although there is a loop inside a loop, the time complexity is still O(N). This is 
# because the inner while loop is bounded by the total number of elements added to the stack (each time it fires 
# an element goes). This means that the total amount of time spent in the inner loop is bounded by O(N), giving 
# us a total time complexity of O(N)
# Space complexity : O(1). At first glance it looks like this is O(N), but that is not true! seen will only 
# contain unique elements, so it's bounded by the number of characters in the alphabet (a constant). You can only 
# add to stack if an element has not been seen, so stack also only consists of unique elements. This means that 
# both stack and seen are bounded by constant, giving us O(1) space complexity.

