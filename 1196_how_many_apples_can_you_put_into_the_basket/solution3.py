# Approach 3: Bucket Sort

# Intuition:
# Notably, this question has the constraint that 1 ≤ arr[i].length ≤ 10^3, and taking advantage of this we can 
# improve the time complexity to O(n) using bucket sort. However, this approach should be used with caution. 
# It is safe to use here because the heaviest apple is guaranteed to weigh no more than 10^3, but this approach 
# would not perform well on a test case such as weight = [1, 2, 3, 10^9].

# Algorithm:
# - Create an array 'bucket' with the length of max(arr) + 1, where bucket[i] represents the number of apples with 
#   weight i.
# - Iterate through arr:
#   -   for each arr[i], increment bucket[arr[i]] by 1;
# - initialize two integer variables: apples to count the number of apples we have put in the basket and units to 
#   record the current weight of the basket.
# - Iterate through bucket:
#   -   to make sure it will not exceed 5000 units of weight, the number of apples we take is take 
#       = min{bucket[i], (5000-units)/i};
#   -   increment units by take * i;
#   -   increment apples by take;


from typing import List

class Solution:
    def maxNumberOfApples(self, weights: List[int]) -> int:
        # initialize the bucket to store all elements
        size = max(weights) + 1
        bucket = [0] * size
        for weight in weights:
            bucket[weight] += 1

        apples = units = 0
        for i in range(size):
            # if we have apples of i units of weight
            if bucket[i] != 0:
                # we need to make sure that:
                # 1. we do not take more apples than those provided
                # 2. we do not exceed 5000 units of weight
                take = min(bucket[i], (5000 - units) // i)
                if take == 0:
                    break

                apples += take
                units += take * i
        return apples
        

weight = [900,950,800,1000,700,800]
obj = Solution()
print(obj.maxNumberOfApples(weight))


# Complexity Analysis:
# Time complexity : O(N + W), where N is the length of arr and W is the largest element in arr. This is because we 
# iterate through arr and bucket once and the lengths are N and W accordingly.
# Space complexity : O(W). This is because we initialize an array bucket with the size of max(arr).
