'''
https://leetcode-cn.com/contest/weekly-contest-147/problems/n-th-tribonacci-number/

类似斐波那契数列

'''


class Solution:
    def yield_tool(self, n):
        a, b, c = 0, 1, 1
        while n > 1:
            yield c
            a, b, c = b, c, a + b + c
            n -= 1

    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1

        l = [x for x in self.yield_tool(n)]
        return l[-1]


if __name__ == '__main__':
    print(Solution().tribonacci(25))
    print(Solution().tribonacci(1))
    print(Solution().tribonacci(2))
    print(Solution().tribonacci(3))
    print(Solution().tribonacci(4))

    print(Solution().tribonacci(32))
