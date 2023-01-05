# Approach 1: Counting
# OR
# https://youtu.be/iAQ4lJcKWcM


# Algorithm:
# 1. Iterate over the integers in the array tasks, and for each integer store the frequency in the map counts.
# 2. Initialize the answer variable res to 0.
# 3. Iterate over the frequencies in the map counts and for each count:
# -  If count is 1, then we should stop and return -1.
# -  Add count // 3 to the answer variable res, if count is divisible by 3.
# -  Otherwise, add count // 3 + 1 to res.
# 4. Return res.


from typing import List

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        counts = dict()
        
        # Store the frequencies in the map.
        for task in tasks:
            if task not in counts:
                counts[task] = 0
            counts[task] += 1
            
        res = 0
        # Iterate over the task's frequencies.
        for key, val in counts.items():
            
            # If the frequency is 1, it's not possible to complete tasks.
            if val == 1:
                return -1
            
            # Group all the task in triplets.
            elif val % 3 == 0:
                res += val // 3
                
            # If count % 3 = 1; (count // 3 - 1) groups of triplets and 2 pairs.
            # If count % 3 = 2; (count // 3) groups of triplets and 1 pair.
            else:
                res += (val//3) + 1
                
        return res


tasks = [2,2,3,3,2,4,4,4,4,4]
obj = Solution()
print(obj.minimumRounds(tasks))


# Complexity analysis:
# Here, N is the number integers in the given array.
# Time complexity : O(N). We iterate over the integer array to store the frequencies in the map, this will take 
# O(N) time, then we iterate over the map to find the minimum group needed for each integer, which again will cost 
# O(N). Therefore, the total time complexity is equal to O(N).
# Space complexity : O(N). We need the map to store the frequencies of the integers, hence the total space 
# complexity is equal to O(N).