# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def reverseLists(ListNodes):
            head = pre = None
            now = ListNodes
            while now:
                pre = now
                now = now.next
                pre.next = head
                head = pre
            return head
        l1 = reverseLists(l1)
        l2 = reverseLists(l2)
        d = 0 
        cur = head = ListNode(0)
        while l1 and l2:
            sum = (l1.val + l2.val + d) % 10 
            d = (l1.val + l2.val + d) // 10
            cur.next = ListNode(sum)
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        if l1:
            cur.next = l1
            while l1 and d:
                d = (l1.val + d) // 10
                l1.val = (l1.val + 1) % 10
                l1 = l1.next 
                cur = cur.next    
        else:
            cur.next = l2
            while l2 and d:
                d = (l2.val + d) // 10
                l2.val = (l2.val + 1) % 10
                l2 = l2.next
                cur = cur.next
        if d:
            cur.next = ListNode(1)
        head = reverseLists(head.next)
        return head