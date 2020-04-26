class Solution:
    def maxScore(self, s: str) -> int:
        max_value = 0
        for i in range(0, len(s)-1):
            left = s[:i+1]
            right = s[i+1:]
            z_c = 0
            for x in left:
                if x=='0': z_c+=1
            o_c = 0
            for x in right:
                if x=='1': o_c+=1

            if o_c+z_c>max_value:
                max_value = o_c+z_c

        return max_value

if __name__ == '__main__':
    s = Solution()
    ans = s.maxScore("011101")
    print(ans)
    ans = s.maxScore("00111")
    print(ans)
    ans = s.maxScore("1111")
    print(ans)
    ans = s.maxScore("01")
    print(ans)
    ans = s.maxScore("11")
    print(ans)
    ans = s.maxScore("00")
    print(ans)
    ans = s.maxScore("111")
    print(ans)