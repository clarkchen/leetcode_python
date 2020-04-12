class Solution:
    def numOfWays(self, n: int) -> int:
        aba = 6
        abc = 6
        MOB = int(1e9)+7
        for i in range(n-1):
            aba, abc = (aba*3+abc*2)%MOB, (aba*2+abc*2)%MOB
        ret = (aba + abc)%MOB
        return ret


if __name__ == '__main__':
    s = Solution()
    print(s.numOfWays(1))
    print(s.numOfWays(2))
    print(s.numOfWays(3))
    print(s.numOfWays(4))
    print(s.numOfWays(7))
    print(s.numOfWays(5000))