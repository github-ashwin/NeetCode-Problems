class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        result = []

        for i in range(len(nums)):
            result.append('1' if nums[i][i] =='0' else '0')
        result = ''.join(result)

        return result