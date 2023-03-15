def solution(n, build_frame):
    answer = [[]]
    board = [['null']*(n+1) for _ in range(n+1)]
    board[n] = ['x'] * (n+1)
    
    for [x,y,a,b] in build_frame:
        [i,j] = [abs(y-n),x]
        
        
    
    return answer