class Solution:
    @classmethod
    def naive(cls, intervals, newInterval):
        res = []
        for interval in intervals:
            if interval[1]>=newInterval[0] and interval[0]<=newInterval[1]:
                newInterval = [min(interval[0], newInterval[0]), 
                    max(interval[1], newInterval[1])]
            else:
                if interval[0] > newInterval[0]:
                    interval, newInterval = newInterval, interval
                res.append(interval)
        res.append(newInterval)
        return res

if __name__ == "__main__":
    inputs = [
        ([[1,3],[6,9]], [2,5], [[1,5],[6,9]]),
        ([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8], [[1,2],[3,10],[12,16]])
    ]
    for intervals, newInterval, expected in inputs:
        print(Solution.naive(intervals, newInterval))
        print("----")