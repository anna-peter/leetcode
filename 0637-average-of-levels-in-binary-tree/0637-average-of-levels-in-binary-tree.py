from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        averages = []
        queue = deque([root])

        while queue:
            current_length = len(queue)
            current_sum = 0
            # print(f"current sum {current_sum}")
            for _ in range(current_length):

                current = queue.popleft()
                current_sum += current.val
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
                
            
            current_average = current_sum / current_length
            averages.append(current_average)
        
        return averages

    
    # queue = [3] len = 1 
    # queue = [3,9,20]
    # [3,9,20,15,7]
    # pop 3, add 3 to sum 
    # pop 9, add 9 to sum, pop 20, add 20 to sum



        