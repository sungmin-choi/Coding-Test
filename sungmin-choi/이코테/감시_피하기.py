from itertools import combinations


n = int(input())

board = []


for i in range(n):
    board.append(list(input().split()))





def initBoard(n,board):
    graph = []
    for i in range(n):
        arr = []
        for j in range(n):
            arr.append(board[i][j])
        graph.append(arr)

    return graph

def bfs(n,graph, teachers):
    dx = [0,1,-1,0]
    dy = [1,0,0,-1]

    for pos in teachers:
        for i in range(4):
            x,y = pos
            flag = True
            while flag:
                nx = dx[i]+x
                ny = dy[i]+y
                if nx >=0 and nx<n and ny >=0 and ny<n:
                    if graph[nx][ny] == 'X' or graph[nx][ny] == 'S' or graph[nx][ny] == 'T':
                        graph[nx][ny] = 'T'
                        x = nx
                        y = ny
                    else:
                        flag = False
                else:
                    flag = False 
        
        
def solution(n, board): 
    students = []
    teachers = []
    extra = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'X' :
                extra.append((i,j))
            if board[i][j] == 'S':
                students.append((i,j))
            if board[i][j] == 'T':
                teachers.append((i,j))
    
    blocks = list(combinations(extra, 3))

    for block_list in blocks:
        s_cnt = 0
        graph = initBoard(n, board)
        for block_pos in list(block_list):
            x,y = block_pos
            graph[x][y] = 'O'
        bfs(n,graph, teachers)
        
        for arr in graph:
            s_cnt = s_cnt + arr.count('S')
        
        if s_cnt == len(students):
            return 'YES'
        
    return 'NO'

      




   


print(solution(n, board))