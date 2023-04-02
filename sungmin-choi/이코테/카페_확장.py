from collections import deque

def solution(menu, order, k):
    answer = 0
    
    i=0
    q=deque([])
    
    
    while i<len(order):
        cur = order[i]
        if len(q)==0:
            q.append(menu[cur])
        elif q[0]>k:
            q[0]-=k
            q.append(menu[cur])
        else:
            
            cur_k=k
            while cur_k>0 and q:
                time = q.popleft()
                if time<=cur_k:
                    cur_k-=time
                else:
                    time-=cur_k
                    cur_k=0
                    q.appendleft(time)
            q.append(menu[cur])
        i+=1
        answer=max(answer,len(q))
    return answer