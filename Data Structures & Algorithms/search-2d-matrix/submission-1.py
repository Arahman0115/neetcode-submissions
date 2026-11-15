class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        Rows, Cols = len(matrix), len(matrix[0])
        top_row, bottom_row = 0, Rows - 1
        while top_row <= bottom_row:
            row = (top_row + bottom_row ) // 2
            if target > matrix[row][-1]:
                top_row  = row + 1
            elif target < matrix[row][0]:
                bottom_row = row - 1
            else:
                break
        if not (top_row <= bottom_row):
            return False
        row = (top_row + bottom_row ) // 2
        l, r = 0, Cols - 1
        while l <= r:
            mid = (l+r) // 2
            if target > matrix[row][mid]:
                l = mid + 1
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                return True
        return False
