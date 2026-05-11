# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        arr =[]
        q = deque([root])
        while q:
            curr = q.popleft()
            if not curr:
                arr.append(-1)
                continue
            arr.append(curr.val)
            q.append(curr.left)
            q.append(curr.right)
        return arr 
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if str[0]  == -1:
            return None
        root = TreeNode(str[0])
        q = deque(root)

        i = 1
        while q:
            curr = q.popleft()
            if str[i] != -1:
                left = TreeNode(str[i])
                curr.left  = left 
                q.append(left)
            i+=1
            if str[i] != -1:
                right = TreeNode(str[i])
                curr.right  = right 
                q.append(right)
            i+=1
        return root


        
        

