def maxSubArray(self, nums) -> int:
    lmax = float('-inf')
    gmax = float('-inf')
    n = len(nums)
    for i in range(n):
        lmax = max(nums[i], nums[i] + lmax)
        if gmax < lmax:
            gmax = lmax
    return gmax