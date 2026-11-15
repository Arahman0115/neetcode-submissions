class Solution:
    def searchMatrix(self, matrix, target):
        l,r = 0,len(matrix[0]) - 1
        row,col = 0,len(matrix) - 1
        while row <= col: 
            row_mid = (row+col) // 2
            col_mid = (l+r) // 2
            if matrix[row_mid][col_mid] == target: 
                return True
            elif matrix[row_mid][0] > target:
                col -= 1
            elif matrix[row_mid][-1] < target:
                row += 1
            else:
                while l <= r: 
                    mid = (l+r) // 2
                    if matrix[row_mid][mid] == target:
                        return True
                    elif matrix[row_mid][mid] > target:
                        r = mid - 1 
                    else:
                        l = mid + 1
                return False
        return False
