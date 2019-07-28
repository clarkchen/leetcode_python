"""
https://leetcode-cn.com/contest/weekly-contest-147/problems/stone-game-ii/

这道题目，递归+逆向思维+结果剪纸

递归比较好想，A选择完之后，B再进行选择，其实本质上是和A一样的问题，所以可以通过递归来解决

逆向思维是，如果要记录每一步的选择结果，其实代码结构会非常的复杂，但是要求得 A 能拿到多少石子，本质上是用总数减去B能拿到的最大石子数量即可


结果剪枝，直接构造一个 100维的1，简单测试了一下，发现非常的慢，然后在思考，其实m 和 current的每次结果返回应该是一致的，所以尝试用dict 的方式来做
但是也是通过List的模式来存储，提前做了一些简单例子证明的确一致，才开始剪枝


最终结果 1A


"""
from typing import List



class Solution:
    def get_max_stones(self, piles, M, current):
        if current >= len(piles):
            return 0
        if (M, current) in self.RESULT_MAP:
            return self.RESULT_MAP[(M, current)][0]
        res = []
        for x in range(1, 2 * M + 1):
            total = sum(piles[current:])
            other_take = self.get_max_stones(piles, max(M, x), current + x)
            res.append(total - other_take)

        # debug 这一步可以用来看结果
        l = self.RESULT_MAP.get((M, current), [])
        l.append(max(res))
        self.RESULT_MAP[(M, current)] = l
        return max(res)

    def stoneGameII(self, piles: List[int]) -> int:
        self.RESULT_MAP = {}
        return self.get_max_stones(piles, 1, 0)


if __name__ == '__main__':
    s = Solution()
    s.stoneGameII([])
    piles = [1]
    print(s.stoneGameII(piles))
    assert s.stoneGameII(piles) == 1

    piles = [2, 7, 9, 4, 4]
    print(s.stoneGameII(piles))
    assert s.stoneGameII(piles) == 10

    piles = [2, 7, 100, 4, 4]
    print(s.stoneGameII(piles))
    assert s.stoneGameII(piles) == 10

    piles = [2, 7, 100, 100, 4]
    print(s.stoneGameII(piles))
    assert s.stoneGameII(piles) == 106
    # print(s.RESULT_MAP)
    #
    piles = [1] * 100
    print(s.stoneGameII(piles))
    assert s.stoneGameII(piles) == 50
