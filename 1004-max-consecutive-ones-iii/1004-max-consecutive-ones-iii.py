class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # flipping k 0s = finding a window that has <= k 0s
        # we want to maximize any window that satisifes this condition
        # start at left=0, right=k [left:right], this will satisfiy the condition for sure
        # if nums[right]==1, we expand the window by one, and so on until we reach a nums[right]==0
        # then we increment left, repeat the same process. store a maxLen and compare the new maxLen
        # end condition: right >=len

       
        # if 0: longest(k-1, nums[i:]). if 1: longest(k, nums{i:})

        # maxLen =0
        # for l in range(len(nums)):
        #     # search as far right as possible
        #     zeroes_left = k
        #     for r in range(l+1, len(nums)):
        #         if zeroes_left ==0:
        #             break
        #         if nums[r]==0:
        #             zeroes_left -=1

        #     maxLen = max(maxLen, r-l)
        # return maxLen
        maxLen = 0
        zeroes_used = 0
        l = 0
        for r in range(len(nums)):
            if nums[r]==0:
                # decrease avail k 
                zeroes_used +=1
            while zeroes_used >k:
                # must reduce window(?)
                if nums[l]==0:
                    zeroes_used -=1
                l+=1 # not sure why this is not inside the if. 
            curr_window = r-l+1
            maxLen = max(curr_window, maxLen)
        return maxLen

                
