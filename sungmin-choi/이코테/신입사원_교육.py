from heapq import heappush,heappop

def solution(ability, number):
    answer = 0
    hq=[]
    for score in ability:
        heappush(hq,score)
    
    for i in range(number):
        stu1=heappop(hq)
        stu2=heappop(hq)
        total_score = stu1+stu2
        heappush(hq,total_score)
        heappush(hq,total_score)
    
    for i in hq:
        answer +=i
        
    return answer