import math

def solution(s):
    answer = len(s)
    for i in range(0, math.ceil(len(s)/2)):
        ns = [s[j:j+i+1] for j in range(0, len(s), i+1)]
        
        k = 0
        cnt = 0
        cur = ns[0]
        cs = ''
        while k<len(ns):
            while k<len(ns) and cur == ns[k]:
                cnt +=1
                k +=1
            if cnt > 1:
                cs +=str(cnt)+cur
            else:
                cs +=cur
       
            cnt = 0
            if k<len(ns):
                cur = ns[k] 
        if answer > len(cs):
            answer = len(cs)
    
    return answer

print(solution("aabbaccc"))