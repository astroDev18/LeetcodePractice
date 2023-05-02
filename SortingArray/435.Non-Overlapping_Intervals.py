from typing import List

# Intervals Problem
def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    # Sort in order
    intervals.sort()
    # Count total overlaps
    res = 0
    # Retrieve the end of the first interval
    prevEnd = intervals[0][1]
    # Extract Start and End in 2nd interval
    for start, end in intervals[1:]:
        # compare interval starting with prevEnd to see if overlap exists
        if start >= prevEnd:
            # if true, move prevEnd forward to the end of current interval
            prevEnd = end
        else:
            # if false, overlap exists and increment res then set end to highest value
            res += 1
            prevEnd = min(end, prevEnd)
    return res

print(eraseOverlapIntervals(0, [[1,2],[2,3],[3,4],[1,3]]))