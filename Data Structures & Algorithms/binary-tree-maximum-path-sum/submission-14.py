# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path_val = root.val

        def dfs(node):
            nonlocal max_path_val

            if not node:
                return max_path_val
            
            if node.left and node.right:
                val_curr = node.val + node.right.val + node.left.val
                max_path_val = max(val_curr, max_path_val)
            if node.left:
                    val_curr = max_path_val + node.val + node.left.val
                    max_path_val = max(val_curr, max_path_val)
            if node.right:
                    val_curr = max_path_val + node.val + node.right.val
                    max_path_val = max(val_curr, max_path_val)
            if not node.left and not node.right:
                max_path_val = max(node.val,max_path_val)


            dfs(node.left)
            dfs(node.right)
            return max(node.val,max_path_val)
                
            
        return dfs(root)
                
                
