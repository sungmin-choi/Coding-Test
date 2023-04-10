obj = {'A':1,'E':2,'I':3,'O':4,'U':5}
arr=['','A','E','I','O','U']

def solution(word):
    answer = 1
    s='A'
    while s!=word:
        if len(s)<5:
            s+='A'
        else:
            if obj[s[-1]]<5:
                s= s[0:-1]+arr[obj[s[-1]]+1]
            else:
                flag=True
                while flag and len(s)>1:
                    s=s[0:-1] 
                    if obj[s[-1]]<5:
                        s=s[0:-1]+arr[obj[s[-1]]+1]
                        flag=False
        answer+=1
    return answer