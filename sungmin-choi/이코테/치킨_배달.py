from itertools import combinations

n=5
m=1

graph = [[1,2,0,2,1],[1,2,0,2,1],[1,2,0,2,1],[1,2,0,2,1],[1,2,0,2,1]]

homesPos = []
chickensPos = []
answer = int(1e9)

for i in range(n):
    for j in range(n):
        if graph[i][j] ==1 :
            homesPos.append((i,j))
        if graph[i][j] ==2 :
            chickensPos.append((i,j))


chickens = list(combinations(chickensPos, m))

for arr in chickens:
    totalDistance = 0
    for hx,hy in homesPos:
        homeDistance = int(1e9)
        for cx, cy in list(arr):
            distance = abs(cx-hx) + abs(cy-hy)
            homeDistance = min(homeDistance, distance)
        totalDistance +=homeDistance
    answer = min(totalDistance, answer)
        
print(answer)


    

