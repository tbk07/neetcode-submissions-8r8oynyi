# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        global_max_path_val = root.val

        def dfs(node):
            max_path_val = 0
            nonlocal global_max_path_val

            if not node:
                return max_path_val
            
            if node.left and node.right:
                val_curr = node.val + node.right.val + node.left.val
                max_path_val = max(val_curr, max_path_val)
            if node.left:
                    val_curr = node.val + node.left.val
                    max_path_val = max(val_curr, max_path_val)
            if node.right:
                    val_curr = node.val + node.right.val
                    max_path_val = max(val_curr, max_path_val)
            if not node.left and not node.right:
                max_path_val = max(node.val,max_path_val)



            dfs(node.left)
            dfs(node.right)
            global_max_path_val = max(global_max_path_val,max_path_val)
            return
                
            
        return global_max_path_val
                
                
