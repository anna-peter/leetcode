# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # max depth at node n = max(left, right)
        # if node is null, return current sum
        # as we move down a level, increase the length
        return self.maxDepthRec(root,0)
    
    def maxDepthRec(self,node,sum)-> int:
        if node is None:
            return sum
        left = node.left
        right = node.right
        sum +=1
        return max(self.maxDepthRec(left, sum), self.maxDepthRec(right,sum))
        