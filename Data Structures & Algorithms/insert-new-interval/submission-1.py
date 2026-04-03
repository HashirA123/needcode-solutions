class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []

        s = newInterval[0]
        e = newInterval[1]

        i = 0

        while i < len(intervals):
            if s > intervals[i][1]:
                res.append(intervals[i])
            elif (s <= intervals[i][1] and intervals[i][0] <= s) or (e <= intervals[i][1] and intervals[i][0] <= e):
                s = min(s, intervals[i][0])
                e = max(e, intervals[i][1])
            elif e < intervals[i][0]:
                res.append([s,e])
                break
            i += 1

        if i == len(intervals):
            res.append([s,e])
        else:
            while i < len(intervals):
                res.append(intervals[i])
                i += 1
        return res


            
