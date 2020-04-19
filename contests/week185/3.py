class Solution:
    def get_next_stat(self, x):
        s='croak'
        return s[(s.index(x)+1)%len(s)]

    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:

        if croakOfFrogs[0]!= 'c':
            return -1
        frog_idx = 1
        frog_dict = {self.get_next_stat('c'):[frog_idx]}
        ret = 0
        for item in croakOfFrogs[1:]:
            """
            该字符符合条件
            """
            if item in frog_dict:
                next_key = self.get_next_stat(item)
                this_frog = frog_dict[item].pop()
                frog_dict[next_key]=frog_dict.get(next_key, [])
                frog_dict[next_key].append(this_frog)
                if not frog_dict[item]: frog_dict.pop(item)
            else:
                # 新增青蛙叫不出来
                if item!='c':
                    return -1
                next_key = self.get_next_stat(item)
                frog_dict[next_key]=frog_dict.get(next_key, [])
                frog_idx += 1
                this_frog = frog_idx
                frog_dict[next_key].append(this_frog)
        for key, value in frog_dict.items():
            ret += len(value)
        if ret!=len(frog_dict.get('c',[])):
            return -1
        return ret



if __name__ == '__main__':
    s = Solution()
    print(s.get_next_stat("k"))

    params = "croakcroakcroakcroakcroakcroakcroakcroak"
    ans = s.minNumberOfFrogs(params)
    print(ans)
    assert ans==1

    print(s.get_next_stat("c"))
    params = "crcoakroak"
    ans = s.minNumberOfFrogs(params)
    print(ans)
    assert ans==2

    params = "croakcrook"
    ans = s.minNumberOfFrogs(params)
    print(ans)
    assert ans==-1

    params = "croakcroa"
    ans = s.minNumberOfFrogs(params)
    print(ans)
    assert ans==-1
    params = "croakcroakcroakcroakcroakcroakcroakcroakk"
    ans = s.minNumberOfFrogs(params)
    print(ans)