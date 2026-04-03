class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = [0]*(n+1)

        for i in range(n+1):
            j = i
            while j > 0:
                arr[i] += (j & 1)
                j >>= 1
        
        return arr
