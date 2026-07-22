from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # maintain a queue of node, and current sum
        # check if node has no children (is a leaf) AND current sum is targetSum

        # base condition
        if not root:
            return False
        
        # start at the top with root's value
        queue = deque([(root, root.val)])
        while queue: 
            current_node, current_sum = queue.pop()

            # we're at a leaf and have summed up to the targetr
            if (not current_node.left) and (not current_node.right) and current_sum==targetSum:
                return True
            
            # add the children to the queue, subtract the current node's value from the current sum
            # but only if they exist. any children that dont exist, we dont care\
            # if both children didn't exist and sum doesn't match, we've reached an "invalid" leaf, just continue
            if current_node.left:
                queue.append((current_node.left, current_sum+current_node.left.val))
            if current_node.right:
                queue.append((current_node.right, current_sum+current_node.right.val))
        
        # failed to find a valid path
        return False

        