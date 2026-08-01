class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        :type n: int
        :rtype: List[List[str]]
        """
        # set up  blank board
        board = [["." for _ in range(n)] for _ in range(n)]
        # set result here
        result = []
        # set up col thread
        columns = set()
        # diag threats 1
        diagonal1 = set() 
        # diag threat 2  
        diagonal2 = set()   
        def backtrack(row):
            """
            for a given row check and backtrack and place
            """
            if row == n:
                '''
                collapse recursion if we hit end
                '''
                result.append(["".join(rw) for rw in board])
                return

            for column in range(n):
                '''
                for each col item check if the square is being yeeted 
                if it is jump if not place queen check if it attacks 
                and if it is backtrack
                '''
                if (column in columns or (row - column) in diagonal1 or (row +                                                             column) in diagonal2):
                    continue
                board[row][column] = "Q"
                columns.add(column)
                diagonal1.add(row - column)
                diagonal2.add(row + column)
                backtrack(row + 1)
                board[row][column] = "."
                columns.remove(column)
                diagonal1.remove(row - column)
                diagonal2.remove(row + column)
        # do backtracked placing
        backtrack(0)
        return result         