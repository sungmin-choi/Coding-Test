from heapq import heappush, heappop

def solution(tickets):
    answer = []
    ticket_dict = dict()
    for start, end in tickets:
        if start not in ticket_dict:
            heap = []
            heappush(heap, end)
            ticket_dict[start] = heap
        else:
            heappush(ticket_dict[start], end)
    
    cur = heappop(ticket_dict['ICN'])
    answer = ['ICN', cur]
    while cur:
        if cur in ticket_dict:
            if len(ticket_dict[cur]) >0:
                cur = heappop(ticket_dict[cur])
                answer.append(cur)
            else:
                cur = False
        else:
            cur = False
        
    return answer


print(solution([["ICN", "AAA"], ["ICN", "CCC"], ["CCC", "DDD"], ["AAA", "BBB"], ["AAA", "BBB"], ["DDD", "ICN"], ["BBB", "AAA"]]))