class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        # u -> (x, y+1)
        # d -> (x, y-1)
        # l -> (x-1, y)
        # r -> (x+1, y)
        pos = [0,0]
        for move in moves:
            print(pos)
            if move=='U': 
                pos = [pos[0], pos[1]+1]
            elif move=='D':
                pos = [pos[0], pos[1]-1]
            elif move=='L':
                pos = [pos[0]-1, pos[1]]
            elif move=='R':
                pos = [pos[0]+1, pos[1]]
            else:
                print("unknown move ")
        
        return pos==[0,0]

        