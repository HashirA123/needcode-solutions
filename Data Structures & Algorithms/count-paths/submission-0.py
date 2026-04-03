class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # two choices, go left, go down, recursively check all branches of tree?
        # how would bottom up work?

        # 2d array to store number of paths at position [i][j]

        arr = [[0 for j in range(n+1)] for i in range(m+1)] # +1 so you dont get out
                                                            # of bounds error
        arr[m-1][n-1] = 1

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                arr[i][j] += arr[i+1][j] + arr[i][j+1]
        
        return arr[0][0]