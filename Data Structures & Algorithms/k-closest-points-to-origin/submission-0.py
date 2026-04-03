class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []

        heapq.heapify(heap)

        distance = {}

        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            d = math.sqrt(x**2 + y**2)
            heapq.heappush(heap, (-d, x, y))

            while len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for d, x, y in heap:
            res.append([x, y])

        return res
            
        


        


