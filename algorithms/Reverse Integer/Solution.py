class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        max_int = 1<<32 -1
        min_int = -(1<<31)
        neg = False
        if x<0:
            neg=True
            x = - x
        ret = 0

        while x!=0:
            last = x%10
            x = x//10
            ret = 10*ret+last
            if (not neg and ret>max_int) or (neg and -ret <min_int):
                ret = 0
                break

        return ret if not neg else -ret