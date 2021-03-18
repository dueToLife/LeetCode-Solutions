# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        cnt = 1
        leftNode = None
        pre, cur, nex = None, head, head.next
        while cnt <= right:
            if cnt >= left:
                cur.next = pre
            if cnt == left:
                leftNone = cur
            pre = cur
            cur = nex
            nex = None if cur == None else cur.next
            cnt += 1
        pre.next = cur
        leftNode.next = pre
        return head