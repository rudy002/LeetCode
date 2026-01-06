# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        

        prev= None
        curr = head

        while curr:

            nxt = curr.next
            
            curr.next = prev # la j'inverse le pointeur
           
            prev = curr #j'avance le prev de 1 en avant 

            curr = nxt # et le suivant de 1 aussi 
           

        return prev