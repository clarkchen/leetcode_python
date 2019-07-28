from unittest import TestCase
from .Solution import Solution

class TestSolution(TestCase):
    def test_reverse(self):
        s = Solution()
        self.assertTrue(s.reverse(123123)== 321321)
        self.assertTrue(s.reverse(-123123)== -321321)
        self.assertTrue(s.reverse(-100)== -1)
        self.assertTrue(s.reverse(-100)==-1)
        self.assertTrue(s.reverse(1e33)==0)
        # self.assertTrue(s.reverse(-2147483412) == 0)
        self.assertTrue(s.reverse(1463847412) == 2147483641)