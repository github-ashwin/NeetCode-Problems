from typing import List
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # Create hashmap first
        hm = {}
        for w in words:
            if w in hm:
                hm[w] += 1
            else:
                hm[w] = 1
        
        # Get the items (word,count)
        word_list = list(hm.items())

        # Sort the items - count in descending; if count is same, then in lexicographical order
        word_list.sort(key=lambda x:(-x[1],x[0]))

        # Get the top k words
        top_k_words = [word for word,_ in word_list[:k]]

        return top_k_words
        