class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
       
        first_row,last_row = 0,len(matrix) - 1
        while first_row <= last_row: 
            mid_matrix = (first_row + last_row) // 2
            if matrix[mid_matrix][0] > target:
                last_row = mid_matrix - 1
            elif matrix[mid_matrix][-1] < target:
                first_row = mid_matrix + 1
            else:
                first,last = 0, len(matrix[0]) - 1 
                while first <= last: 
                    mid = (first+last) // 2
                    if matrix[mid_matrix][mid] == target:
                         return True
                    elif matrix[mid_matrix][mid] < target:
                        first = mid + 1
                    elif matrix[mid_matrix][mid] > target:
                        last = mid - 1
                return False
            
        return False

            
