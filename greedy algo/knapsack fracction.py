class Solution:
    def fractionalKnapsack(self, val, wt, capacity):
        item = sorted(
            zip(val, wt),
            key=lambda x: x[0]/x[1],
            reverse = True
        )
        final_val = 0
        cur_wt = 0
        
        for val, wt  in item:
            if cur_wt + wt <= capacity:
                cur_wt = cur_wt + wt
                final_val += val
            else:
                remain = capacity - cur_wt
                cost = val/wt * remain
                final_val += cost
                break
        return final_val