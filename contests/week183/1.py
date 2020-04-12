from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        """
        逆序排列，看第几个数，大于 sum/2
        :param nums:
        :return:
        """
        nums.sort(reverse=True)
        l = nums
        total = sum(l)
        sum_test = 0
        res = []
        for i in range(len(l)):
            if sum_test>total/2:
                break
            sum_test += l[i]
            res.append(l[i])
        return res

if __name__ == '__main__':
    s=  Solution()
    print(s.minSubsequence([4,3,10,9,8]))
    print(s.minSubsequence([4,4,7,6,7]))
    print(s.minSubsequence([4]))
    print(s.minSubsequence([1,1,1]))
