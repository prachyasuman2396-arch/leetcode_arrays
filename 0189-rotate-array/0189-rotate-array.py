class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k %= n

        ans = [0] * n

        for i in range(n):
            ans[(i + k) % n] = nums[i]

        nums[:] = ans