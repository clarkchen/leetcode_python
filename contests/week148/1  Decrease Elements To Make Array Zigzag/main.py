"""
https://leetcode-cn.com/contest/weekly-contest-148/problems/decrease-elements-to-make-array-zigzag/

"""
from typing import List


class Solution:

    def get_ans(self, nums, lower):
        if len(nums) == 1: return 0

        if lower == 1:
            if nums[0] < nums[1]:
                return self.get_ans(nums[1:], lower=1 - lower)
            if nums[0] >= nums[1]:
                m = nums[0] - nums[1] + 1
                return m + self.get_ans(nums[1:], lower=1 - lower)
        else:
            if nums[0] > nums[1]:
                return self.get_ans(nums[1:], lower=1 - lower)
            if nums[0] <= nums[1]:
                m = nums[1] - nums[0] + 1
                nums[1] = nums[0]-1
                return m + self.get_ans(nums[1:], lower=1 - lower)

    def movesToMakeZigzag(self, nums: List[int]) -> int:
        res = min([self.get_ans(nums.copy(), 0), self.get_ans(nums.copy(), 1)])
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3]
    res = s.movesToMakeZigzag(nums)
    print(res)

    nums = [9, 6, 1, 6, 2]
    res = s.movesToMakeZigzag(nums)
    print(res)

    nums = [50, 100, 40]
    res = s.movesToMakeZigzag(nums)
    print(res)

    nums = [1, 100, 10000]
    res = s.movesToMakeZigzag(nums)
    print(res)

    nums = [1, 100, 500, 500]
    res = s.movesToMakeZigzag(nums)
    print(res)

    nums = [1, 100, 500, 10000]
    res = s.movesToMakeZigzag(nums)
    print(res)

    nums = [1]
    res = s.movesToMakeZigzag(nums)
    print(res)

    nums = [1, 2, 1]
    res = s.movesToMakeZigzag(nums)
    print(res)
    assert res ==0

    nums = [2, 1, 2]
    res = s.movesToMakeZigzag(nums)
    print(res)

    nums = [10, 4, 4, 10, 10, 6, 2, 3]
    res = s.movesToMakeZigzag(nums)
    print(res)#13

    nums = [1, 2, 3]
    res = s.movesToMakeZigzag(nums)
    print(res)
    assert res ==2

    nums = [27, 178, 78, 220, 632, 305, 116, 817, 348, 278, 213, 133, 466, 108, 915, 277, 929, 745, 57, 80, 759, 137,
            678, 348, 699, 149, 344, 60, 870, 62]
    res = s.movesToMakeZigzag(nums)
    print(res)
