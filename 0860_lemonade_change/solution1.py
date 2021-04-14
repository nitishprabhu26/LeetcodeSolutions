class Solution:
    def lemonadeChange(self, bills: [int]) -> bool:
        five,ten=0,0
        for bill in bills:
            if bill==5:
                five+=1
            elif bill==10:
                if not five: return False
                five-=1
                ten+=1
            else:
                if ten and five:
                    ten-=1
                    five-=1
                elif five>=3:
                    five-=3
                else:
                    return False   
        return True

bills = [5,5,5,10,20,5,10]
obj = Solution()
print(obj.lemonadeChange(bills))

# Complexity Analysis:
# Time Complexity: O(N), where N is the length of bills.
# Space Complexity: O(1).