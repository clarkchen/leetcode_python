import queue
from typing import List


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        q = queue.Queue()
        q.put((nums[0][0],0,0))
        res = []
        label = {}
        while not q.empty():
            value, x, y = q.get()
            if x+1<len(nums) and len(nums[x+1])>y:
                down = (nums[x+1][y], x+1, y)
                if not label.get((x+1,y)):
                    q.put(down)
                    label[(x+1, y)] = 1
            if y+1<len(nums[x]):
                right = (nums[x][y+1], x, y+1)
                if not label.get((x,y+1)):
                    q.put(right)
                    label[(x,y+1)]=1
            res.append(value)
        return res

if __name__ == '__main__':
    s= Solution()
    nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    ans = s.findDiagonalOrder(nums)
    print(ans)

    nums = [[1, 2, 3, 4, 5], [6, 7], [8], [9, 10, 11], [12, 13, 14, 15, 16]]
    ans = s.findDiagonalOrder(nums)
    print(ans)