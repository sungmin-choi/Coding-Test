N,M = map(int,input().split())

DNA_list = [list(input()) for _ in range(N)]

answer = ''
hd_total=0
for i in range(M):
    alpha = ''
    count = 0
    col=[]
    for j in range(N):
        col.append(DNA_list[j][i])
    
    set_list = list(set(col))
    set_list.sort()
    for v in set_list:
        cur_cnt = col.count(v)
        if cur_cnt > count:
            alpha = v
            count=cur_cnt
    answer +=alpha


for l in DNA_list:
    for i in range(M):
        if l[i] != answer[i]:
            hd_total +=1

print(answer)
print(hd_total)






