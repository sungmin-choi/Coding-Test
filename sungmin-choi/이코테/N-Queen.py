import copy

N = int(input())


board = [[0]*N for i in range(N)]

answer = 0


def blockBoard(new_board, x, y):
    global N
    re_board =copy.deepcopy(new_board)
    for i in range(N):
        re_board[x][i] = 1
        re_board[i][y] = 1
        ax,ay = x-i, y-i
        if N>ax>=0 and N>ay>=0:
            re_board[ax][ay] = 1
        bx,by = x-i,y+i
        if N>bx>=0 and N>by>=0:
            re_board[bx][by] = 1
        cx,cy = x+i,y+i
        if N>cx>=0 and N>cy>=0:
            re_board[cx][cy] = 1
        dx,dy = x+i,y-i
        if N>dx>=0 and N>dy>=0:
            re_board[dx][dy] = 1
    
    return re_board


def BT(count, new_board):
    global answer
    global N
    if count == N:
        answer +=1
        return
    for i in range(N):
        for j in range(N):
            if new_board[i][j]==0:
                bt_board = blockBoard(new_board,i,j)
                print(bt_board)
                BT(count+1, bt_board)
 


BT(1,board)

print(answer)



                


