import copy
from heapq import heappush, heappop
arr=[]

def recur(count,emoticons,cur_arr):
    if count==len(emoticons):
        arr.append(cur_arr)
        return
    discount10=copy.deepcopy(cur_arr)
    discount10.append((emoticons[count],10))
    recur(count+1,emoticons,discount10)
    discount20=copy.deepcopy(cur_arr)
    discount20.append((emoticons[count],20))
    recur(count+1,emoticons,discount20)
    discount30=copy.deepcopy(cur_arr)
    discount30.append((emoticons[count],30))
    recur(count+1,emoticons,discount30)
    discount40=copy.deepcopy(cur_arr)
    discount40.append((emoticons[count],40))
    recur(count+1,emoticons,discount40)


def solution(users, emoticons):
    answer = []
    recur(0,emoticons,[])
    for items in arr:
        member_cnt=0
        total_money=0
        for user in users:
            user_disc, user_money = user
            user_use=0
            for item in items:
                price, disc = item
                if disc>=user_disc:
                    user_use+=int(price*0.01*(100-disc))
            if user_use>=user_money:
                member_cnt+=1
            else:
                total_money+=user_use
            heappush(answer,(-member_cnt,-total_money))
            
    result = list(map(abs,list(heappop(answer))))
    return result