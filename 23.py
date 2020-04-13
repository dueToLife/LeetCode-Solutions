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
        k = len(lists)
        head = None
        cur = None
        cnt = k
        while cnt > 0:
            minv = 0x3f3f3f
            cnt = k
            for i in range(k):
                if lists[i] == None:
                    cnt -= 1
                    continue
                elif lists[i].val < minv:
                    print(lists[i].val,end='')
                    minv = lists[i].val
                    lists[i] = lists[i].next
            node = ListNode(minv)
            if head == None:
                head = node
                cur = head
            else:
                cur.next = node
                cur = cur.next
        return head

s = Solution()
print(s.mergeKLists())