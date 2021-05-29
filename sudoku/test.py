def func(grid):
    N = 9


    def printing(arr):
        ans = []
        for i in range(N):
            ans.append([])
            for j in range(N):
                ans[i].append(arr[i][j])
        return ans


    def isSafe(grid, row, col, num):
        for x in range(9):
            if grid[row][x] == num:
                return False

        for x in range(9):
            if grid[x][col] == num:
                return False
        startRow = row - row % 3
        startCol = col - col % 3
        for i in range(3):
            for j in range(3):
                if grid[i + startRow][j + startCol] == num:
                    return False
        return True


    def solveSuduko(grid, row, col):
        if row == N - 1 and col == N:
            return True
        if col == N:
            row += 1
            col = 0
        if grid[row][col] > 0:
            return solveSuduko(grid, row, col + 1)
        for num in range(1, N + 1, 1):
            if isSafe(grid, row, col, num):
                grid[row][col] = num

                if solveSuduko(grid, row, col + 1):
                    return True

            grid[row][col] = 0
        return False
    if solveSuduko(grid, 0, 0):
        a = printing(grid)
        return a
    return 'No'
