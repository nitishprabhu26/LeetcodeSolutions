# Approach 1: One Pass
# https://leetcode.com/problems/robot-bounded-in-circle/solution/

# Intuition:
# This solution is based on two facts about the limit cycle trajectory.
# - After at most 4 cycles, the limit cycle trajectory returns to the initial point x = 0, y = 0. 
# - We do not need to run 4 cycles to identify the limit cycle trajectory. One cycle is enough. There could be 
#   two situations here.
#     - First, if the robot returns to the initial point after one cycle, that's the limit cycle trajectory.
#     - Second, if the robot doesn't face north at the end of the first cycle, that's limit cycle trajectory.


# Algorithm:

# - Let's use numbers from 0 to 3 to mark the directions: north = 0, east = 1, south = 2, west = 3. 
#   In the array directions we could store corresponding coordinates changes, i.e. directions[0] is to go north, 
#   directions[1] is to go east, directions[2] is to go south, and directions[3] is to go west.
# - The initial robot position is in the center x = y = 0, facing north idx = 0.
# - Now everything is ready to iterate over the instructions:
#   - If the current instruction is R, i.e. to turn on the right, the next direction is idx = (idx + 1) % 4. 
#       Modulo here is needed to deal with the situation - facing west, idx = 3, turn to the right to face 
#       north, idx = 0.
#   - If the current instruction is L, i.e. to turn on the left, the next direction could written in a 
#       symmetric way idx = (idx - 1) % 4. That means we have to deal with negative indices. A more simple way 
#       is to notice that 1 turn to the left = 3 turns to the right: idx = (idx + 3) % 4.
#   - If the current instruction is to move, we simply update the coordinates: 
#       x += directions[idx][0], y += directions[idx][1].
# - After one cycle we have everything to decide. It's a limit cycle trajectory if the robot is back to the 
#   center: x = y = 0 or if the robot doesn't face north: idx != 0.



class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # north = 0, east = 1, south = 2, west = 3
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        # Initial position is in the center
        x = y = 0
        # facing north
        idx = 0
        
        for i in instructions:
            if i == "L":
                idx = (idx + 3) % 4
            elif i == "R":
                idx = (idx + 1) % 4
            else:
                x += directions[idx][0]
                y += directions[idx][1]
        
        # after one cycle:
        # robot returns into initial position
        # or robot doesn't face north
        return (x == 0 and y == 0) or idx != 0
                


instructions = "GGLLGG"
obj = Solution()
print(obj.isRobotBounded(instructions))


# Complexity Analysis:
# Time complexity: O(N) where N is a number of instructions to parse.
# Space complexity: O(1) because the array directions contains only 4 elements.