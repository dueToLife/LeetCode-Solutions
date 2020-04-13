# # Definition for singly-linked list.
# # class ListNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None

# class Solution(object):
#     def mergeKLists(self, lists):
#         """
#         :type lists: List[ListNode]
#         :rtype: ListNode
#         """
#         k = len(lists)
#         head = cur = ListNode(0)
#         while True:
#             minv = 0x3f3f3f
#             mini = 0
#             cnt = k
#             for i in range(k):
#                 if lists[i] == None:
#                     cnt -= 1
#                     continue
#                 elif lists[i].val < minv:
#                     minv = lists[i].val
#                     mini = i
#             if cnt == 0:
#                 break
#             lists[mini] = lists[mini].next
#             cur.next = ListNode(minv)
#             cur = cur.next
#         return head.next
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval*2):
                lists[i] = self.merge2Lists(lists[i], lists[i+interval])
            interval *= 2
        return lists[0] if amount > 0 else lists

    def merge2Lists(self, la, lb):
        head = cur = ListNode(0)
        while la and lb:
            if la.val < lb.val:
                cur.next = la
                la = la.next
            else:
                cur.next = lb
                lb = lb.next
            cur = cur.next
        if la:
            cur.next = la
        else:
            cur.next = lb
        return head.next