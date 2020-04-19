class Solution:
    def is_num(self, a):
        return '0' <= a <='9'

    def reformat(self, s: str) -> str:
        num_list = []
        char_list = []

        for i in s:
            if self.is_num(i):
                num_list.append(i)
            else:
                char_list.append(i)
        if abs(len(num_list)-len(char_list))>1:
            return ""
        elif len(num_list)<len(char_list):
            char_list, num_list = num_list, char_list

        ret=[]
        i = 0
        for n, c in zip(num_list, char_list):
            i+=1
            ret.extend([n,c])
        ret.extend(num_list[i:])
        return "".join(ret)

if __name__ == '__main__':
    s = Solution()
    ans = s.reformat("a0b1c2")
    print(ans)
    ans = s.reformat("leetcode")
    print(ans)
    ans = s.reformat("1229857369")
    print(ans)
    ans = s.reformat("covid2019")
    print(ans)
    ans = s.reformat("ab123")
    print(ans)
