N,M  = map(int, input().split())

coins = [ int(input())  for _ in range(N)]

INF = 10001

d = [INF] * (10001)




for i in coins:
    d[i] = 1


for i in range(1,10001):
    for j in coins:
        if i-j>0:
            d[i] = min(d[i-j]+1, d[i])


if d[M]==10001:
    print(-1)
else:
    print(d[M])






