# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        # temporary node before head 
        dummy = ListNode(0)
        # next node after dummy i shead
        dummy.next = head
        # node before current block of k being processed
        prevGroupEnd = dummy

        while True:
            ''' every k nodes loop k times to flip
            then advance if k more exist
            '''
            groupEnd = prevGroupEnd
            for node in range(k):
                groupEnd = groupEnd.next
                if not groupEnd:
                    return dummy.next

            groupStart = prevGroupEnd.next
            nextGroupStart = groupEnd.next
            prev = nextGroupStart
            curr = groupStart
            while curr != nextGroupStart:
                following = curr.next
                curr.next = prev
                prev = curr
                curr = following
            prevGroupEnd.next = groupEnd
            prevGroupEnd = groupStart  