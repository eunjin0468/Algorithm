import sys
a,b = map(int, sys.stdin.readline().split())
dic = {} 
for i in range(a):
    i = sys.stdin.readline().rstrip()
    if len(i) >= b:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i]+=1
dic = sorted(dic.items(), key=lambda x:(-x[1], -len(x[0]), x[0]))
for i in range(len(dic)):
    print(dic[i][0])