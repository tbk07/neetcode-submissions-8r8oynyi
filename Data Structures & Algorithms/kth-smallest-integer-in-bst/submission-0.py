# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = 0
        node = root
        stack = []
        while cnt == k and node.val not in stack:
            node = root
            if node.left:
                node = node.left 
            cnt += 1
            stack.append(node.val)
        return node.val
        