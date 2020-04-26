from queue import PriorityQueue
from typing import List


class Solution:

    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        if len(nums)==1: return nums[0]
        dp = [0]*len(nums)
        dp[0] = nums[0]
        max_value = dp[0]
        pq = PriorityQueue()
        pq.put((-max_value, 0))
        for i in range(1, len(nums)):
            dp[i] = max(max_value, 0) + nums[i]

            if max_value < dp[i]:
                max_value = dp[i]
            pq.put((-dp[i], i))
            if i>=k:
                v = pq.get()
                max_value, max_idx = -v[0], v[1]
                if max_idx <= i-k:
                    v= pq.get()
                    max_value = -v[0]
                    max_idx = v[1]

                pq.put((-max_value, max_idx))

        return max(dp)

if __name__ == '__main__':
    # pq = PriorityQueue()
    #
    # for i in range(3, 0, -1):
    #     pq.put(i)
    #
    # pq = PriorityQueue()
    #
    # for i in range(3, 0, -1):
    #     pq.put(-i)
    #
    # print(-pq.get())

    s = Solution()
    nums = [10, 2, -10, 5, 20]
    k = 2
    ans = s.constrainedSubsetSum(nums, k)
    print(ans)
    assert ans == 37

    nums = [10, -2, -10, -5, 20]
    k = 2
    ans = s.constrainedSubsetSum(nums,k)
    print(ans)
    assert ans==23

    nums = [-1, -2, -3]
    k = 1
    ans = s.constrainedSubsetSum(nums, k)
    print(ans)
    assert ans == -1
