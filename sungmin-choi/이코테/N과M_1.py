from itertools import permutations


N,M = map(int,input().split())


numbers = [i for i in range(1,N+1)]

answers = list(permutations(numbers,M))

for answer in answers:
    s = ''
    for a in list(answer):
        s +=str(a)+' '
    print(s[0:len(s)-1])
