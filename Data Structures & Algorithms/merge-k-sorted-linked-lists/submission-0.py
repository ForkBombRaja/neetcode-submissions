import heapq
from itertools import count
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        # hrap with smallest node in top
        heap = []
        # if there are ties put it here
        tie = count()  
        for node in lists:
            ''' slap each node into the heap
            '''
            if node:
                heapq.heappush(heap, (node.val, next(tie), node))
        # placeholder to build the final
        dummy = ListNode(0)
        # tail will expand from here
        tail = dummy
        while heap:
            '''  while hewp is there remove the smallest node attach to tail and advance it 
            if therres more inside that list add next to  the heap.'''
            nodeVal, uniqueNumber, node = heapq.heappop(heap)
            tail.next = node
            tail = tail.next
            if node.next:
                heapq.heappush(heap, (node.next.val, next(tie), node.next))

        return dummy.next        