import sys
read = lambda: sys.stdin.readline().rstrip()

arr = list(read())

grp0=0
grp1=0

curNum=arr[0]
if curNum == '0':
    grp0 +=1
else:
    grp1 +=1


for i in range(1, len(arr)):
    if arr[i]!=curNum:
        curNum = arr[i]
        if curNum == '0':
            grp0 +=1
        else:
            grp1 +=1

print(min(grp0,grp1))
