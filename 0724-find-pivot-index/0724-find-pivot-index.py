class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        # always calculate the sum of all elements to the right of curr
        # initialize it once as sum(nums)
        # then just subtract nums[i] 
        right_sum = sum(nums)
        left_sum = 0

        for i in range(len(nums)):
            # exclude current index
            right_sum -= nums[i]
            if right_sum==left_sum:
                return i
            # add curr index for next iter
            left_sum += nums[i]

        return -1

        