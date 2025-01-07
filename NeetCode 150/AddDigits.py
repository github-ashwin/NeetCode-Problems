class Solution:
    def addDigits(self, num: int) -> int:
        sum = 0
        while num!=0:
            n = num%10
            sum +=n
            num = num//10

            if num==0 and sum>9:
                num = sum
                sum = 0
                     
        return sum