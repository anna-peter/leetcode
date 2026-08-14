class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        # create a list of all numbers that need to appear and "tick them off"
        # we could also just use the index as the numbers and mark a boolean if its ticked off
        numbers = [i for i in range(n+1)]
        nums_set = set(nums)
        for num in numbers:
            if num not in nums_set:
                return num

        