from collections import deque

def solution(numbers, target):
    answer = []
    q = deque([(numbers[0], 0), (-numbers[0], 0)])
    while q:
        cost, cnt = q.popleft()
        if cnt == len(numbers)-1:
            answer.append(cost)
        else:
            cnt = cnt+1
            q.append((cost + numbers[cnt], cnt))
            q.append((cost - numbers[cnt], cnt))


        
    return answer.count(target)