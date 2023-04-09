from collections import deque
import sys
f = sys.stdin.readline

N, M, K, X = map(int,f().split())
answers=[]
INF = int(1e9)
graph=[[] for _ in range(N+1)]
visited = [False] * (N+1)
distance = [INF] * (N+1)
for i in range(M):
    a,b = map(int,f().split())
    graph[a].append(b)

q=deque([X])

distance[X]=0


while q:
    node=q.popleft()
    visited[node]=True
    dis = distance[node]
    for i in graph[node]:
        if not visited[i]:
            visited[i]=True
            q.append(i)
            distance[i]=dis+1


for i in range(N+1):
    if distance[i]==K:
        answers.append(i)

if len(answers)==0:
    print(-1)
else:
    for i in answers:
        print(i)


        






    


     

