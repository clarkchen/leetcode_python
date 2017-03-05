# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None: return l2
        if l2 is None: return l1
        h1, h2 = t1 ,t2 = l1, l2

        head = None
        while h1!=None and h2!=None:

            if h1.val> h2.val:
                while t2.next!=None and h1.val>t2.next.val : t2 = t2.next
                if head is None: head = h2
                temp = t2.next
                t2.next = h1
                t2 = h1
                h1 = h1.next
                t2.next = temp


            elif h1.val<=h2.val:
                while t1.next!=None and h2.val>t1.next.val: t1=t1.next
                if head is None: head = h1
                temp = t1.next
                t1.next = h2
                t1 = h2
                h2 = h2.next
                t1.next = temp

        return head




