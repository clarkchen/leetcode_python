from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        for x in words:
            for y in words:
                if x==y:
                    continue
                if x in y:
                    res.append(x)
                    break
        return res

if __name__ == '__main__':
    s = Solution()
    words = ["mass", "as", "hero", "superhero"]
    print(s.stringMatching(words))
    words = ["leetcode", "et", "code"]
    print(s.stringMatching(words))
    words = ["blue","green","bu"]
    print(s.stringMatching(words))
