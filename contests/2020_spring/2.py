from typing import List


class Solution:
    def ans(self, r_dict, k, src, target):
        if src == target and k == 0:
            return [[src]]
        elif k == 0:
            return []

        ret = []
        for x in r_dict.get(src,[]):
            sub = self.ans(r_dict, k-1, x,target)
            if not sub: continue

            for y in sub:
                temp_ret = [src]
                temp_ret.extend(y)
                ret.append(temp_ret)
        return ret

    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        r_dict = {}
        for item in relation:
            src = item[0]
            target = item[1]
            r_dict[src] = r_dict.get(src, [])
            r_dict[src].append(target)

        solutions = self.ans(r_dict, k, 0, n-1)
        # print(solutions)
        return len(solutions)



if __name__ == '__main__':
    s = Solution()
    ans = s.numWays(5, [[0,2],[2,1],[3,4],[2,3],[1,4],[2,0],[0,4]], 3)
    print(ans)
    # 输入：n = 3, relation = [[0,2],[2,1]], k = 2
    ans = s.numWays(3, [[0,2],[2,1]], 2)
    print(ans)
    ans = s.numWays(2, [[0,1]], 2)
    print(ans)
    ans = s.numWays(2, [[0,1]], 1)
    print(ans)
    #
    # ans = s.minCount([2, 3, 10])
    # print(ans)
    #
    # ans = s.minCount([1])
    # print(ans)
    #
    # ans = s.minCount([2])
    # print(ans)