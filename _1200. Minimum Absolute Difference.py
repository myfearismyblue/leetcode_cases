# Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.
#
# Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows
#
# a, b are from arr
# a < b
# b - a equals to the minimum absolute difference of any two elements in arr

class Solution:
    def minimumAbsDifference(self, arr):
        temp_arr = sorted(arr)
        assert len(temp_arr) >= 2
        answer = []
        current_lowest_diff = float("+inf")
        for idx in range(len(temp_arr)-1):
            current_diff = abs(temp_arr[idx] - temp_arr[idx + 1])
            if current_diff < current_lowest_diff:
                current_lowest_diff = current_diff
                answer = [[temp_arr[idx], temp_arr[idx + 1]]]
            elif current_diff == current_lowest_diff:
                answer.append([temp_arr[idx], temp_arr[idx + 1]])
        return answer


my_sol = Solution()
arr = [3,8,-10,23,19,-4,-14,27]
print(my_sol.minimumAbsDifference(arr))
