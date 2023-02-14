# Approach : Neetcode
# https://youtu.be/wrIWye928JQ


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        range_length = high - low + 1
        count = range_length // 2
        
        # when range is even, (eg: l=3, h=6 ) or (eg: l=2, h=5 ); odd value count is range//2 always
        # but if range is odd, and low is also even (eg: l=2, h=6); then high is even
        # then odd value count is range//2 
        # but if range is odd, and low is also odd (eg: l=3, h=7); then high is also odd
        # therfore odd value count = (range // 2) + 1
        if range_length % 2 and low % 2:
            count += 1
            
        return count


low = 3
high = 7
obj = Solution()
print(obj.countOdds(low, high))


# Complexity Analysis:
# Time complexity : O(1).
# Space complexity : O(1).