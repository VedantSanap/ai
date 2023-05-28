N = int(input("enter the board size:"))


def printSolution(board):
    for i in range (N):
        for j in range (N):
            print (board[i][j],end=" ")
        print()



def isSafe(row,col,slashcode,backslashcode,rowlookup,slashcodelookup,backslashcodelookup):
    if(slashcodelookup[slashcode[row][col]] or
       backslashcodelookup[backslashcode[row][col]] or 
       rowlookup[row]):
        return False
    return True

def solvenqueensutil(board,col,slashcode,backslashcode,rowlookup,
                     slashcodelookup,backslashcodelookup,solutionCount):
    if col >=N :
        solutionCount[0] +=1
        print("solution",solutionCount[0])
        printSolution(board)
        print()
        return
    
    for i in range (N):
        if(isSafe(i,col,slashcode,backslashcode,rowlookup,slashcodelookup,backslashcodelookup)):
            board[i][col]=1
            rowlookup[i]=True
            slashcodelookup[slashcode[i][col]]=True
            backslashcodelookup[backslashcode[i][col]]=True
            
            solvenqueensutil(board,col+1,slashcode,backslashcode,rowlookup,slashcodelookup,backslashcodelookup,solutionCount)
            board[i][col]=0
            rowlookup[i]=False
            slashcodelookup[slashcode[i][col]]=False
            backslashcodelookup[backslashcode[i][col]]=False



def solvenqueen():
    board = [[0 for i in range(N)] for j in range (N)]
    
    slashcode = [[0 for i in range(N)] for j in range (N)]
    
    backslashcode = [[0 for i in range(N)] for j in range (N)]
    
    rowlookup = [False] * N
    
    x= 2*N-1
    
    slashcodelookup = [False]*x
    
    backslashcodelookup = [False]*x
    
    for rr in range(N):
        for cc in range(N):
            slashcode[rr][cc]=rr+cc
            backslashcode[rr][cc]=rr-cc+N-1
            
    solutionCount = [0]
    
    solvenqueensutil(board,0,slashcode,backslashcode,rowlookup,slashcodelookup,backslashcodelookup,solutionCount)
    
    print("total solution",solutionCount[0])
    
solvenqueen()
    
    
    