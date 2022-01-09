class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        moves = [0,0,0,0] # n e s w
        direction = 0
        
        for _ in range(4):
            for i in instructions:
                if i == "G": # GO
                    moves[direction%4] += 1
                elif i == "R":
                    direction += 1
                elif i == "L":
                    direction -= 1
        # iterate four times
        
        #north==south    east==west
        if moves[0] == moves[2] and moves[1] == moves[3]:
            return True
        else:
            return False

    
    
    
    
    def _isRobotBounded(self, instructions: str) -> bool:
        
        visited = set()
        
        
        position = (0,0)
        current = "N"
        
        leftward = {"N":"W", "W":"S", "S":"E", "E":"N"}
        rightward = {"N":"E", "E":"S", "S":"W", "W":"N"}
        # (x,y)
        moves = {"N":(0,1), "E":(1,0), "S": (0,-1), "W":(-1,0)}
        
        for inst in instructions:
            if inst == "L":
                print(f"Turn left from {current}",end=" ") 
                current = leftward[current]
                print(f"to {current}")

            elif inst == "R":
                print(f"Turn right from {current}",end=" ") 
                current = rightward[current]
                print(f"to {current}")


            else: # "G"
                position = (position[0] + moves[current][0], 
                            position[1] + moves[current][1])
                visited.add(position)
                print(f"{position}")
        
"""
On an infinite plane, a robot initially stands at (0, 0) and faces north. The robot can receive one of three instructions:

"G": go straight 1 unit;
"L": turn 90 degrees to the left;
"R": turn 90 degrees to the right.
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

 

Example 1:

Input: instructions = "GGLLGG"
Output: true
Explanation: The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.
Example 2:

Input: instructions = "GG"
Output: false
Explanation: The robot moves north indefinitely.
Example 3:

Input: instructions = "GL"
Output: true
Explanation: The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...

"""
