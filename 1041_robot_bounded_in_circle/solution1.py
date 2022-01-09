# Approach: Neetcode
# https://youtu.be/nKv2LnC_g6E

# Algorithm:
# Initially facing North
# To check if a instruction vector creates a cycle or not:
# 1. change in position is 0
# OR
# 2. change in direction is present

# case 1 : change of position is 0. at the end of each cycle(instruction) [pointer comes back to origin].
# [cycle of 1 to reach back to origin by running the instructions once - GGLLGG]
# OR
# case 2 : if position change then, change in direction is needed at end of each cycle.
# [cycle of 2 to reach back to origin by running the instructions twice - GGLL]
# [cycle of 4 to reach back to origin by running the instructions 4 times - GGL]


# We could either run the instruction once, twice or 4 times and then see if the pointer is back at origin
# (by running 4 times)
# OR
# run simulation only once and see if 
# - position did not change - we have a cycle
# or
# - if position did change and direction also changed - we have a cycle.


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        # Facing North (up)
        dirX, dirY = 0, 1
        
        # our position
        x, y = 0, 0
        
        # iterate through instructions once
        for d in instructions:
            if d == "G":
                x, y = x + dirX, y + dirY
            # rotating 90 degrees: swap dirX and dirY
            elif d == "L":
                # rotating left(first): dirX, dirY = -1, 0
                # rotating left(second): dirX, dirY = 0, -1
                dirX, dirY = -1 * dirY, dirX
            else:
                # rotating right(first): dirX, dirY = 1, 0
                # rotating right(second): dirX, dirY = 0, -1
                dirX, dirY = dirY, -1 * dirX
               
        # after looping through the instructions once,
        # if the position did not change, or the direction has been changed atleast by 1.
        return (x, y) == (0, 0) or (dirX, dirY) != (0, 1)
                


instructions = "GGLLGG"
obj = Solution()
print(obj.isRobotBounded(instructions))


# Complexity Analysis:
# Time complexity: O(N) where N is a number of instructions to parse.
# Space complexity: O(1) because the array directions contains only 4 elements.