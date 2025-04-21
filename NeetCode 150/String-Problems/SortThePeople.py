from typing import List
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        h_map = {heights[i]:names[i] for i in range(len(names))}
        h_result = sorted(h_map.keys(),reverse=True)

        output = [h_map[i] for i in h_result]
        return output