from collections import deque

N,L,R =   list(map(int,input().split()))


graph = []

for i in range(N):
    graph.append(list(map(int, input().split())))



 

def dfs(q, cnt, total, trans_arr, visited, graph):
    dx = [0,-1,0,1]
    dy = [1,0,-1,0]
    cnt = cnt
    total = total
    while q:
        x, y = q.popleft()
        visited[x][y] = True
        cnt +=1
        total +=graph[x][y]
        trans_arr.append((x,y))
        for k in range(4):
            nx,ny = x+dx[k], y+dy[k]
            if nx>=0 and nx<N and ny>=0 and ny<N:
                period = abs(graph[x][y] - graph[nx][ny])
                if (visited[nx][ny] ==False) and  (period >=L and period<=R):
                    q.append((nx,ny))
    return cnt, total
            


def solution(N, L,R, graph):
    dx = [0,-1,0,1]
    dy = [1,0,-1,0]
    result = 0
    
    flag = True

    while flag:
        flag = False
        visited = [[False]*N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if visited[i][j] == False:
                    arr = []
                    for k in range(4):
                        nx,ny = i+dx[k], j+dy[k]
                        if nx>=0 and nx<N and ny>=0 and ny<N:
                            period = abs(graph[i][j] - graph[nx][ny])
                            if  (visited[nx][ny] ==False) and  (period >=L and period<=R):
                                
                                flag = True
                                arr.append((nx,ny))
                    if len(arr) > 0:
                        trans_arr = [(i,j)]
                        total = graph[i][j]
                        cnt = 1
                        visited[i][j] = True
                        q = deque([])
                        for x, y in arr:
                            q.append((x,y))
                        cnt, total =  dfs(q, cnt, total, trans_arr, visited, graph)
                        a = int(total/cnt)
                        for cx,cy in trans_arr:
                            graph[cx][cy] = a
                        result +=1
    
    print(result)



solution(N,L,R,graph)

                    


    