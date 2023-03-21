from collections import deque

game_board = [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]
table = [[1,0,0,1,1,0],
         [1,0,1,0,1,0],
         [0,1,1,0,1,1],
         [0,0,1,0,0,0],
         [1,1,0,1,1,0],
         [0,1,0,0,0,0]]


def bfs(graph, table, x, y, t):
    dx = [0,1,-1,0]
    dy = [-1,0,0,1]
    result = []
    q = deque([(x,y)])
    min_x = x
    min_y = y
    max_x = 0
    max_y = 0
    blocks_pos = [(x,y)]
    while q:
        x, y = q.popleft()
        graph[x][y] = abs(t-1)
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if (nx >=0 and nx < len(table)) and (ny >= 0 and ny<len(table)):
                if graph[nx][ny] == t:
                    min_x = min(min_x, nx)
                    min_y = min(min_y, ny)
                    blocks_pos.append((nx,ny))
                    q.append((nx,ny))
    for i in range(len(blocks_pos)):
        c_x,c_y = blocks_pos[i]
        result.append((c_x - min_x, c_y - min_y))
    
    return result


def getBlock(table, t):
    graph = [[abs(t-1)]*len(table) for _ in range(len(table))]
    for i in range(len(table)):
        for j in range(len(table)):
            graph[i][j] = table[i][j]
    
    blocks = []


    for i in range(len(table)):
        for j in range(len(table)):
            if graph[i][j] ==t:
               blocks.append(bfs(graph,table,i,j, t))
    return blocks





def solution(game_board, table):
    blocks =  getBlock(table, 1)  
    boards = getBlock(game_board, 0)



    print(boards)


solution(game_board, table)