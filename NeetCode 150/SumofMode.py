import heapq
class Solution:
    def sumOfModes(self, arr, k):
        # code here
        
        # n = len(arr)
        # mode_list = []

        # # Helper method
        # def hashing(arr):
        #     hmap = {}
        #     for i in arr:
        #         if i in hmap:
        #             hmap[i] += 1
        #         else:
        #             hmap[i] = 1
        #     return hmap

        # def mode(freq_map):
        #     mode_val = None
        #     max_freq = -1
        #     for num, cnt in freq_map.items():
        #         if cnt > max_freq or (cnt == max_freq and (mode_val is None or num < mode_val)):
        #             max_freq = cnt
        #             mode_val = num
        #     return mode_val

        # for i in range(n - k + 1):
        #     sub = arr[i:i + k]
        #     hmap = hashing(sub)
        #     mode_list.append(mode(hmap))

        # return sum(mode_list)
        
        n = len(arr)
        if k > n:
            return 0

        freq = {}                     # Frequency map
        heap = []                     # Max heap (freq as -ve for max behavior)
        total_sum = 0

        # --- Initialize first window ---
        for i in range(k):
            freq[arr[i]] = freq.get(arr[i], 0) + 1
        for num, f in freq.items():
            heapq.heappush(heap, (-f, num))  # Push as (-frequency, number)

        # Helper: get current mode
        def get_mode():
            while heap:
                f, num = heap[0]
                if num in freq and -f == freq[num]:   # Valid frequency
                    return num
                heapq.heappop(heap)   # Remove outdated entry
            return 0  # fallback (shouldn't happen for valid k)

        total_sum += get_mode()

        # --- Slide the window ---
        for i in range(k, n):
            # Remove outgoing element
            outgoing = arr[i - k]
            freq[outgoing] -= 1
            if freq[outgoing] == 0:
                del freq[outgoing]
            else:
                # push updated outgoing frequency so heap has current state
                heapq.heappush(heap, (-freq[outgoing], outgoing))

            # Add incoming element
            incoming = arr[i]
            freq[incoming] = freq.get(incoming, 0) + 1

            # Push updated counts to heap
            heapq.heappush(heap, (-freq[incoming], incoming))

            # Add current mode
            total_sum += get_mode()

        return total_sum
