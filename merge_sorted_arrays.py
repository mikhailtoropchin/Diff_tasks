# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
# and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:

        write_index = n + m - 1
        m, n = m - 1, n - 1

        while m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[write_index] = nums1[m]
                m -= 1
            else:
                nums1[write_index] = nums2[n]
                n -= 1
            write_index -= 1

        if n > -1:
            nums[0: n + 1] = nums2[0: n + 1]
        return nums1

sol = Solution()
print(sol.merge([1,2,3,0,0,0], 3, [2,5,6], 3))


