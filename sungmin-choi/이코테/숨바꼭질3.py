from heapq import heappop, heappush

N,K = map(int, input().split())


INF = int(1e9)

visited = [False] * 100001

distance = [INF] * 100001

distance[N] = 0

q=[]

heappush(q,(0,N))

while q:
    dis,node =  heappop(q)
    visited[node] = True
    if node-1>=0 and visited[node-1]==False:
        if distance[node-1] > dis+1:
            heappush(q,(dis+1,node-1))
            distance[node-1]=dis+1
    if node+1<=100000 and visited[node+1]==False:
        if distance[node+1] > dis+1:
            heappush(q,(dis+1,node+1))
            distance[node+1]=dis+1
    if node*2<=100000 and visited[node*2]==False:
        if distance[node*2] > dis:
            heappush(q,(dis,node*2))
            distance[node*2] = dis

        
print(distance[K])












