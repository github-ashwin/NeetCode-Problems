class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """

        punctuations = "!?',;."

        for p in punctuations:
            paragraph = paragraph.replace(p, " ")
        
        count = {}

        words = paragraph.lower().split()

        for i in words:
            if i not in banned:
                if i in count:
                    count[i] +=1
                else:
                    count[i] = 1
        return max(count,key=count.get)
        