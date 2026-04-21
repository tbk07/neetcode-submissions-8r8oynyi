# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
        prevNode, currNode = None, slow
        while currNode:
            currNode.next,prevNode,currNode = prevNode,currNode,currNode.next
        
        first, second = head, prevNode
        while second.next:  
            first.next, first = second, first.next
            second.next, second = first, second.next

                
        
