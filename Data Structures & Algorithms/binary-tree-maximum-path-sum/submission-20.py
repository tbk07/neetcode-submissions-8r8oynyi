# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')
        
        def dfs(node):
            if not node: return 0
            
            # 1. Get best branches, ignoring negatives
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            
            # 2. Update global record with the "turning point" path
            self.max_sum = max(self.max_sum, node.val + left + right)
            
            # 3. Return only the single best path upward
            return node.val + max(left, right)

        dfs(root)
        return self.max_sum