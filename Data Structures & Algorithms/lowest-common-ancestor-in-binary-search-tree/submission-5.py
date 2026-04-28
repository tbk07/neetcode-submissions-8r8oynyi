# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Helper to get the path to a specific node in a BST
        def get_path(target):
            path = []
            curr = root
            while curr:
                path.append(curr)
                if target.val < curr.val:
                    curr = curr.left
                elif target.val > curr.val:
                    curr = curr.right
                else:
                    break
            return path

        path_p = get_path(p)
        path_q = get_path(q)
        
        lca = root
        # Compare the paths until they diverge
        for n1, n2 in zip(path_p, path_q):
            if n1 == n2:
                lca = n1
            else:
                break
        
        return lca