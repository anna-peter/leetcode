class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums)==1:
            return nums[0] # base case
        
        # we could brute force it by sliding over each subarray of len k, computing the average, and comparing it to the current max average
        # this can be improved by keeping the sum of the window first, and subtracting the last while adding the next value (O(1) operations) and comping that as the average

        # window start and end indices
        window_left = 0
        window_right = k

        # initialize max_average and sum
        current_sum = sum(num for num in nums[:k])
        max_average = current_sum / k

        while window_right < len(nums):
            current_sum -= nums[window_left]
            current_sum += nums[window_right]

            current_average = current_sum / k

            max_average = max(max_average, current_average)
            window_right +=1
            window_left +=1
        return max_average


