from typing import List
from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        strlist = list(map(str,nums))

        def comparator(a,b):
            if a+b>b+a:
                return -1
            elif a+b<b+a:
                return 1
            else:
                return 0

        strlist.sort(key=cmp_to_key(comparator))

        if strlist[0]=='0':
            return "0"

        result = ''.join(strlist)

        return result

        