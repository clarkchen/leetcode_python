from typing import List


class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        P = [x+1 for x in range(m)]
        ret = []
        for i in queries:
            idx = P.index(i)
            ret.append(idx)
            P.pop(idx)
            P.insert(0, i)
        return ret

if __name__ == '__main__':
    s = Solution()
    queries = [3, 1, 2, 1]
    m = 5
    print(s.processQueries(queries, m))
    queries = [4, 1, 2, 2]
    m = 4
    print(s.processQueries(queries, m))
