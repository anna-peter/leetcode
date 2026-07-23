from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        # we can calculate the level sum for each level in an array and return the last value
        # use bfs to traverse levels

        # base case
        if not root:
            return 0

        queue = deque([root])
        level_sums = []

        while queue:
            level_sum = 0
            for _ in range(len(queue)):
                current = queue.popleft()
                level_sum += current.val
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            
            level_sums.append(level_sum)
        return level_sums[-1]



        