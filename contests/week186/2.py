from typing import List


class Solution:
    record = {}
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k==0: return 0
        first = cardPoints[0]
        last = cardPoints[-1]
        v1 = self.maxScore(cardPoints[1:], k-1)
        v2 = self.maxScore(cardPoints[:-1], k-1)
        v1 = first+v1
        v2 = last+v2
        if v1 > v2:
            return v1
        else:
            return v2


if __name__ == '__main__':
    s = Solution()
    cardPoints = [1, 79, 80, 1, 1, 1, 200, 1]
    k = 3

    ans = s.maxScore(cardPoints, k)
    print(ans)

    cardPoints = [1, 1000, 1]
    k = 1
    ans = s.maxScore(cardPoints, k)
    print(ans)

    cardPoints = [1, 2, 3, 4, 5, 6, 1]
    k = 3
    ans = s.maxScore(cardPoints, k)

    print(ans)

    # 232
    ans = s.maxScore([11, 49, 100, 20, 86, 29, 72], 4)

    print(ans)

    ans = s.maxScore([1, 2, 3, 4, 5, 6, 1], 3)
    print(ans)
