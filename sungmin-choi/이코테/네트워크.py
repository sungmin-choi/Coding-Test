from collections import deque
def solution(n, computers):    
    visited = [False] * (n)
    
    cnt = 0
    
    for i in range(n):
        if visited[i]:
            continue
        else:
            q = deque([i])
            visited[i] = True
            cnt +=1 
            while q:
                curNode = q.popleft()
                for j in range(n):
                        if visited[j] == False and computers[curNode][j] == 1:
                            q.append(j)
                            visited[j] = True
                
    return cnt