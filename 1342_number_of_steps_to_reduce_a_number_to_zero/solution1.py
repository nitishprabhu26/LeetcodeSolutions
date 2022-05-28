# Approach 1: Simulation

# Intuition:
# The most intuitive, and easiest, solution is to simply simulate the rules and count how many steps are carried 
# out in order to reach zero.

# Algorithm:
# The algorithm works by simulating each step of the rules; if the current number is even then divide it by 2. 
# Else if it's odd, subtract 1 from it. Each time we perform one of these actions, we increment the steps we've 
# taken by 1 so that we can return it at the end.


class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0 # We need to keep track of how many steps this takes.
        while num > 0: # Remember, we're taking steps until num is 0.
            if num % 2 == 0: # Modulus operator tells us num is *even*.
                num = num // 2 # So we divide num by 2.
            else: # Otherwise, num must be *odd*.
                num = num - 1 # So we subtract 1 from num.
            steps = steps + 1 # We *always* increment steps by 1.
        return steps # And at the end, the answer is in steps so we return it.


# OR (using binary operations)
# https://youtu.be/iVd7KWccHYQ


class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        
        while num > 0:
            if num & 1 != 1:
                num = num >> 1
            else:
                num -= 1
            count += 1
        
        return count



num = 14
obj = Solution()
print(obj.numberOfSteps(num))


# Complexity Analysis:
# Time complexity : O(log n).
# At each step, what we did depended on whether the remaining num was odd or even. If num was even, we halved 
# what was left. If it was odd, we only subtracted 1. However, by subtracting 1, we were making it even, and so 
# on the next step we were guaranteed to halve it.
# What this means is that in the worst case, we're halving it on every second step. We treat the 1/2 of the time 
# as a constant though, so in essence, we say that at each step, num is being halved.
# When something is halved at every step, it has a O(logn) time complexity.
# Space complexity : O(1).
# We only use a constant number of integer variables, and so the space complexity is O(1).