from unittest import TestCase
from .Solution import Solution,ListNode
class TestSolution(TestCase):
    def test_mergeTwoLists(self):
        s = Solution()
        l1 = ListNode(2)
        l2 = ListNode(1)
        l = s.mergeTwoLists(l1, l2)
        x = l
        while x!=None:
            print(x.val)
            x =  x.next
