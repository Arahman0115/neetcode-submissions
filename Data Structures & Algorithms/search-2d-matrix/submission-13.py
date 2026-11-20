class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t,b = 0,len(matrix) - 1
        l,r = 0,len(matrix[0]) - 1

        while t <= b: 
            midCol = (t+b) // 2
            if matrix[midCol][-1] == target or matrix[midCol][0] == target:
                return True
            elif matrix[midCol][-1] < target:
                t  = midCol + 1
            elif matrix[midCol][0] > target:
                b = midCol - 1
            else:
                while l <= r:
                    mid = (l+r) // 2
                    if matrix[midCol][mid] == target:
                        return True
                    elif matrix[midCol][mid] > target:
                        r = mid - 1
                    else:
                        l = mid + 1 
                return False
        return False