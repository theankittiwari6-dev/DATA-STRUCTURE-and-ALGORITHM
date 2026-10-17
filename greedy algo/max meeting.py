class Solution:
    def activitySelection(self, start: list[int], finish: list[int]) -> int:
        #code here
        item = sorted(
            zip (start, finish),
            key = lambda x: x[1]
        )
        result = 0
        prev_fin = -1
        for start, finish in item:
            if start > prev_fin:
                result += 1
                prev_fin = finish
        return result
            