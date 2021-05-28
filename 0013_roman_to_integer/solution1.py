# used an array to store te mapped value of string and do calculation on the array
class Solution:
    def romanToInt(self, s: str) -> int:
        sym_value={'I': 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        value_arr=[]
        for i,x in enumerate(s):
            value_arr.append(sym_value.get(s[i]))
        
        i = 0
        while i < len(value_arr)-1:
            if value_arr[i]<value_arr[i+1]:
                value_arr[i] = value_arr[i+1]-value_arr[i]
                value_arr[i+1]=0
                i+=1
            i+=1
        return sum(value_arr)

s = "MCMXCIV"
obj = Solution()
print(obj.romanToInt(s))


# Complexity analysis:
# Time complexity : O(n).
# Space complexity : O(n).