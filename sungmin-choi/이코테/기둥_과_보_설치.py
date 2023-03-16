Pillow = []
Bar = []

def checkPillow(x,y):
    if y == 0 or Pillow[x][y-1]:
        return True
    if Bar[x][y] or (x>0 and Bar[x-1][y]):
        return True
    return False

def checkBar(x,y):
    if Pillow[x][y-1] or Pillow[x+1][y-1]:
        return True
    if (x>0 and Bar[x-1][y]) and Bar[x+1][y]:
        return True
    return False

def canCancel(x,y):
    for i in range(x-1,x+2):
        for j in range(y, y+2):
            if Pillow[i][j] and checkPillow(i,j) == False:
                return False
            if Bar[i][j] and checkBar(i,j) == False:
                return False
    return True
      

def solution(n, build_frame):
    answer = []
    global Pillow, Bar
    Pillow =  [[0 for _ in range(n+2)] for _ in range(n+2)]
    Bar = [[0 for _  in range(n+2)] for _ in range(n+2)]
    for x,y,a,b in build_frame:
        if b == 1:
            if a == 0 and checkPillow(x,y):
                Pillow[x][y] = 1
            elif a== 1 and checkBar(x,y):
                Bar[x][y] = 1
        elif b==0:
            if a==0:
                Pillow[x][y] = 0
                if not canCancel(x,y):
                    Pillow[x][y] = 1
            elif a==1:
                Bar[x][y] = 0
                if not canCancel(x,y):
                    Bar[x][y] = 1
    
    for i in range(n+2):
        for j in range(n+2):
            if Pillow[i][j]:
                answer.append([i,j,0])
            if Bar[i][j]:
                answer.append([i,j,1])
    
    return answer