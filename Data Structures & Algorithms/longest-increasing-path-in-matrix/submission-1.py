class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        # rows and cols set up matric blank
        rows, cols = len(matrix), len(matrix[0])
        # set up memoization
        memo = [[0] * cols for column in range(rows)]
        # directions we can step
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        def dfs(r, c):
            """
            depth first search to bet longest path 
            """
            if memo[r][c]:
                ''' if this is it collapse recursion and return '''
                return memo[r][c]
            # best so far
            best = 1
            for dr, dc in directions:
                ''' 
                in each direction go and check against best and see if it increases 
                if yes add
                '''
                nr, nc = r + dr, c + dc
                if (0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]):
                    best = max(best, 1 + dfs(nr, nc))
            # memoize best
            memo[r][c] = best
            return best
        # begin path at 0
        path = 0
        for r in range(rows):
            '''
            accumulate the path
            '''
            for c in range(cols):
                path = max(path, dfs(r, c))
        return path