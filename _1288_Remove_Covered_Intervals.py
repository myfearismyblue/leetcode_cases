# Given an array intervals where intervals[i] = [li, ri] represent the interval [li, ri),
# remove all intervals that are covered by another interval in the list.
#
# The interval [a, b) is covered by the interval [c, d) if and only if c <= a and b <= d.
#
# Return the number of remaining intervals.

# Example 1:
#
# Input: intervals = [[1,4],[3,6],[2,8]]
# Output: 2
# Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
# Example 2:
#
# Input: intervals = [[1,4],[2,3]]
# Output: 1
from typing import List


class Solution:
    class ConstrainViolation(Exception):
        pass

    def check_constrains(self, intervals=None, boundary=None, current_interval=None):
        """Checks if constrains are violated
        boundary - l or r,
        current_interval - intervals[i]"""
        if (boundary is not None and not 0 <= boundary <= 10 ** 5 or
                current_interval is not None and len(current_interval) > 2
            ):
            raise self.ConstrainViolation('Constrain Violation')
        if intervals is not None:
            _ = set()
            [_.add(tuple(item)) for item in intervals]
            if not 0 < len(intervals) <= 1000 or len(intervals) != len(_):
                raise self.ConstrainViolation('Constrain Violation')

    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        self.check_constrains(intervals)

        temp_intervals = set()
        [temp_intervals.add(tuple(item)) for item in intervals]
        covered = set()
        checked = set()

        for item in temp_intervals:
            current_left, current_right = item[0], item[1]
            self.check_constrains(boundary=current_left, current_interval=item)
            self.check_constrains(boundary=current_right)
            checked.add(item)
            remain = temp_intervals.difference(checked.union(covered))
            for other_item in remain:
                if current_left <= other_item[0] and other_item[1] <= current_right:  # item covers other_item
                    covered.add(other_item)
                elif other_item[0] <= current_left and current_right <= other_item[1]:  # other_item covers item
                    covered.add(item)
                    break

        return len(temp_intervals) - len(covered)