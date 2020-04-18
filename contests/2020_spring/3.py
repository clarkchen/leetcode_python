from typing import List


class Solution:

    def get_min_idx(self, l, search):
        i = 0
        for x in l:
            if x<search:
                i+=1
            else:
                break
        return i

    def binary_search(self, alist, item):
        """
        二分查找 ，早最小值

        """
        n = len(alist)
        start = 0
        end = n - 1
        if item > alist[-1]: return -1
        if item < alist[0]: return 0
        while start <= end:
            mid = (start + end) // 2
            if alist[mid] == item:
                break
            elif item < alist[mid]:
                end = mid - 1
            else:
                start = mid + 1
        while mid > 0 and alist[mid]==alist[mid-1] and alist[mid]==item:
            mid -= 1
        if alist[mid]<item:
            mid+=1
        return mid

    def getTriggerTime(self, increase: List[List[int]], requirements: List[List[int]]) -> List[int]:
        self.C = [0]
        self.R = [0]
        self.H = [0]

        for c,r,h in increase:
            self.C.append(c+self.C[-1])
            self.R.append(r + self.R[-1])
            self.H.append(h + self.H[-1])
        # return self.C, self.R, self.H
        # print(self.C, self.R, self.H)
        ret = []
        # print(len(increase), len(self.C))
        for c,r,h in requirements:
            c_idx = self.binary_search(self.C, c)
            # if c_idx>len(self.C):
            #     ret.append(-1);continue;
            r_idx = self.binary_search(self.R, r)
            # if r_idx > len(self.R):
            #     ret.append(-1);continue;
            h_idx = self.binary_search(self.H, h)
            # if h_idx > len(self.H):
            #     ret.append(-1);continue;
            temp = [c_idx, r_idx, h_idx]
            if min(temp)==-1:
                ret.append(-1)
            else:
                ret.append(max(temp))

            # print(c_idx, r_idx, h_idx)
        return ret


if __name__ == '__main__':
    # ncrease = [[2,8,4],[2,5,0],[10,9,8]] requirements = [[2,11,3],[15,10,7],[9,17,12],[8,1,14]]
    s = Solution()
    print(s.binary_search([0, 2, 4, 14], 2))
    print(s.binary_search([0, 2, 4, 14], 15))

    print(s.binary_search([0, 2, 4, 14], 14))
    print(s.binary_search([0, 2, 4, 14], 9))
    print(s.binary_search([0, 2, 4, 14], 5))
    print(s.binary_search([0, 2, 4, 14], 0))
    print(s.binary_search([2, 2, 2, 2,2,2,2, 2], 2))

    print(s.binary_search([0, 2, 9,15,20,],9))
    print(s.binary_search([0, 2, 9,15,20,],8))
    print(s.binary_search([0, 2, 9,15,20,],10))


    print(s.binary_search([0, 2, 4, 14], 500))
    print(s.binary_search([0, 2, 4, 14], -1))
    print(s.binary_search([0, 2, 4, 14], 3))






    ans = s.getTriggerTime([[2,8,4],[2,5,0],[10,9,8]], [[2,11,3],[15,10,7],[9,17,12],[8,1,14]])
    print(ans)
    # 输入： increase = [[0,4,5],[4,8,8],[8,6,1],[10,10,0]] requirements = [[12,11,16],[20,2,6],[9,2,6],[10,18,3],[8,14,9]]
    ans = s.getTriggerTime([[0,4,5],[4,8,8],[8,6,1],[10,10,0]],[[12,11,16],[20,2,6],[9,2,6],[10,18,3],[8,14,9]])
    print(ans)

    increase = [[1, 1, 1]]
    requirements = [[0, 0, 0]]
    ans = s.getTriggerTime(increase,requirements)
    print(ans)

    increase = [[1, 1, 1], [1, 1, 1]]
    requirements = [[2, 2, 2]]
    ans = s.getTriggerTime(increase, requirements)
    print(ans)
    increase = [[1, 1, 1], [1, 1, 1]]
    requirements = [[2, 2, 3]]
    ans = s.getTriggerTime(increase, requirements)
    print(ans)

    increase = [[0, 1, 0],[1, 1, 1]]
    requirements = [[0, 1, 0]]
    ans = s.getTriggerTime(increase, requirements)
    print(ans)


    increase = [[1, 1, 1],[0, 1, 100000] ]
    requirements = [[0, 1, 100000]]
    ans = s.getTriggerTime(increase, requirements)
    print(ans)

    # 二分查找特殊情况
    increase = [[2,2, 3], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    requirements = [[2, 2, 3]]
    ans = s.getTriggerTime(increase, requirements)
    print(ans)

    increase = [[2, 2, 3], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    requirements = [[2, 2, 4]]
    ans = s.getTriggerTime(increase, requirements)
    print(ans)

'''

[0, 2, 4, 14] [0, 8, 13, 22] [0, 4, 4, 12]
[1, 2, 1]
[4, 2, 3]
[4, 3, 3]
[4, 1, 4]
[2, -1, -1, -1]


[0, 2, 4, 14] [0, 8, 13, 22] [0, 4, 4, 12]
[1, 2, 1]
[4, 2, 3]
[3, 3, 3]
[3, 1, 4]
[2, -1, 3, -1]


'''