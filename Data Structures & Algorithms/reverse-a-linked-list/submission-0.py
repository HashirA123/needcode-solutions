# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None:
            return head
        sentry = head
        prev = None

        while sentry and sentry.next:
                nxt = sentry.next
                sentry.next = prev
                prev = sentry
                sentry = nxt
        
        # last one should still need its next updated
        sentry.next = prev

        return sentry



