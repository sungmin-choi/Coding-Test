import copy

N,M = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(N)]


actions = [list(map(int, input().split())) for _ in range(M)]

# 구름 한점이 방향(type)으로 1칸 이동 후 위치 구하는 함수
def getMovePos(type,x,y,N):
    nx,ny=0,0
    if type==1:
        nx=x
        if y==0:
            ny=N-1
        else:
            ny=y-1
    if type==2:
        if x==0:
            nx=N-1
        else:
            nx=x-1
        if y==0:
            ny=N-1
        else:
            ny=y-1
    if type==3:
        ny=y
        if x==0:
            nx=N-1
        else:
            nx=x-1
    if type==4:
        if x==0:
            nx=N-1
        else:
            nx=x-1
        if y==N-1:
            ny=0
        else:
            ny=y+1
    if type==5:
        nx=x
        if y==N-1:
            ny=0
        else:
            ny=y+1
    if type==6:
        if x==N-1:
            nx=0
        else:
            nx=x+1
        if y==N-1:
            ny=0
        else:
            ny=y+1
    if type==7:
        ny=y
        if x==N-1:
            nx=0
        else:
            nx=x+1
    if type==8:
        if x==N-1:
            nx=0
        else:
            nx=x+1
        if y==0:
            ny=N-1
        else:
            ny=y-1
    return nx,ny

clouds = [(N-1,0),(N-1,1),(N-2,0),(N-2,1)]


# 구름이 이동후 위치 구하는 함수
def getNextClouds(type, step, clouds, N):
    for _ in range(step):
        n_clouds = []
        for cloud in clouds:
            cx,cy = cloud
            nx,ny = getMovePos(type,cx,cy,N)
            n_clouds.append((nx,ny))
        clouds = n_clouds
    return clouds


def copyWaterBug(x,y,N,graph):
    dir4 = [(x-1,y-1),(x-1,y+1),(x+1,y-1),(x+1,y+1)]
    for dir in dir4:
        cx,cy = dir
        if cx >=0 and cx<N and cy >=0 and cy<N:
            if graph[cx][cy] >0:
                graph[x][y] +=1

            
def getNewClouds(graph,c_graph):
    n_clouds =[]
    for i in range(len(graph)):
        for j in range(len(graph)):
            if c_graph[i][j] >=2:
                graph[i][j] -=2
                n_clouds.append((i,j))
    return n_clouds



for action in actions:
    type, step = action
    cur_clouds = getNextClouds(type, step, clouds, N)
    for cur_cloud in cur_clouds:
        x,y = cur_cloud
        graph[x][y] +=1
    for cur_cloud in cur_clouds:
        x,y = cur_cloud
        copyWaterBug(x,y,N,graph)
    # 기존 전에 클라우드 체크하기 위한 c_graph
    c_graph = copy.deepcopy(graph)
    for cur_cloud in cur_clouds:
        x,y = cur_cloud
        c_graph[x][y]=0
    clouds = getNewClouds(graph,c_graph)


answer=0

for i in range(N):
    for j in range(N):
        answer +=graph[i][j]

print(answer)




            
        

