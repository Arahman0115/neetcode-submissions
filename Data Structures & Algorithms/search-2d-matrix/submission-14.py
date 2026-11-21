class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t,b = 0, len(matrix) - 1
        l,r = 0 ,len(matrix[0]) - 1
        while t <= b:
            midRow = (t+b) // 2
            if matrix[midRow][-1] == target or matrix[midRow][0] == target:
                return True
            elif  matrix[midRow][0] > target:
                b = midRow - 1
            elif  matrix[midRow][-1] < target:
                t = midRow + 1
            else:
                
                while l <=r : 
                    mid = (l+r) // 2
                    if matrix[midRow][mid] == target:
                        return True
                    elif matrix[midRow][mid] < target:
                        l = mid + 1
                    else:
                        r = mid - 1
                return False
        return False