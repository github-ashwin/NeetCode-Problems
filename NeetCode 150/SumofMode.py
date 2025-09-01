class Solution:
    def sumOfModes(self, arr, k):
        # code here
        n = len(arr)
        mode_list = []

        # Helper method
        def hashing(arr):
            hmap = {}
            for i in arr:
                if i in hmap:
                    hmap[i] += 1
                else:
                    hmap[i] = 1
            return hmap

        def mode(freq_map):
            mode_val = None
            max_freq = -1
            for num, cnt in freq_map.items():
                if cnt > max_freq or (cnt == max_freq and (mode_val is None or num < mode_val)):
                    max_freq = cnt
                    mode_val = num
            return mode_val

        for i in range(n - k + 1):
            sub = arr[i:i + k]
            hmap = hashing(sub)
            mode_list.append(mode(hmap))

        return sum(mode_list)
