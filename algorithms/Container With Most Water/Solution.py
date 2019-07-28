class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        x = 0
        y = len(height)-1
        ret = []
        cal =0
        while x!=y:
            if height[x]>height[y]:
                ret.append(abs(y-x)*height[y])
                y-=1
            elif height[x]<=height[y]:
                ret.append(abs(y-x)*height[x])
                x+=1
            cal+=1
        max_area = max(ret)
        return max_area

if __name__ == '__main__':
    s = Solution()
    print (s.maxArea([2, 2, 2]))