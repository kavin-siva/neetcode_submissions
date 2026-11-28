class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        first_row_zero = False

        # 1. Mark rows and columns that need to be zeroed
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        first_row_zero = True

        # 2. Zero out inner cells based on markers
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # 3. Zero out the first column if needed
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0

        # 4. Zero out the first row if needed
        if first_row_zero:
            for c in range(COLS):
                matrix[0][c] = 0

        
        