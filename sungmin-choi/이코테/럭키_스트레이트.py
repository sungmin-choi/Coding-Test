# 1. 123402 => 1+2+3 == 4+0+2 스킬 사용 가능

def solution(n):
    N = str(n)
    half = (len(N)/2)
    left = 0
    right = 0
    for i in range(len(N)):
        if i < half:
            left = left + int(N[i])
        else:
            right = right + int(N[i])
    
    if left == right:
        print('LUCKY')
    else:
        print('READY')






    