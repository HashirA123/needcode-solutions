# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # fast and slow

        fast = head
        slow = head

        while slow and slow.next:
            if fast and fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next

                if fast == slow:
                    return True
            else:
                return False

        return False