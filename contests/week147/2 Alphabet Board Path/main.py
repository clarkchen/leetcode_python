"""
https://leetcode-cn.com/contest/weekly-contest-147/problems/alphabet-board-path/

难点在于Z的位置，分别为 起点和终点时的情况

"""
class Solution:
    def get_location(self, c):
        ord_m = ord(c) - ord('a')
        x = int(ord_m / 5)
        y = ord_m % 5
        return x, y

    def get_str_x(self, x, y):
        m = x - y
        ret = ""
        if m > 0:
            ret = ''.join(['D'] * m)
        elif m < 0:
            ret = ''.join(['U'] * abs(m))

        return ret

    def get_str_y(self, x, y):
        m = x - y
        if m > 0:
            return ''.join(['R'] * m)
        if m < 0:
            return ''.join(['L'] * abs(m))
        return ""

    def get_path(self, x, y, current_x, current_y):
        temp = []
        x_str = self.get_str_x(x, current_x)

        y_str = self.get_str_y(y, current_y)

        if not x_str and not y_str:
            temp.append('!')
        else:
            temp.extend([x_str, y_str, "!"])
        return ''.join(temp)

    def alphabetBoardPath(self, target: str) -> str:
        ret = []
        current_x, current_y = 0, 0
        for c in target:
            p = ""
            x, y = self.get_location(c)
            # end is z
            if (x, y) == (5, 0) and (current_y != y):
                p = self.get_path(4, 0, current_x, current_y)
                p = p[:-1]
                p += "D!"
            # start is z
            elif (current_x, current_y) == (5, 0) and (current_y != y):
                p = self.get_path(x, y, 4, 0)
                p = "U"+p
            else:
                p = self.get_path(x, y, current_x, current_y)
            ret.append(p)
            current_y, current_x = y, x
        return "".join(ret)


if __name__ == '__main__':
    print(Solution().get_location('a'))
    print(Solution().get_location('l'))
    print(Solution().get_location('e'))
    print(Solution().alphabetBoardPath('a'))
    print(Solution().alphabetBoardPath('l'))
    print(Solution().alphabetBoardPath('leet') == "DDR!UURRR!!DDD!")
    print(Solution().alphabetBoardPath('code') == "RR!DDRR!UUL!R!")
    print(Solution().alphabetBoardPath('aaazaa'))
    print(Solution().alphabetBoardPath('zdz')=="DDDDD!UUUUURRR!DDDDLLLD!")
    print(Solution().alphabetBoardPath('uz'))
    print(Solution().alphabetBoardPath('vzv'))


    # print(Solution().get_str_x(0,2))
    # print(Solution().get_str_x(2,0))
