N = int(input())

tasks = [list(map(int,input().split())) for _ in range(N)]

dp = [0] * (N+1)

t, p =  tasks[N-1]

for i in range(N-2, -1, -1):

    t, p = tasks[i]
    if i+t<=N:
         dp[i]=max(dp[i+1], dp[i+t] + p)
    else:
        dp[i]=dp[i+1]
    

print(dp[0])
 

        

