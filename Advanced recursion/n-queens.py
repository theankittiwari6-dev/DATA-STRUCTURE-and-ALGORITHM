# brute force 



class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        result = []
        board = [["."]*n for _ in range(n)]
        
        def isSafe (row, coloum):
            r = row -1
            c = coloum -1
            while r>=0 and c>=0:
                if board[r][c] == "Q":
                    return False
                r -= 1
                c -= 1  
            c = coloum-1
            while c>=0:
                if board[row][c] == "Q":
                    return False
                c -=1
            r = row + 1
            c = coloum -1
            while r < n and c >= 0:
                if board[r][c] == "Q":
                    return False
                r +=1
                c -=1
            return True
        
        
        def backtrack(coloum):
            if coloum == n:
                result.append(["".join(r) for r in board])
                return
            for row in range(n):
                if isSafe(row,coloum):
                    board[row][coloum] = "Q"
                    backtrack(coloum + 1)
                    board[row][coloum] = "."
        
        backtrack(0)
        return result




# optimal solution 

class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        result = []
        board = [["."]*n for _ in range(n)]
        left_row = [0]*n
        upper_digonal = [0]*(2*n-1)
        lower_digonal = [0]*(2*n-1)
        def backtrack(coloum):
            if coloum == n:
                result.append(["".join(r) for r in board])
                return
            for row in range(n):
                if (
                    left_row[row] == 0
                    and lower_digonal[row + coloum] == 0
                    and upper_digonal[(n-1)+(coloum-row)] == 0
                ):
                    board[row][coloum] = "Q"
                    left_row[row] = 1
                    lower_digonal[row + coloum] = 1
                    upper_digonal[(n-1)+(coloum-row)] = 1
                    backtrack(coloum+1)
                    board[row][coloum] = "."
                    left_row[row] = 0
                    lower_digonal[row + coloum] = 0
                    upper_digonal[(n-1)+(coloum-row)] = 0
        
        backtrack(0)
        return result
