# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        path_to_q = []
        path_to_p = []
        node = root
        while node:  
            path_to_p.append(node)  
            if node == p:
                break
            if node.val > p.val:
                node = node.left
            elif node.val < p.val:
                node = node.right
        
        node = root        
        while node:  
            path_to_q.append(node)  
            if node == q:
                break
            if node.val > q.val:
                node = node.left
            elif node.val < q.val:
                node = node.right
        lca = root
        for n1, n2 in zip(path_to_p, path_to_q):
            if n1 == n2:
                lca = n1  
            else:
                break     

        return lca
        



                




        