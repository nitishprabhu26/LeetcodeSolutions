# Approach: Neetcode
# https://youtu.be/ER_oLmdc-nw


from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r

        def canShip(cap):
            ships = 1
            curCap = cap

            for w in weights:
                if curCap - w < 0:
                    ships += 1
                    curCap = cap
                curCap -= w

            return ships <= days

        while l <= r:
            cap = (l + r) // 2
            if canShip(cap):
                res = min(res, cap)
                r = cap - 1
            else:
                l = cap + 1
        return res


weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
obj = Solution()
print(obj.shipWithinDays(weights, days))


# Complexity Analysis:
# Time complexity: O(n ⋅ log(m)). n is length of array and m is the sum of all elements in the array.
# Space complexity: O(1). We are only defining a few integer variables.