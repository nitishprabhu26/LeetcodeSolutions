# Approach 2: Using Binary Search
# https://youtu.be/xW4QsTtaCa4
# We can apply Binary Search to find the given number. We start with the mid number. We pass that number to the 
# guess function. If it returns a -1, it implies that the guessed number is larger than the required one. Thus, 
# we use Binary Search for numbers lower than itself. Similarly, if it returns a 1, we use Binary Search for 
# numbers higher than itself.


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n
        
        while low <= high:
            mid = low + (high - low) // 2
            res = guess(mid)
            
            if res > 0:
                low = mid + 1
            elif res < 0:
                high = mid - 1
            else:
                return mid


n = 10
pick = 6
obj = Solution()
print(obj.guessNumber(n))


# Complexity Analysis:
# Time complexity : O(log n). Binary Search is used.
# Space complexity : O(1). No extra space is used.