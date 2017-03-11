class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row_one = set(list("qwertyuiop"))
        row_two = set(list("asdfghjkl"))
        row_three = set(list("zxcvbnm"))
        rows = [row_one, row_two, row_three ]
        words_of_set = [set(list(x.lower())) for x in words]
        l = []
        for i,x in enumerate(words_of_set):
            for row in rows:
                temp = row & x
                if len(temp)==len(x):
                    l.append(i)
        return [words[i] for i in l]
