# Approach 2: Two Pointer Approach
# OR
# Neetcode: https://youtu.be/UuiTKBwPgAo

# Algorithm:
# We take two pointers, one at the beginning and one at the end of the array constituting the length of the 
# lines. Futher, we maintain a variable maxarea to store the maximum area obtained till now. At every step, 
# we find out the area formed between them, update maxarea and move the pointer pointing to the shorter line 
# towards the other end by one step.


class Solution:
    def maxArea(self, height) -> int:
        max_area = 0
        i = 0
        j = len(height)-1
        while i < j:
            max_area = max(max_area, (j-i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area


height = [4, 3, 2, 1, 4]
obj = Solution()
print(obj.maxArea(height))


# Complexity Analysis:
# Time complexity : O(n). Single pass.
# Space complexity : O(1). Constant space is used.
