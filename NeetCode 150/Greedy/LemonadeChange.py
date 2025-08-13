from typing import List
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # We have to provide the appropriate change to the customer so track 5 ollar and 10 dollar bill seperately
        d5 , d10 = 0,0

        for bill in bills:

            if bill == 5:
                d5+=1

            elif bill == 10:
                d10+=1
                if d5 >=1:
                    d5-=1
                else:
                    return False
            else:
                if d10 >=1 and d5 >=1:
                    d10-=1
                    d5-=1
                elif d5>=3:
                    d5-=3
                else:
                    return False

        return True
        