gear1 = list(input())
gear2 = list(input())
gear3 = list(input())
gear4 = list(input())
N = int(input())


gears=[[],gear1,gear2,gear3,gear4]

steps = [list(map(int, list(input().split())))  for _ in range(N)]

answer = 0

def right(gear):
    n_gear = [0]
    n_gear.extend(gear[0:len(gear)-1])
    n_gear[0] = gear[-1]
    return n_gear

def left(gear):
    n_gear = gear[1:len(gear)]
    n_gear.append(gear[0])
    return n_gear




for i in range(len(steps)):
    [gear, arrow] = steps[i]
    
    gears_step = [0,0,0,0,0]

    gears_step[gear] = arrow

    if gear ==1:
        if gears[1][2] != gears[2][6]:
            gears_step[2] = -arrow
            if gears[2][2] != gears[3][6]:
                gears_step[3] = arrow
                if gears[3][2] != gears[4][6]:
                    gears_step[4] = -arrow
    if gear ==2:
        if gears[1][2] != gears[2][6]:
            gears_step[1] = -arrow
        if gears[3][6] != gears[2][2]:
            gears_step[3] = -arrow
            if gears[3][2] != gears[4][6]:
                gears_step[4] = arrow
    if gear ==3:
        if gears[2][2] != gears[3][6]:
            gears_step[2] = -arrow
            if gears[2][6] !=gears[1][2]:
                gears_step[1] = arrow
        if gears[3][2] != gears[4][6]:
            gears_step[4] = -arrow     
    if gear ==4:
          if gears[3][2] != gears[4][6]:
            gears_step[3] = -arrow
            if gears[3][6] != gears[2][2]:
                gears_step[2] = arrow
                if gears[2][6] != gears[1][2]:
                    gears_step[1] = -arrow
    for j in range(1,5):
        if gears_step[j] == 1:
            gears[j] = right(gears[j])

        if gears_step[j] == -1:
            gears[j] = left(gears[j])
   
    if i == len(steps)-1:
        for k in range(1,len(gears)):
            if gears[k][0] == '1':
                if k==1:
                    answer +=1
                if k==2:
                    answer +=2
                if k==3:
                    answer +=4
                if k==4:
                    answer +=8


print(answer)

