N, M =map(int,input().split())


INF = int(10)

graph = [[INF] * (N+1) for _ in range(N+1)]

answer =0

mid = (N+1)/2

for i in range(M):
    a,b=map(int,input().split())
    graph[a][b]=1
    graph[b][a]=-1


for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if graph[i][j] == INF and graph[i][k] !=INF and graph[k][j] !=INF:
                pare = graph[i][k] + graph[k][j]
                if pare==2:
                    graph[i][j] = 1
                    graph[j][i] = -1
                elif pare==-2:
                    graph[i][j] = -1
                    graph[j][i] = 1


for arr in graph:
    h= arr.count(1)
    l= arr.count(-1)
    if h>=mid or l>=mid:
        answer+=1

print(answer)

                