S = 'K1KA5CB7'
s = ''
n = ''
for i in S:
    if i.isalpha():
        s +=i
    else:
        n +=i
s = list(s)
number = 0  
for i in list(n):
    number += int(i) 

print(''.join(sorted(s))+str(number))


