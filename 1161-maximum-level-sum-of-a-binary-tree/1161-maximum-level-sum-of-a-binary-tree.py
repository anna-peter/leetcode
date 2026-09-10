# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # return the level with maximum sum. if two or more levels have maximum sum, return the lowest level
        # for each level, calculate the level sum first
        queue = deque([root])
        level_sums = [] # stores the sum for each level
        max_level = 1
        while queue:
            curr_level_sum = 0

            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                curr_level_sum += curr.val
            
            level_sums.append(curr_level_sum)
        return level_sums.index(max(level_sums))+1
        

        