from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        heap = []

        # min heap will sort by the lowest frequency first
        for num, freq in counts.items():
            heapq.heappush(heap, (freq, num))

            # if the heap's length exceeds k, pop the minimum
            if len(heap)>k:
                heapq.heappop(heap)
        
        result = [pair[1] for pair in heap]
        return result
        
        


        