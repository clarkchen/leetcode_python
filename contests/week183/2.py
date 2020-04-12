class Solution:

    def add_byte_by_one(self, s:str):
        add_item = 1
        ans = list(s)
        for i in range(len(ans)-1, -1, -1):
            if ans[i]=='1':
                ans[i] = '0'
            elif ans[i]=='0':
                ans[i]='1'
                add_item = 0
            if add_item==0:
                break

        if add_item==1:
            ans.insert(0,'1')
        return "".join(ans)

    def devide_byte_by_two(self, s:str):
        ans = list(s)
        ret = [ans[-1]]+ans[:-1]
        cur = 0
        while ret[cur]=='0':
            cur+=1
        return "".join(ret[cur:])
    def numSteps(self, s: str) -> int:
        # number = self.get_number_from_byte(s)
        # print()
        number = s
        step = 0
        while not(number=='1'):
            # print(number)
            if number[-1]=='1':
                number = self.add_byte_by_one(number)
            else:
                number = self.devide_byte_by_two(number)
            step+=1
        return step
if __name__ == '__main__':
    s = Solution()
    print(s.numSteps(s="1101"))
    print(s.numSteps('10'))
    print(s.numSteps("1111011110000011100000110001011011110010111001010111110001"))
    # print(s.add_byte_by_one("11"))
    # print(s.devide_byte_by_two("110"))