
from collections import deque

dx=[-1,1,0,0]
dy=[0,0,1,-1]

def bfs(y,x,graph,distance):
    q=deque([(y,x)])
    distance[y][x] = 0
    while q:
        cy,cx=q.popleft()
        for i in range(4):
            ny,nx=cy+dy[i],cx+dx[i]
            if 0<=ny<=100 and 0<=nx<=100:
                if graph[ny][nx]=='W':
                    if distance[ny][nx] > distance[cy][cx]+1:
                        distance[ny][nx] = distance[cy][cx]+1
                        q.append((ny,nx))

    
    
    
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    INF = int(1e9)
    graph = [['X']*102 for _ in range(102)]
    distance = [[INF]*102 for _ in range(102)]
    for x1,y1,x2,y2 in rectangle:
        for i in range(y1*2,y2*2+1):
            for j in range(x1*2,x2*2+1):
                if i==y1*2 or i==y2*2 or j==x1*2 or j==x2*2:
                    if graph[i][j]=='X':
                        graph[i][j]='W'
                else:
                    graph[i][j]='R'
                    
    bfs(characterY*2,characterX*2,graph,distance)
    
    return distance[itemY*2][itemX*2]//2