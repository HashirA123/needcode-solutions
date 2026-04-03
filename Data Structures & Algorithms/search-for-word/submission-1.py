class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(i, j, counter, visited):
            if counter >= len(word):
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return False
            if (i, j) in visited:
                return False
            if board[i][j] != word[counter]:
                return False
            visited[(i, j)] = True
            res = (dfs(i+1, j, counter+1, visited) or
                    dfs(i, j+1, counter+1, visited) or
                    dfs(i-1, j, counter+1, visited) or
                    dfs(i, j-1, counter+1, visited))
            # you have to remove the visited node, thats what i missed
            visited.pop((i,j))
            return res
        

        for i in range(len(board)):
            for j in range(len(board[i])):
                if dfs(i, j, 0, {}):
                    return True
        
        return False