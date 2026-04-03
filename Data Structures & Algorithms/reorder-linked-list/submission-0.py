# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # fast and slow to get mid point first

        fast = head
        slow = head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        # slow now equals mid point of list
        mid = slow.next
        slow.next = None
        # now starting from mid, reverse the list
        prev = None

        while mid:
            temp = mid.next
            mid.next = prev
            prev = mid
            mid = temp
        # if everything went right, prev should now be point at the
        # last node in the list

        # now we do the swapping.
        start = head
        merger = prev

        while merger != None:
            tmp1, tmp2 = start.next, merger.next
            start.next = merger
            merger.next = tmp1
            start, merger = tmp1, tmp2

