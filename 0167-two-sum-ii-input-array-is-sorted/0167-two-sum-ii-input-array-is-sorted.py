class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # non-decreasing -> next value is always >= previous
        # use two pointers, left and right
        # increase left if target is < current_sum; decrease right else
        # return the two found indices, +1 as required

        # base case: length is 2
        if len(numbers)==2:
            return [1,2] # this is the only solution

        # initialize our two pointers
        left = 0
        right = len(numbers)-1

        while left < right:
            current_sum = numbers[left]+numbers[right]
            # found our targer
            if target==current_sum:
                return [left+1,right+1]

            if target > current_sum:
                # our target is higher, so we need to increase the sum, move left
                left +=1
            else:
                right -=1
        