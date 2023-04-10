import sys
from collections import deque
f = sys.stdin.readline
sys.setrecursionlimit(10**6)
N = int(f())
graph = [list(map(int,f().split())) for _ in range(N)]
dx=[0,1,-1,0]
dy=[1,0,0,-1]
distance = [[-1]*(N) for _ in range(N)]

def bfs(x,y):
    if distance[x][y]>=0:
        return distance[x][y]
    if distance[x][y]==-1:
        distance[x][y] = 1
        v = graph[x][y]
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<N and graph[nx][ny]>v:
                distance[x][y] = max(bfs(nx,ny),distance[x][y])
    return distance[x][y]

answer = 0

for i in range(N):
    for j in range(N):
        bfs(i,j)

for i in range(N):
    answer = max(answer,max(distance[i]))

print(answer)
