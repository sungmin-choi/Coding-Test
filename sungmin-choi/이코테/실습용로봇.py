def solution(command):
    answer = [0,0]
    cur_dir = 0
    arr = []
    dirs = [[0,1],[1,0],[0,-1],[-1,0]]
    for c in command:
        if c=='R':
            if cur_dir ==3:
                cur_dir=0
            else:
                cur_dir+=1
        if c=='L':
            if cur_dir ==0:
                cur_dir=3
            else:
                cur_dir-=1
        if c=='G':
            cx,cy=answer
            arr.append([cx,cy])
            answer =[cx+dirs[cur_dir][0], cy+dirs[cur_dir][1]]
        if c=='B':
            cx,cy=answer
            arr.append([cx,cy])
            answer =[cx-dirs[cur_dir][0], cy-dirs[cur_dir][1]]
            
    return answer