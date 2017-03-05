# -*- coding:utf-8 -*-
__author__ = 'chenxi'


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        assert isinstance(nums1, list) and isinstance(nums2, list)

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        max_left = None
        min_right = None
        e1 = len(nums1)
        e2 = len(nums2)
        e = e1
        s = 0
        bc = (len(nums1) + e2 + 1) // 2

        if len(nums1) == 0:
            max_left = nums2[(e2 - 1) // 2]
            min_right = nums2[(e2 - 1) // 2 + 1] if e2 > 1 else None
            if (len(nums1) + e2) % 2 == 0:
                return (max_left + min_right) / 2.0
            else:
                return max_left
        else:
            while 0 <= s <= e:
                i = (s + e) // 2
                j = bc - i
                # if not (and ):break
                if i > 0 and nums1[i - 1] > nums2[j]:
                    e = i
                elif i < e and nums2[j - 1] > nums1[i]:
                    s = i + 1
                else:
                    break
            # nums 1 all to right
            if i == 0:
                max_left = nums2[j - 1]
            # nums 1 all to left
            elif j == 0:
                max_left = nums1[i - 1]
            else:
                max_left = max(nums1[i - 1], nums2[j - 1])
            if (e1 + e2) % 2 == 1: return max_left

            if i == e1:
                min_right = nums2[j]
            elif j == e2:
                min_right = nums1[i]
            else:
                min_right = min(nums1[i], nums2[j])

            return (max_left + min_right) / 2.0
