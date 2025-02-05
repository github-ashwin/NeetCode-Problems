class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sum_set = set()

        while n!=1:
            if n in sum_set:
                return False
            sum_set.add(n)
            
            n = sum(int(num)**2 for num in str(n))
            
        return True

        