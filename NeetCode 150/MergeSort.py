class Solution:
    
    def merge(self, arr, left, mid, right):
        # Lengths of two subarrays
        l1 = mid - left + 1
        l2 = right - mid

        # Temporary subarrays
        left_part = arr[left:mid+1]
        right_part = arr[mid+1:right+1]

        i = j = 0
        k = left 

        # Merge the subarrays
        while i < l1 and j < l2:
            if left_part[i] <= right_part[j]:
                arr[k] = left_part[i]
                i += 1
            else:
                arr[k] = right_part[j]
                j += 1
            k += 1

        # Copy remaining elements of left_part
        while i < l1:
            arr[k] = left_part[i]
            i += 1
            k += 1

        # Copy remaining elements of right_part
        while j < l2:
            arr[k] = right_part[j]
            j += 1
            k += 1

    def mergeSort(self, arr, l, r):
        if l < r:
            m = (l + r) // 2
            self.mergeSort(arr, l, m)
            self.mergeSort(arr, m + 1, r)
            self.merge(arr, l, m, r)
