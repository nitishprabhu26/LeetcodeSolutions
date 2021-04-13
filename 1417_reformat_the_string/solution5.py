from itertools import zip_longest
class Solution:
    def reformat(self, s: str) -> str:
        d = [a for a in s if a.isdigit()]
        c = [a for a in s if a.isalpha()]
        if abs(len(c) - len(d)) > 1: return ''
        if len(d) > len(c): c, d = d, c
            
        return "".join(map(lambda x: x[0] + x[1], zip_longest(c, d, fillvalue='')))

num1 = "abcde13456"
obj = Solution()
print(obj.reformat(num1))


# Explanation:
# https://www.geeksforgeeks.org/python-itertools-zip_longest/

# 1) d and c are list of digits and non-digits respectively.

# 2) We return False if their (c and d) difference in length is greater than one

# 3) To see why to use zip_longest instead of zip see below example:
# 	zip([2, 1], ['a'])                        ---->  ((2, 'a'))
# 	zip_longest([2, 1], ['a'], fillvalue='')  ---->  ((2, 'a'), (1, ''))
# As you see zip acts based on the shortest iterable an zip_longest acts based on the longest iterable 
# which is the case e are looking for in this problem.

# 4) In the "return" line we concatenate them and if None is present we change it to '' to prevent exception