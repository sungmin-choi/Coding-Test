import sys
f = sys.stdin.readline



N,K = map(int,f().split())

products = [list(map(int,f().split())) for _ in range(N)]

dp = [[0]*(K+1) for _ in range(N+1)]


for i in range(1,N+1):
    w = products[i-1][0]
    v = products[i-1][1]
    for j in range(1,K+1):
        if j<w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)


print(dp[N][K])




