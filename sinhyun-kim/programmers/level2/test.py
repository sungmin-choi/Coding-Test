def solution(progresses, speeds):
    n = len(progresses)
    answer=[]
    import math
    from collections import deque
    
    progresses = deque(progresses)
    speeds = deque(speeds)
    total_time = deque([])
    left_time = 0
    while progresses:
        p = progresses.popleft()
        print()
        s = speeds.popleft()
        print(f"p={p} ; progresses={progresses} ; answer={answer}")
        t_answer = 1
        left_time += math.ceil((100-p)//s)
        for i in range(len(progresses)):
            progresses[i] += left_time*speeds[i]

        if(p >= 100):
            while len(progresses)>0 and progresses[0] >= 100:
                print(f"t_answer={t_answer}")
                p = progresses.popleft()
                print(f"t_answer={progresses[0]}")
                speeds.popleft()
                t_answer += 1
        answer.append(t_answer)
    
    return answer

# temp = solution([93, 30, 55],[1, 30, 5])
temp = solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1])
print(temp)