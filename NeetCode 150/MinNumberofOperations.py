class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        n = len(boxes)
        result = []

        for i in range(n):
            op = 0
            for j in range(n):
                if boxes[j]=='1':
                    op += abs(i-j)
            result.append(op)

        return result