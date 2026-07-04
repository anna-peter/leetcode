class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # threesum(i, j, k) = threesum(i + j, 0, k)
        # threesum(0,0,0) = 1
        # threesum([i,j,k]) = 1 if i+j+k=0 else 0
        # threesum([i,j,k,x]) = threesum([i+j, k, x]) + threesum([i, j+k, x]) + threesum([i, j, k+x])
        # threesum([i,j,k,x,y]) = threesum([i,j,k,x]) + 
        if len(nums)==3:
            return [nums] if nums[0]+nums[1]+nums[2]==0 else []
        # threesum(i, j, k) = twosum(i+j, k) + twosum(i, j+k)
        res = []
        nums.sort() # sorts ascending
        for i in range(len(nums)):
            if nums[i]>0:
                break #bc we sorted we could never reach 0
            if i>0 and nums[i]==nums[i-1]:
                continue # skip duplicates

            two_sum = self.twoSum(nums[i],nums[i+1:])
            # print(two_sum)
            for x in two_sum:
                res.append([x[0],x[1],nums[i]])
        return res
        
        
    def twoSum(self, a, nums:list[int]) -> list[list[int]]:    

        res = []

        matches = set() # store found values
        found_pairs = set()
        for k in range(len(nums)):
            neg_k = -nums[k]-a
            # print(f"looking for {a} with {nums[k]}")

            if neg_k in matches: 
                if ((nums[k],neg_k)) not in found_pairs:
                    res.append([nums[k],neg_k])
                    found_pairs.add((nums[k],neg_k))
            else:
                matches.add(nums[k])
            
        return res
            
        
        