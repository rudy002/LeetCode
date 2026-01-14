# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        if not head or not head.next:
            return True
        
        arr = []
        val = ""
        curr = head

        while curr:
            val += str(curr.val)
            curr = curr.next
        
        print(val)
        if val == val[::-1]:
            return True
        else:
            return False 