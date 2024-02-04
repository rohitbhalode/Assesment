def searchMatrix( matrix, target) -> bool:
    # Approach 2024.01.20
    row = len(matrix)
    col = len(matrix[0])
    l = 0
    r = row * col - 1
    while l <= r:
        m = (r - l) // 2 + l
        _r = m // col
        _c = m % col
        mv = matrix[_r][_c]
        if target < mv:
            r = m - 1
        elif target > mv:
            l = m + 1
        else:
            return True
    return False
    
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(searchMatrix(matrix,target))
