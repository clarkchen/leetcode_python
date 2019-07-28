from unittest import TestCase
from .Solution import Solution

class TestSolution(TestCase):
    def test_romanToInt(self):
        s = Solution()
        self.assertEqual(s.romanToInt("VI"),6 )

        self.assertEqual(s.romanToInt("IV"),4 )

        self.assertEqual(s.romanToInt("VII"),7 )

        self.assertEqual(s.romanToInt("IX"), 9)

        self.assertEqual(s.romanToInt("MCMXCVI"),1996 )
