class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals = sorted(intervals, key=lambda x: x[0])

        results = list()
        previous = intervals.pop(0)
        while intervals:
            current = intervals.pop(0)
            if previous[1] >= current[0]:
                previous = [min(current[0], previous[0]), max(current[1], previous[1])]
            else:
                results.append(previous)
                previous = current
        results.append(previous)
        return results
