from  heapq import heappush, heappop


dir = [[1,2],[1,3],[2,3],[2,4]]

INF = int(1e9)

def solution(n,m,k,x,dir):
    answer = []
    distance = [INF] * (n+1)
    graph = [[] for _ in range(n+1)]

    for start, end in dir:
        graph[start].append((1,end))
    
    q = []
    heappush(q, (0, x))
    distance[x] = 0
    while q:
        c, s = heappop(q)
        for cost, end in graph[s]:
            cost = cost +c
            if distance[end] < cost:
                continue
            else:
                distance[end] = cost
                heappush(q,(cost, end))
    
    for i in range(n+1):
        if distance[i] == k:
            answer.append(i)
    
    answer.sort()

    print(answer)





solution(4,4,2,1,dir)



     

