from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        traversed = []
        while queue:
            # initialize empty array for this level, go through all children
            current_level = []
            for _ in range(len(queue)):
                current = queue.popleft()
                if current:
                    current_level.append(current.val)
                else:
                    continue
                if current.left:
                    queue.append(current.left)

                if current.right:
                    queue.append(current.right)
            traversed.append(current_level)
        return traversed




        