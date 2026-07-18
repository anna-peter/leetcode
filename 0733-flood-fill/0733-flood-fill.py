from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # empty array
        if image ==[[]]:
            return image
        # base case, starting pixel has target color
        if image[sr][sc]==color:
            return image
        
        # starting from source=image[sr][sc], explore all adjacent nodes, filling them with the color IF they have the same color as source
        # traverse in a BFS manner
        # children are [i-1][j] and [i][j-1] (don't consider diagonal, as that will be traversed after)
        # also keep track of already visited nodes, since there will be overlap -> set() traversed

        input_color = image[sr][sc]
        rows_len = len(image)
        cols_len = len(image[0])

        queue = deque([(sr,sc)])
        visited = set()
        while queue:
            for _ in range(len(queue)):
                i,j = queue.popleft()
                current_val = image[i][j]
                if current_val==input_color:
                    # adjacent value has the same color, paint it and add its children to the queue
                    image[i][j] = color

                    if i>0:
                        queue.append((i-1,j)) #top
                    if i<rows_len-1:
                        queue.append((i+1,j)) #bottom
                    if j>0:
                        queue.append((i,j-1)) #left
                    if j<cols_len-1:
                        queue.append((i,j+1)) #right
        return image
                    




        
