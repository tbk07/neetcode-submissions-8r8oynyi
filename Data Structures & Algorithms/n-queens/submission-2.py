class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        col = set() 
        posdig = set()
        negdig = set()
        board = [["."] * n for _ in range(n)]
        def backtracking(r):
            if r == n:
                copy = [''.join(row) for row in board]
                res.append(copy)
                return 
            for c in range(n):
                if c in col or (r + c) in posdig or (r-c) in negdig:
                    continue
                
                col.add(c)
                posdig.add(r+c)
                negdig.add(r-c)
                board[r][c] = "Q"

                backtracking(r + 1)

                col.remove(c)
                posdig.remove(r+c)
                negdig.remove(r-c)
                board[r][c] = "."

        backtracking(0)
        return res


            



                
               
            
        