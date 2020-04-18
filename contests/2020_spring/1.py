from typing import List


class Solution:
    def minCount(self, coins: List[int]) -> int:
        res = []
        for x in  coins:
            res.append(x//2+x%2)
        return sum(res)
if __name__ == '__main__':
    s = Solution()
    ans = s.minCount([4,2,1])
    print(ans)

    ans = s.minCount([2,3,10])
    print(ans)

    ans = s.minCount([1])
    print(ans)

    ans = s.minCount([2])
    print(ans)