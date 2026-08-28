class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if not gas and not cost:
            return 0

        total_cost = 0
        total_gas = 0
        start_station = 0
        tank = 0

        for i in range(len(gas)):
            total_cost += cost[i]
            total_gas += gas[i]
            tank += gas[i] - cost[i]

            if tank < 0:
                start_station = i + 1
                tank = 0
            
        
        if total_gas < total_cost:
            return -1

        return start_station