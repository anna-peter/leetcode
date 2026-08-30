class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # brute force: go through each num in nums1, if its not in nums2 add to answer[0]
        # then go through each num in nums[2], if its not in nums1 add to answer[1]
        # create a set of each of nums to check in o(1)
        nums1_set = set(nums1)
        nums2_set = set(nums2)

        answer = [[],[]]
        for num in nums1:
            if num not in nums2_set:
                answer[0].append(num)
        for num in nums2:
            if num not in nums1_set:
                answer[1].append(num)
        answer[0] = list(set(answer[0]))
        answer[1] = list(set(answer[1])) # ugly but should work
        return answer

        