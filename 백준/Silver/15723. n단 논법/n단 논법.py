inf = int(1e9)
t1 = int(input())
distance = [[inf]*26 for _ in range(26)]
for _ in range(t1):
    a,b = input().split(' is ')
    a = ord(a)-97
    b = ord(b)-97
    distance[a][b] = 1

for i in range(26): #가운데
    for j in range(26): #시작
        for k in range(26): #마지막
            distance[j][k] = min(distance[j][k], distance[j][i]+distance[i][k])
t2 = int(input())
for _ in range(t2):
    c,d = input().split(' is ')
    c = ord(c)-97
    d = ord(d)-97
    print("T" if distance[c][d] < inf else "F")