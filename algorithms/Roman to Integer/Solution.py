class Solution(object):
    key_value = {
        "I":1, "V":5, "X":10,
        "L":50, "C":100, "D":500, "M":1000

    }

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        kv = self.key_value
        ret = 0
        i = 0
        while i<len(s):
            c = s[i]
            i += 1
            c_v = kv.get(c)
            if i<len(s):
                n_v = kv.get(s[i])
                if n_v > c_v:
                    ret+=n_v-c_v
                    i+=1
                    continue
            ret+=c_v


        return ret