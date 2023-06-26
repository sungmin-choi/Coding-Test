N=int(input())

b_values=[0]*(N+1)

graph = [[] for _ in range(N+1)]

INF=int(1e9)

print(graph)
dp = [[INF]*(N+1)]
for i in range(1,N+1):
    arr = list(map(int,input().split()))
    value = arr[0]
    nodes = arr[1:-1]
    b_values[i]=value
    graph[i]=(i,nodes)


graph.sort()


print(graph)


# for i in range(1,N+1):




