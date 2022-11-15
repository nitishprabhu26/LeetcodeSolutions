# Program to Find GCD or HCF of Two Numbers:
# https://www.geeksforgeeks.org/program-to-find-gcd-or-hcf-of-two-numbers/
# GCD (Greatest Common Divisor) or HCF (Highest Common Factor) of two numbers is the largest number that divides 
# both of them. 
# Online calculator: http://www.alcula.com/calculators/math/gcd/#gsc.tab=0


# Approach 1: For finding the GCD of two numbers we will first find the minimum of the two numbers and then find 
# the highest common factor of that minimum which is also the factor of the other number.

def gcd1(a, b):
    # Find minimum of a and b
    result = min(a, b)
  
    while result:
        if a % result == 0 and b % result == 0:
            break
        result -= 1
  
    # Return the gcd of a and b
    return result


num1 = 98
num2 = 56
print(f"Approach 1: GCD of {num1} and {num2} is {gcd1(num1, num2)}")


# Time Complexity : O(min(a,b)).
# Auxiliary Space : O(1) or constant.

# ----------------------------------------------------------------------------------------------------------------


# Approach 2: An efficient solution is to use Euclidean algorithm which is the main algorithm used for this 
# purpose. The idea is, GCD of two numbers doesn’t change if a smaller number is subtracted from a bigger number.

# Recursive function to return gcd of a and b
def gcd2(a, b):
  
    # Everything divides 0
    if (a == 0):
        return b
    if (b == 0):
        return a
  
    # base case
    if (a == b):
        return a
  
    # a is greater
    if (a > b):
        return gcd2(a-b, b)
    return gcd2(a, b-a)


num1 = 98
num2 = 56
print(f"Approach 2: GCD of {num1} and {num2} is {gcd2(num1, num2)}")


# Time Complexity : O(min(a,b)).
# Auxiliary Space : O(min(a,b)).

# ----------------------------------------------------------------------------------------------------------------


# Approach 3: Instead of Euclidean algorithm by subtraction, a better approach is present. We don’t perform 
# subtraction here. we continuously divide the bigger number by the smaller number.

# Recursive function to return gcd of a and b
def gcd3(a,b):
      
    # Everything divides 0 
    if (b == 0):
         return a
    return gcd3(b, a%b)


num1 = 98
num2 = 56
print(f"Approach 3: GCD of {num1} and {num2} is {gcd3(num1, num2)}")


# Time Complexity : O(log(min(a,b)).
# Auxiliary Space : O(log(min(a,b)).

# ----------------------------------------------------------------------------------------------------------------


# Approach 4: GCD and LCM | Python Program (same as approach 3)
# https://youtu.be/R4wK8wSNLF8 (divisor and dividend wrongly assigned; if n1 % n2, then always n1 is dividend)

# Given 2 numbers, num1 and num2. Take num2 as divisor and num1 and dividend.
# If remainder is 0, stop the operation. Then return divisor as answer (GCD)
# Or, If remainder is not 0, then set num2 = remainder and num1 = num2, and continue.
# [Works even if order of a and b are different (i.e. num1 = 48, num2 = 36 or num1 = 36, num2 = 48)]
# if num1 = 36, num2 = 48, then in the next iteration order of num1 and num2 will get exchanged
# i.e. num1 will be 48, num2 will be 36

# Iterative function to return gcd of a and b
def gcd4(n1,n2):
    # n1 is dividend and n2 is divisor
    while n1 % n2 != 0:
        rem = n1 % n2
        n1 = n2
        n2 = rem

    return n2


num1 = 48
num2 = 36
print(f"Approach 4: GCD of {num1} and {num2} is {gcd4(num1, num2)}")


# Time Complexity : O(log(min(a,b)).
# Auxiliary Space : O(1).

# ----------------------------------------------------------------------------------------------------------------


# Approach 5: HCF/GCD of Two numbers Using Python (similar to approach 1 but this is less efficient)
# https://youtu.be/DePWIOK1STg


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


num1 = 48
num2 = 36
print(f"Approach 5: GCD of {num1} and {num2} is {gcd5(num1, num2)}")


# Time Complexity : O(min(a,b).
# Auxiliary Space : O(1).

# ----------------------------------------------------------------------------------------------------------------

# GCD of more than two (or array) numbers:
# https://www.geeksforgeeks.org/gcd-two-array-numbers/