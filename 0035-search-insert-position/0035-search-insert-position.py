class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = left + ((right - left) // 2) # // gives us the floor
           
            mid_value = nums[mid]
            # print(f"at mid {mid} with val {mid_value}")
            if target == mid_value:
                return mid
            elif target < mid_value:
                # target has to be between left and middle
                # we can move right down to the middle
                right = mid-1
            else:
                # target is between middle and right
                # move left up to the middle
                left = mid+1
        return left
            

# 1,2,3,5,6 | 4
#left=0 (1), right=4 (6) -> mid = 2 (3)
# left = 2 (3) and right = 4 (6). mid = 3 (5)
# left = 2 (3) right = 3 (5). mid 1//2=0 mid = 2 (3)
        