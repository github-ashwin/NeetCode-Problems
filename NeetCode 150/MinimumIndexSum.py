class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        index_map = {name: i for i, name in enumerate(list1)}
        min_sum = float('inf')
        result = []

        for j, name in enumerate(list2):
            if name in index_map:
                total_index = index_map[name] + j
                if total_index < min_sum:
                    result = [name]
                    min_sum = total_index
                elif total_index == min_sum:
                    result.append(name)

        return result
        