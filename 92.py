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
            print(cur.val)
            if cnt >= left:
                cur.next = pre
            if cnt == left:
                leftNode = cur
            pre = cur
            cur = nex
            nex = None if cur == None else cur.next
            cnt += 1
        if leftNode.next:
            leftNode.next.next = pre
        else: #head is changed
            head = pre
        leftNode.next = cur

        return head