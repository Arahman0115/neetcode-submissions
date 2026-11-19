class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t,b = 0, len(matrix) - 1
        l,r = 0,len(matrix[0]) - 1
        while t <=b: 
            mid = (t+b) // 2
            if matrix[mid][l] == target or matrix[mid][r] == target: 
                return True
            elif target < matrix[mid][0]:
                b = mid - 1
            elif target > matrix[mid][-1]:
                t = mid + 1
            else:
                while l <= r: 
                    m = (l+r) // 2
                    if matrix[mid][m] == target:
                        return True
                    elif matrix[mid][m] < target: 
                        l = m + 1
                    else:
                        r = m - 1
                return False
        return False
