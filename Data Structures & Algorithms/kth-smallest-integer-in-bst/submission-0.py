# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = k
        result = root.val


        def helper(node):
            nonlocal count, result
            if count == 0:
                return
            if node == None:
                return

            helper(node.left) # first left, then itself, then right
            count -= 1 # counting down as we go inorder
            if count == 0: # we found the kth smallest
                result = node.val
            helper(node.right)

            return

        helper(root)
        return result