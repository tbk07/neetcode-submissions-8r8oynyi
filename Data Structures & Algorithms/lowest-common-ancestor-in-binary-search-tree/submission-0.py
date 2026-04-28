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
        while node and node != p:
            if node.val > p.val:
                path_to_p.append(node)
                node = node.left
            elif node.val < p.val:
                path_to_p.append(node)
                node = node.right
        path_to_p.append(node)
        node = root        
        while node and node != q:
            if node.val > q.val:
                path_to_q.append(node)
                node = node.left
            elif node.val < q.val:
                path_to_q.append(node)
                node = node.right 
        path_to_q.append(node)
        lca = root
        for n1, n2 in zip(path_to_p, path_to_q):
            if n1 == n2:
                lca = n1  
            else:
                break     

        return lca
        



                




        