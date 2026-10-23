class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        res = []

        for num in nums:
            count[num] = 1 + count.get(num, 0)




        heap = [(-freq, num) for num, freq in count.items()]
        heapq.heapify(heap)


        while heap and k != 0:

            res.append(heapq.heappop(heap)[1])
            k-=1

        return res



        