"""
https://leetcode-cn.com/contest/weekly-contest-147/problems/largest-1-bordered-square/

最大的以 1 为边界的正方形

本质是 遍历矩阵，然后有一个 O(1) 的方法来看最大矩阵的面积

"""


class Solution:
    def __init__(self):
        self.length = 0
        self.width = 0
        self.right_matrix = None
        self.down_matrix = None
        self.grid = None

    def get_martix(self, grid):
        # right max
        right_matrix = []

        self.width = len(grid[0])
        self.length = len(grid)

        for x in range(0, self.length):
            l_m = []
            end = self.width - 1
            for y in range(end + 1, 0, -1):
                y = y - 1
                temp = 0
                if l_m:
                    temp = l_m[-1]
                if grid[x][y] == 1:
                    temp += 1
                else:
                    temp = 0
                l_m.append(temp)

            l_m.reverse()
            right_matrix.append(l_m)

        # down max

        down_matrix = [[0 for x in range(0, self.width)] for x in range(0, self.length)]
        for y in range(0, self.width):
            c_m = []
            end = self.length - 1
            for x in range(end + 1, 0, -1):
                x = x - 1
                temp = 0
                if c_m:
                    temp = c_m[-1]
                if grid[x][y] == 1:
                    temp += 1
                else:
                    temp = 0
                c_m.append(temp)
            c_m.reverse()

            for x in range(0, self.length):
                down_matrix[x][y] = c_m[x]

        self.right_matrix, self.down_matrix = right_matrix, down_matrix

        return right_matrix, down_matrix

    def getSquareArea(self, x, y, length):
        p1x, p1y = x, y + length - 1

        p2x, p2y = x + length - 1, y

        # 越界
        if p1y >= self.width or p2x >= self.length:
            return 0

        # 非越界
        if self.down_matrix[p1x][p1y] >= length and self.right_matrix[p2x][p2y] >= length:
            if self.down_matrix[x][y] >= length and self.right_matrix[x][y] >= length:
                return length * length

        return 0

    #
    def largest1BorderedSquare(self, grid) -> int:

        self.grid = grid
        self.get_martix(grid)

        max_area_list = [0]
        for x in range(0, self.length):
            for y in range(0, self.width):
                if grid[x][y] == 0: continue
                r_len = self.right_matrix[x][y]
                d_len = self.down_matrix[x][y]
                temp_list = [0]
                max_l = max(r_len, d_len)
                for l in range(max_l, 0, -1):
                    temp_list.append(self.getSquareArea(x,y, l))
                max_area_list.append(max(temp_list))

        return max(max_area_list)


def print_m(grid):
    print('-' * 20)
    for x in grid:
        print(x)
    print('-' * 20)


if __name__ == '__main__':

    # grid = [[1, 1,1], [1,0,1],[1,1,1]]
    # print(Solution().get_martix(grid))
    # print(Solution().largest1BorderedSquare(grid))
    # print(Solution().largest1BorderedSquare([[0]]))
    #
    s = Solution()

    grid = [[1,1,1],[1,1,0],[1,1,1],[0,1,1],[1,1,1]]
    print(Solution().get_martix(grid))

    print(Solution().largest1BorderedSquare(grid))
    print(Solution().largest1BorderedSquare(grid)==4)

    grid = [[1, 1, 1, 1, 1, 1], [1, 0, 1, 0, 1, 1], [1, 1, 1, 0, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 0]]
    print(s.largest1BorderedSquare(grid))
    print(s.largest1BorderedSquare(grid) == 25)

    grid = [[0, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 1, 1, 1, 0, 1, 1], [1, 1, 1, 1, 0, 1, 1, 1],
            [1, 0, 1, 0, 0, 1, 1, 1], [0, 1, 1, 1, 1, 0, 1, 1]]
    print(s.largest1BorderedSquare(grid))
    print(s.largest1BorderedSquare(grid)==9)

    grid = [[1,1,0,0]]
    print(s.largest1BorderedSquare(grid))
    print(s.largest1BorderedSquare(grid) == 1)

    grid = [[0,0]]
    print(s.largest1BorderedSquare(grid))
    print(s.largest1BorderedSquare(grid) == 0)
    # print_m(grid)
    # r, d = s.get_martix(grid)
    # print_m(r)
    # print_m(d)

    # print(s.largest1BorderedSquare(grid))
    # print(s.largest1BorderedSquare(grid)==9)

'''
111
110
111
011
111

'''
