# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # incase one or both are emtpy, return the non-empty one
        if not list1 and not list2:
            return list1
        elif not list1:
            return list2
        elif not list2:
            return list1

        l1 = list1
        l2 = list2

        # head is the sentry node
        head = node = ListNode()

        while l1 and l2:

            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            
            node = node.next

        # add whichever list is stll remaining to the end

        node.next = l1 or l2
        
        return head.next

                


            
