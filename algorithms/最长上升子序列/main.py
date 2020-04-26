from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        dp = [0]*len(nums)
        dp[0] = 1
        for i in range(1, len(nums)):
            max_value = 0
            for j in range(0,i):
                if nums[i] > nums[j] and max_value<dp[j]:
                    max_value = dp[j]
            dp[i] = max_value + 1

        return max(dp)


if __name__ == '__main__':
    s = Solution()
    nums = [10,9,2,5,3,7,101,18]
    ans = s.lengthOfLIS(nums)
    print(ans)

    nums = []
    ans = s.lengthOfLIS(nums)
    print(ans)

    nums = [5,6,7,8,10,1,2,3,4,5,6,7,8,89,13]
    ans = s.lengthOfLIS(nums)
    print(ans)

    nums = [5,5]
    ans = s.lengthOfLIS(nums)
    print(ans)



    nums = [1, 3, 6, 7, 9, 4, 10, 5, 6]
    ans = s.lengthOfLIS(nums)
    print(ans)