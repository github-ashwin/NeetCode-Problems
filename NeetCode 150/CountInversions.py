class Solution:
    def inversionCount(self, arr):
        # Code Here
        # MergeSort Approach
        res = 0
        
        def merge(left, right):
            nonlocal res
            merged = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] > right[j]:
                    merged.append(right[j])
                    j += 1
                    res += len(left) - i  # All remaining left[i...] are greater than right[j]
                else:
                    merged.append(left[i])
                    i += 1
            merged.extend(left[i:])
            merged.extend(right[j:])
            return merged
            
        def mergesort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = mergesort(arr[:mid])
            right = mergesort(arr[mid:])
            return merge(left, right)
        
        mergesort(arr)
        return res
