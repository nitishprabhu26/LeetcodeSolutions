# Program to find LCM of two numbers:
# https://www.geeksforgeeks.org/program-to-find-lcm-of-two-numbers/
# LCM (Least Common Multiple) of two numbers is the smallest number which can be divided by both numbers. 
# Online calculator: http://www.alcula.com/calculators/math/lcm/


# Approach 1: Using GCD to find LCM
# An efficient solution is based on the below formula for LCM of two numbers ‘a’ and ‘b’. 
#    a x b = LCM(a, b) * GCD(a, b)
#    LCM(a, b) = (a x b) / GCD(a, b)
# Using GCD, we can find LCM. 


# Recursive function to return gcd of a and b
def gcd1(a,b):
    if a == 0:
        return b
    return gcd1(b % a, a)
 
# Function to return LCM of two numbers
def lcm1(a,b):
    return (a / gcd1(a,b))* b


num1 = 98
num2 = 56
print('LCM of', num1, 'and', num2, 'is', lcm1(num1, num2))


# Time Complexity: O(log(min(a,b))
# Auxiliary Space: O(log(min(a,b))

# ----------------------------------------------------------------------------------------------------------------

# Iterative function to return gcd of a and b
def gcd5(n1,n2):
    # find the min number amongst n1 and n2
    min_num = min(n1, n2)
    gcd = 1

    # loop from 1 to min_num and see if both n1 and n2 are divisible; if so then update gcd
    for i in range(1, min_num + 1):
        if n1 % i == 0 and n2 % i == 0:
            gcd = i
            
    return gcd

# Approach 2: Loop
# https://youtu.be/hSTZ4Pi51lI


# Iterative function to return lcm of a and b
def lcm2(a, b):
    # find the max number amongst a and b
    max_num = max(a, b)

    # iterate by incrementing max_num by 1, until both a and b divides max_num
    # break out of loop and return max_num as lcm
    while(True):
        if max_num % a == 0 and max_num % b == 0:
            break
        max_num += 1

    return max_num


num1 = 12
num2 = 78
print('LCM of', num1, 'and', num2, 'is', lcm2(num1, num2))


# Time Complexity : O(a * b).
# Auxiliary Space : O(1).

# ----------------------------------------------------------------------------------------------------------------