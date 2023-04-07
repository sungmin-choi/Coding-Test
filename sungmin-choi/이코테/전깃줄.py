import bisect

N = int(input())

w=[]
w_b=[]


for i in range(N):
    w.append(list(map(int,input().split())))

w.sort(key=lambda x:x[0])

for i in range(N):
    w_b.append(w[i][1])

dp = [w_b[0]]


for i in range(N):
    if w_b[i] > dp[-1]:
        dp.append(w_b[i])
    else:
        index = bisect.bisect_left(dp,w_b[i])
        dp[index] = w_b[i]

print(N-len(dp))
    

        
             