# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def validate(node,minval,maxval):
            if not node:
                return True
            
            if not (minval < node.val < maxval):
                return False
            
            return validate(node.left,minval,node.val) and validate(node.right,node.val,maxval)
        return validate(root,float('-inf'),float('inf'))