# https://www.acmicpc.net/problem/1717

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N, M = map(int, input().split())
parents = [i for i in range(N+1)]

# 작은 쪽에 union
def union(a,b):
    if (a == b):
        return
    elif (a<b):
        parents[b] = a
    else:
        parents[a] = b
        
def find_parent(a):
    if(parents[a] == a):
        return a
    else:
        return find_parent(parents[a])
        

answer = []
for i in range(M):
    op, a, b = map(int,input().split())
    if op == 0:
        union(a,b)
    else:
        if(find_parent(a) == find_parent(b)):
            answer.append("YES")
        else:
            answer.append("NO")

for i in answer:
    print(i)


# import sys 
# input = sys.stdin.readline

# N, M = map(int, input().split())
# sets = [set() for _ in range(N+1)]

# answer = []
# for i in range(M):
#     op, set1, set2 = map(int, input().split())
#     if (op == 0):
#         sets[set1] = sets[set1].union({set2})
#         sets[set2] = sets[set2].union({set1})
#     elif (op == 1):
#         if set2 in sets[set1]:
#             answer.append("YES")
#         else:
#             answer.append("NO")
            
# for i in answer:
#     print(i)