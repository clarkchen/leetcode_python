class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        # 初始化矩阵
        len_h = len(height)
        matrix = [[0 for i in range(len_h)] for j in range(len_h)]
        ret = []
        for m in range(0, len_h):
            for n in range(len_h - 1, m, -1):
                if matrix[m][n] is None: continue
                # line[n] max area is with m
                # vertical n change to None
                if height[m] >= height[n]:
                    matrix[m][n] = (n - m) * height[n]
                    for j in range(m + 1, len_h):
                        matrix[j][n] = None
                # line[m] max area is with line[n]
                # horiztal m change to None
                elif height[m] <= height[n]:
                    matrix[m][n] = (n - m) * height[m]
                    for j in range(n - 1, m, -1):
                        matrix[m][j] = None
                print
                m, n, matrix[m][n]
                ret.append(matrix[m][n])

        max_area = max(ret)
        return max_area

if __name__ == '__main__':
    s = Solution()
    s.maxArea([2, 2, 2])