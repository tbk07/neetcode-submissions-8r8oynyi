# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val : i for i,val in enumerate(inorder)}
        preorder_index = 0
        def helper(left,right):
            nonlocal preorder_index
            if left > right:
                return None
            root_node = preorder[preorder_index]
            root = TreeNode(root_node)
            preorder_index += 1
            inorder_index = inorder_map[root_node]
            root.left = helper(left, inorder_index - 1)
            root.right = helper(inorder_index + 1, right )

            return root

        return helper(0, len(inorder) - 1)

            

    
