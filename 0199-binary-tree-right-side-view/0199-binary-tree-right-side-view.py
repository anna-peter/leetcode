from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # the right side view always displays the last value we would visit per level
        # starting at the root, for each level add nodes to the queue
        # we can create an array of all nodes per level, and then for each array, return the last value

        if not root:
            # base case, empty array
            return []
        
        queue = deque([root])
        all_levels = [] # this will be an array of arrays, containing nodes per level

        while queue:

            # build array of nodes at current level
            current_level = []
            # go through queue
            for _ in range(len(queue)):
                # pop leftmost value -> this is the current level
                current = queue.popleft()
                current_level.append(current.val)
                # print("current val "+str(current.val))
                # add its children to the queue, but dont explore yet (we need to finish this level via the queue first)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            # print("finished level with "+str(current_level))
            
            all_levels.append(current_level)
        
        # return the last element of each level
        return [level[-1] for level in all_levels]

# queue = [1]
# pop 1; current_level = [1]. queue = [2,3]. all_levels= [[1]]
# pop 2; current_level = []. len(queue)=1. current_level=[2]. queue = [3,5]

        