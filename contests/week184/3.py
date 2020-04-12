
class Solution:
    def entityParser(self, text: str) -> str:
        """
        双引号：字符实体为 &quot; ，对应的字符是 " 。
        单引号：字符实体为 &apos; ，对应的字符是 ' 。
        与符号：字符实体为 &amp; ，对应对的字符是 & 。
        大于号：字符实体为 &gt; ，对应的字符是 > 。
        小于号：字符实体为 &lt; ，对应的字符是 < 。
        斜线号：字符实体为 &frasl; ，对应的字符是 / 。
        :param text:
        :return:
        """
        map =  {
            "&quot;":"\"",
            "&apos;":"'",
            "&amp;": "&",
            "&gt;": ">",
            "&lt;":"<",
            "&frasl;":"/"
        }
        for key, value in map.items():
            text = text.replace(key, value)
        return text

if __name__ == '__main__':
    text = "&amp; is an HTML entity but &ambassador; is not."
    s = Solution()
    print(s.entityParser(text))
    text = "leetcode.com&frasl;problemset&frasl;all"
    print(s.entityParser(text))
    text = "and I quote: &quot;...&quot;"
    print(s.entityParser(text))
    text = "Stay home! Practice on Leetcode :)"
    print(s.entityParser(text))

    text = "Stay home! Practice on Leetcode :)  &apos;"
    print(s.entityParser(text))
