# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []
        self.traverse(root,result)
        return result
    def traverse(self,root,result):
        if root is not None:
            self.traverse(root.left,result)
            result.append(root.val)
            self.traverse(root.right,result)
        