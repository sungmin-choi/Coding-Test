import sys
from collections import deque
def input(): return sys.stdin.readline().strip()

N,L,R =   list(map(int,input().split()))


graph = []

dx=[0,1,-1,0]
dy=[1,0,0,-1]


graph = [list(map(int, input().split())) for _ in range(N)]


def dfs(q, visited, cnt):
    united = []
    while q:
        x,y = q.popleft()
        united.append((x,y))
        visited[x][y] = cnt
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < N and 0<= ny < N and visited[nx][ny] == -1 and L <= abs(graph[x][y] - graph[nx][ny]) <=R:
                q.append((nx,ny))
    
    total = 0
    count = 0
    for x,y in united:
        total +=graph[x][y]
        count +=1
    
    next_num = total//count

    for x,y in united:
        graph[x][y] = next_num


def process():
    result = 0
    flag = True
    while flag:
        visited = [[-1] * N for _ in range(N)]
        cnt = 1
        flag = False
        for i in range(N):
            for j in range(N):
                if visited[i][j] == -1:
                    for k in range(4):
                        nx, ny = i+dx[k], j+dy[k]
                        if 0 <= nx < N and 0<= ny < N and visited[nx][ny] == -1 and L <= abs(graph[i][j] - graph[nx][ny]) <=R:
                                q = deque([(i,j)])
                                dfs(q,visited,cnt)
                                cnt +=1
                                flag = True
        if flag:
            result +=1
        
    print(result)

process()
                

                        


    


                    


    