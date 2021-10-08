class Solution:
    def intToRoman(self, num: int) -> str:
        hashmap = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC",
                   100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"}
        ans = ""
        divsr_list = sorted(hashmap.keys(), reverse=True)
        for divsr in divsr_list:
            q = num//divsr
            r = num % divsr

            if q == 0:
                pass
            else:
                ans += hashmap[divsr]*q
                num = r
        return ans


num = 34
obj = Solution()
print(obj.intToRoman(num))
