class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])

        res = []

        s = intervals[0][0]
        e = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= e:
                e = max(intervals[i][1], e)
            else:
                res.append([s,e])
                s = intervals[i][0]
                e = intervals[i][1]
        
        res.append([s,e])
        return res
