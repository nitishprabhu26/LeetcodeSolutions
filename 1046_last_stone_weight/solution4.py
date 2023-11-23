# Approach 4: Bucket Sort
# https://leetcode.com/problems/last-stone-weight/editorial/

# Intuition:
# Let W be the maximum stone weight in the input array. We can create a bucket array of size W + 1, where 
# each index of the bucket array represents a stone weight. Then, we can bucket "sort" the stones in O(N) time 
# by iterating over them and incrementing the relevant bucket array index by 1.


from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # Set up the bucket array.
        max_weight = max(stones)
        buckets = [0] * (max_weight + 1)

        # Bucket sort.
        for weight in stones:
            buckets[weight] += 1

        # Scan through the weights.
        biggest_weight = 0 
        current_weight = max_weight
        while current_weight > 0:
            if buckets[current_weight] == 0:
                current_weight -= 1
            elif biggest_weight == 0:
                buckets[current_weight] %= 2
                if buckets[current_weight] == 1:
                    biggest_weight = current_weight
                current_weight -= 1
            else:
                buckets[current_weight] -= 1
                if biggest_weight - current_weight <= current_weight:
                    buckets[biggest_weight - current_weight] += 1
                    biggest_weight = 0
                else:
                    biggest_weight -= current_weight
        return biggest_weight


stones = [2,7,4,1,8,1]
# stones = [2,2]
obj = Solution()
print(obj.lastStoneWeight(stones))


# Complexity Analysis:
# Time complexity : O(N + W).
# Putting the N stones of the input array into the bucket array is O(N), because inserting each stone is an 
# O(1) operation.
# In the worst case, the main loop iterates through all of the W indexes of the bucket array. Processing 
# each bucket is an O(1) operation. This, therefore, is O(W).
# Seeing as we don't know which is larger out of N and W, we get a total of O(N + W).
# Space complexity : O(W).
# We allocated a new array of size W.