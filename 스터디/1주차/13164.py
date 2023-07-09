import sys
read = lambda: sys.stdin.readline().rstrip()

N,M = map(int, input().split())
arr = list(map(int, read().split()))


spends = []

for i in range(N-1):
    spends.append(arr[i+1]-arr[i])

spends.sort()

print(sum(spends[0:N-M]))

