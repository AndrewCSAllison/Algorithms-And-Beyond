def searchMatrix(self, matrix, target):    
    m = len(matrix)
    n = len(matrix[0])
    low = 0
    high = m * n - 1
    while (low <= high):
        mid = (low + high) // 2
        row = mid // n
        col = mid % n
        midVal = matrix[row][col]
        if midVal < target:
            low += 1
        elif midVal > target:
            high -= 1
        else:
            return True
    return False

def main():
    matrix = [
      [1,   3,  5,  7],
      [10, 11, 16, 20],
      [23, 30, 34, 50]
    ]
    target = 3
    print(searchMatrix(None, matrix, target), matrix, "Target = " + str(target))
    target = 18
    print(searchMatrix(None, matrix, target), matrix, "Target = " + str(target))
    target = 34
    print(searchMatrix(None, matrix, target), matrix, "Target = " + str(target))
main()