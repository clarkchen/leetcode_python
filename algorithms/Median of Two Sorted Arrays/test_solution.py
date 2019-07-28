from unittest import TestCase
from .Solution import Solution

class TestSolution(TestCase):
    def test_findMedianSortedArrays1(self):
        s = Solution()
        l = [1,2,3,4]
        l2 = [5,6,7,8]
        res = s.findMedianSortedArrays(l,l2)
        print(res)
        self.assertTrue(res==4.5)

        l = [1, 2, 3, 4]
        l2 = [5, 6, 7, 8]
        res = s.findMedianSortedArrays(l2, l)
        self.assertTrue(res == 4.5)

    def test_findMedianSortedArrays2(self):
        s = Solution()
        l = [2,3,5,8,12,14]
        l2 = [7,9,11,15]
        res = s.findMedianSortedArrays(l,l2)
        print(res)
        self.assertTrue(res==8.5)

    def test_findMedianSortedArrays3(self):
        s = Solution()

        l = [1, 2, 3, 4]
        l2 = [5, 6, 7, 8, 9, 10]
        res = s.findMedianSortedArrays(l2, l)
        print(res)
        self.assertTrue(res == 5.5)

    def test_findMedianSortedArrays4(self):
        s = Solution()
        l =  [1, 2]
        l2 = [3, 4, 5, 6, 7, 8]
        res = s.findMedianSortedArrays(l2, l)
        print(res,  )
        self.assertTrue(res == 4.5)

    def test_findMedianSortedArrays5(self):
        s = Solution()

        l = [1, 3,4, 5]
        l2 = []
        res = s.findMedianSortedArrays(l2, l)
        print(res)
        self.assertTrue(res == 3.5)

    def test_findMedianSortedArrays6(self):
        s = Solution()

        l = [1, 2 ]
        l2 = [3,4]
        res = s.findMedianSortedArrays(l, l2)
        print(res)
        self.assertTrue(res == 2.5)

    def test_findMedianSortedArrays7(self):
        s = Solution()

        l = [1,]
        l2 = [2, 3]
        res = s.findMedianSortedArrays(l, l2)
        print(res)
        self.assertTrue(res == 2)

    def test_findMedianSortedArrays8(self):
        s = Solution()

        l = [1, 3]
        l2 = [2,]
        res = s.findMedianSortedArrays(l, l2)
        print(res)
        self.assertTrue(res == 2)

    def test_findMedianSortedArrays8(self):
        s = Solution()

        l = [1, 2]
        l2 = [3,4]
        res = s.findMedianSortedArrays(l, l2)
        print(res)
        self.assertTrue(res == 2.5)