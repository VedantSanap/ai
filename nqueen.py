N = int(input("Enter the value of N: "))

def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()

def isSafe(board, row, col):
    
    for i in range(col):
        if board[row][i] == 1:
            return False
    
   
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    
  
    i = row
    j = col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1
    
    return True

def solveNQueensUtil(board, col, solutionCount):
    if col >= N:
        solutionCount[0] += 1
        print("Solution", solutionCount[0])
        printSolution(board)
        print()
        return
    
    for i in range(N):
        if isSafe(board, i, col):
            board[i][col] = 1
            
            solveNQueensUtil(board, col + 1, solutionCount)
            
            board[i][col] = 0

def solveNQueens():
    board = [[0 for _ in range(N)] for _ in range(N)]
    
    solutionCount = [0]
    solveNQueensUtil(board, 0, solutionCount)
    
    print("Total solutions:", solutionCount[0])

solveNQueens()
