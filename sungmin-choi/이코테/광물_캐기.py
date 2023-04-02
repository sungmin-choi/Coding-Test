
def solution(picks, minerals):
    answer = 0
    
    i=0
    arr =[]
    gok =picks[0]+picks[1]+picks[2]
    
    minerals=minerals[0:gok*5]
    
    while i+5<=len(minerals):
        split_minerals = minerals[i:i+5]
        d_cnt = split_minerals.count('diamond')
        i_cnt = split_minerals.count('iron')
        s_cnt = split_minerals.count('stone')
        
        arr.append((d_cnt*25+i_cnt*5+s_cnt*1, split_minerals))
            
        i +=5
    if i<=len(minerals):
        split_minerals = minerals[i:i+(len(minerals)-i)]
        d_cnt = split_minerals.count('diamond')
        i_cnt = split_minerals.count('iron')
        s_cnt = split_minerals.count('stone')
        
        arr.append((d_cnt*25+i_cnt*5+s_cnt*1, split_minerals))
    
    arr.sort(reverse=True)
    
    print(arr)
    
    for cnt, cur_minerals in arr:
        if gok==0:
            break
        diamond =cur_minerals.count('diamond')
        iron=cur_minerals.count('iron')
        stone=cur_minerals.count('stone')
        if picks[0]>0:
            answer +=diamond+iron+stone
            picks[0]=picks[0]-1
        elif picks[1]>0:
            answer +=5*diamond+iron+stone
            picks[1]=picks[1]-1
        elif picks[2]>0:
            answer +=25*diamond+5*iron+stone
            picks[2]=picks[2]-1
        else:
            break
        gok-=1


    return answer