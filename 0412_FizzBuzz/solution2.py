# Approach 2: String Concatenation
class Solution:
    def fizzBuzz(self, n: int) -> [str]:
        answer = []

        for i in range(1,n+1):
            divisible_by_3 = (i%3==0)
            divisible_by_5 = (i%5==0)

            num_ans_str = ""

            if divisible_by_3:
                num_ans_str += "Fizz"
            if divisible_by_5:
                num_ans_str += "Buzz"
            if not num_ans_str:
                num_ans_str += str(i)
            answer.append(num_ans_str)
                
        return answer

n = 15
obj = Solution()
print(obj.fizzBuzz(n))

# Complexity Analysis:
# Time Complexity: O(N)
# Space Complexity: O(1)

# What if FizzBuzz is now FizzBuzzJazz i.e.
# 3 ---> "Fizz" , 5 ---> "Buzz", 7 ---> "Jazz"
# If you try to solve this with the previous approach the program would have too many conditions to check:

# Divisible by 3
# Divisible by 5
# Divisible by 7
# Divisible by 3 and 5
# Divisible by 3 and 7
# Divisible by 7 and 3
# Divisible by 3 and 5 and 7
# Not divisible by 3 or 5 or 7.
# This way if the FizzBuzz mappings increase, the conditions would grow exponentially in your program.

# Algorithm
# Instead of checking for every combination of these conditions, check for divisibility by given numbers i.e. 3, 5 as 
# given in the problem. If the number is divisible, concatenate the corresponding string mapping Fizz or Buzz to the 
# current answer string.

# For eg. If we are checking for the number 15, the steps would be:
# Condition 1: 15 % 3 == 0 , num_ans_str = "Fizz"
# Condition 2: 15 % 5 == 0 , num_ans_str += "Buzz"
# => num_ans_str = "FizzBuzz"
# So for FizzBuzz we just check for two conditions instead of three conditions as in the first approach.