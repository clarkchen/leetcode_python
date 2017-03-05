# -*- coding:utf-8 -*-
__author__ = 'chenxi'


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        offset = self.find_off_set(nums1, nums2)
        # new_l = nums1.expend(nums2)
        media_index1 = int(len(nums1) / 2)
        media_index2 = int(len(nums2) / 2)
        a = None
        if offset >= media_index1:
            a = nums2[media_index2 - offset]
        # elif offset> media_index2:
        #     return nums1[media_index1 + offset]
        else:
            a = nums1[media_index1 + offset]

        if (len(nums1)+len(nums2))%2==0:
            pass
            # b=

        return (a+b)/2

    def find_off_set(self, nums1, nums2, m1, m2):
        # nums 1 已经迭代挖鼻
        if not (0<=m1<len(nums1)) and not (0 <=m2<len(nums2)): return None,None
        elif not (0<=m1<len(nums1)): return None, nums2[m2]
        elif not (0 <=m2<len(nums2)): return m1, None
        p12 = self.find_postion(nums2, nums1[m1], 0, len(nums2))
        p21 = self.find_postion(nums1, nums2[m2], 0, len(nums1))
        off1 = m2-p12
        off2 = m1-p21

        if off1==0 and off2==0:
            return m1, m2

        res = [
            self.find_off_set(nums1, nums2, m1+off1,m2), self.find_off_set(nums1, nums2, m1, m2+off2),
            self.find_off_set(nums1, nums2, m1+off1, m2+off2)
        ]
        for ret1, ret2 in res:
            if ret1!=None and ret2!=None:
                return ret1, ret2

        return None, None


        media_index1 = int(len(nums1) / 2)
        media_index2 = int(len(nums2) / 2)
        if abs(offset) >= media_index1 or abs(offset)>=media_index2: return offset

        media1 = nums1[int(len(nums1) / 2 + offset)]
        new_index =
        meida2_index = int(len(nums2) / 2)
        media2 = nums2[meida2_index]

        new_offset = meida2_index - new_index
        if media1 == media2: return offset
        return self.find_off_set(nums1, nums2, new_offset)

    def find_postion(self, nums, target, start, end):
        """
        二分查找
        :param nums:
        :param target:
        :return:
        """
        media = int((start + end) / 2)
        if start >= end or target == nums[media]: return media

        if target < nums[media]:
            return self.find_postion(nums, target, start, media - 1)
        else:
            return self.find_postion(nums, target, media + 1, end)


if __name__ == '__main__':
    s = Solution()
    l = [1, 2, 2, 2, 2, 2, 2, 2, 4]
    print(s.find_postion(l, 3, 0, len(l)))
