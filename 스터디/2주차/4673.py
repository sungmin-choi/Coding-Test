numbers = [0 for _ in range(10001)]


for i in range(1,10001):
    ## a=['31']  if i==31
    a = [str(i)] 
    ## a=['31','3','1']
    a.extend(list(str(i)))
    ## a=[31,3,1] => 31+3+1 =>35
    b=sum(list(map(int, a)))
    if b <=10000:
        numbers[b]=1

for i in range(1,10001):
    if numbers[i] == 0:
        print(i)


