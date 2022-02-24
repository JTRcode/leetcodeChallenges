class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        position = [0,0]
        direction = [0,1]
        for _ in range(4):
            for c in instructions:
                # print(direction)
                if c == "L":
                    temp = direction[0] 
                    direction[0] = direction[0] + 1 if (sum(direction) == -1) else direction[0] - 1
                    direction[1] = temp
                elif c == "R":
                    temp = direction[1] 
                    direction[1] = direction[1] + 1 if (sum(direction) == -1) else direction[1] - 1
                    direction[0] = temp
                elif c == "G":
                    position[0] += direction[0]
                    position[1] += direction[1]
                else:
                    pass
                # print(position)
            # print(position)
            if position[0] == 0 == position[1]:
                return True
        return False
    #                 0 1
    #           -1 0       1 0
    #                 0 -1