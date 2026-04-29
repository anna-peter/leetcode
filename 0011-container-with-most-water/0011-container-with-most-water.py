class Solution:
    def maxArea(self, height: List[int]) -> int:
        # each elem is a given height
        # water area = min(h_l, h_r) * (index(r)-index(l))

        # we start with 2 pointers l, r
        # move whichever is lower in 
        # compute area at each step, keep track of a maximum 
        # stop when distance = 1
        # return the maximum that we kept track of

        # ugli but works ig
        if len(height)==1:
            return height[0]
        elif len(height)==2:
            return min(height[0],height[1])

        max_area = 0

        left = 0
        right = len(height) - 1 
        distance = right - left

        while distance > 1: 
            distance = right - left # e.g [1,1]-> distance is 1
            
            area = min(height[left], height[right]) * distance
            max_area = max(area, max_area)
            # print(f"area {area} distance {distance}  max area {max_area}")
            if height[left]<height[right]:
                left+=1 # left is shorter
            else:
                right -=1
        return max_area


