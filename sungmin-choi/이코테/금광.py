T = int(input())
result = []
for _ in range(T):
    N,M = map(int, input().split())
    arr = list(map(int,input().split()))
    graph = []
    dp = [[0]*(M) for _ in range(N)]
    for i in range(0,N*M,M):
        graph.append(arr[i:i+M])
    for i in range(N):
        dp[i][0] = graph[i][0]
    
    for m in range(1, M):
        for n in range(N):
            a = 0
            b = 0
            c = 0
            if n-1>=0: a=graph[n][m] + dp[n-1][m-1]
            b=graph[n][m] + dp[n][m-1]
            if n+1<N: c=graph[n][m] + dp[n+1][m-1]
            dp[n][m] = max(a,b,c)
    
    result.append(max(dp[i][m] for i in range(N)))

print(result)






        
    

    