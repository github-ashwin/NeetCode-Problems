from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(nums, L, M, R):
            left = nums[L:M+1]
            right = nums[M+1:R+1]

            # i pointer for the array, p1 an p2 pointer for the subarrays
            i = L
            p1 = p2 = 0

            # Merge both subarrays
            while p1 < len(left) and p2 < len(right):
                if left[p1] <= right[p2]:
                    nums[i] = left[p1]
                    p1 += 1
                    i += 1
                else:
                    nums[i] = right[p2]
                    p2 += 1
                    i += 1
                

            while p1 < len(left):
                nums[i] = left[p1]
                p1 += 1
                i += 1

            while p2 < len(right):
                nums[i] = right[p2]
                p2 += 1
                i += 1

        def mergeSort(nums, l, r):
            if l >= r:
                return
            m = (l + r) // 2
            mergeSort(nums, l, m)
            mergeSort(nums, m + 1, r)
            merge(nums, l, m, r)

        mergeSort(nums, 0, len(nums) - 1)
        return nums
