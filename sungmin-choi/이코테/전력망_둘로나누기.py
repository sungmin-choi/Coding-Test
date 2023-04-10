from collections import deque

def bfs(a,b,n,graph):
    
    visited=[False]*(n+1)
    q=deque([a])
    count=0
    visited[a]=True
    while q:
        node=q.popleft()
        count+=1
        for cnt_node in graph[node]:
            if cnt_node!=b and visited[cnt_node]==False:
                visited[cnt_node] = True
                q.append(cnt_node)
    return count
                
        
    
    


def solution(n, wires):
    answer = n+1
    
    graph=[[] for _ in range(n+1)]
    
    
    for a,b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    for a,b in wires:
        count1=bfs(a,b,n,graph)
        count2=bfs(b,a,n,graph)
        answer = min(answer,abs(count1-count2))        
    
    return answer