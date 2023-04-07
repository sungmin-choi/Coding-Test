
N,K = map(int,input().split())

coins = [int(input()) for _ in range(N)]

INF = int(1e9)

dp = [INF] *  (K+1)


dp[0]=0
# 여기서 처음 동전 초기화하면 안됨
# K값이 몇인지 모르기떄문에



for coin in coins:
    for i in range(coin,K+1):
        dp[i] = min(dp[i-coin]+1, dp[i])


# for i in range(1, K+1):
#     for coin in coins:
#         if i == coin:
#             dp[coin]=1
#         elif i+coin<=K:
#             dp[i+coin] = min(dp[i+coin], dp[i]+1)



if dp[K]==INF: print(-1)
else: print(dp[K])