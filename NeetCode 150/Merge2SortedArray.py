class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        c1 = m - 1
        c2 = n - 1
        p = m + n - 1

        while c1 >= 0 and c2 >= 0:
            if nums1[c1] > nums2[c2]:
                nums1[p] = nums1[c1]
                c1 -= 1
            else:
                nums1[p] = nums2[c2]
                c2 -= 1
            p -= 1

        while c2 >= 0:
            nums1[p] = nums2[c2]
            c2 -= 1
            p -= 1
        