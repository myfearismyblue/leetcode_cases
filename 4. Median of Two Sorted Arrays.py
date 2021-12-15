# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
#
# The overall run time complexity should be O(log (m+n)).
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        nums1.extend(nums2)
        nums1.sort()
        lengh = len(nums1)
        median = float(
            nums1[int((lengh - 1) / 2)] if lengh % 2 else (nums1[int(lengh / 2 - 1)] + nums1[int(lengh / 2)]) / 2)
        return median
