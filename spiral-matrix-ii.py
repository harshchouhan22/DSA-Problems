class Solution(object):
    def generateMatrix(self, n):
        matrix = [[0] * n for _ in range(n)]
        left, right, top, bottom = 0, n-1, 0 , n - 1
        num = 1
   # Iterate until all elements in the matrix are filled
        while num <= n * n:
            #Fill the top row of the matrix
            for i in range(left, right + 1):
                matrix[top][i] = num
                num += 1
            top += 1

            #Fill the rightmost columns of the matrix
            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += 1
            right -= 1

            #Fill the bottom most row of the matrix 
            for i in range(right, left - 1, - 1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1

            #fill the leftmost column of the matrix
            for i in range(bottom, top -1, - 1):
                matrix[i][left] = num
                num += 1
            left += 1
        return matrix

        
n = 5
result = Solution().generateMatrix(n)
print(result)

