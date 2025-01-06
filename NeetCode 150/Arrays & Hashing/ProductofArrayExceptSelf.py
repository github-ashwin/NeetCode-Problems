class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # result = [0]*len(nums)
        # for i in range(len(nums)):
        #     prd = 1
        #     for j in range(len(nums)):
        #         if i==j:
        #             continue
        #         prd = prd*nums[j]
        #     result[i] = prd
        
        # return result
        
        l = len(nums)

        result = [1] * l

        # first find prefixes

        prefix = 1

        for i in range(l):
            result[i] = prefix
            prefix = prefix * nums[i]

        # finding postifixes

        postfix = 1

        for i in range(l -1,-1,-1):
                result[i] = result[i] * postfix
                postfix = postfix * nums[i]
        return result 