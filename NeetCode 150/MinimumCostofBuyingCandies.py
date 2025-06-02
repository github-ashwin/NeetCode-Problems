class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        # print(cost)
        max_cost = cost[0]
        for i in range(1,len(cost)):
            if i%3!=2:
                max_cost +=cost[i]
        return max_cost

        

        