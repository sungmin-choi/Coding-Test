N = int(input())

d = [0] *(N+1)

l = 10007

d[1] = 1
d[2] = 3

for i in range(3,N+1):
    d[i]  = (d[i-1] + (d[i-2] *2)%l )%l


print(d[N])