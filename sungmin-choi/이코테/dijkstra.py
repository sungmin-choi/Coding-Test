from heapq import heapush, heappop



#간선 정보
dir = [[1,2],[1,3],[2,3],[2,4]]

# 노드 갯수
n = 5

# 무한 
INF = int(1e9)

# 시작 노드
x = 1

# 시작노드에서부터 모든 노드 까지의 거리를 무한으로 초기화
distance = [INF] * (n+1)

#graph 는 특정 노드에서 갈수 있는 노드와 거리를 저장하는 2*2배열
graph = [[] * (n+1)]
for start, end in dir:
        graph[start].append((1,end))




def dijkstra(x,distance,graph):
    q= []
    distance[x] = 0
    heapush(q,(0,x))

    while q:
        c , now = heappop(q)
        for cost, end in graph[now]:
            cost = cost + c
            if distance[end] < cost:
                continue
            else:
                distance[end] = cost
                heapush(q,(cost,end))
                
    #distance에 거리정보 저장됨