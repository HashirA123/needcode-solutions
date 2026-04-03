# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def helper(node, ma, mi):
            if node == None:
                return True

            if node.val <= mi or node.val >= ma:
                return False
            
            # go left
            res = (helper(node.left, node.val, mi) and 
                    helper(node.right, ma, node.val))

            return res
        
        return helper(root, math.inf, -math.inf)