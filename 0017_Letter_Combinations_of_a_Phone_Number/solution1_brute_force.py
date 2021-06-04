class Solution:
    def letterCombinations(self, digits: str) -> [str]:
        res = []
        if len(digits) < 1:
            return res

        key_value = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                     "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        if len(digits) == 1:
            return list(key_value[digits])

        for i in digits:
            res.append(list(key_value[i]))

        mid_array = res[0]
        for i in range(1, len(res)):
            result = []
            for j in mid_array:
                for k in res[i]:
                    result.append(j+k)
            mid_array = result
        return result


inp_str = "234"
obj = Solution()
print(obj.letterCombinations(inp_str))

# Complexiety Analysis:
# Time: O(N^3)
