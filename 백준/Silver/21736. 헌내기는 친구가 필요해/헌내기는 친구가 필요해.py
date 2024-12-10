from collections import deque
a,b = map(int, input().split())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
ch = [[0]*b for _ in range(a)]
campus = []
q = deque()
result = 0
for i in range(a):
    campus.append(list(map(str, input().strip())))
    for j in range(len(campus[i])):
        if campus[i][j]=="I":
            q.append([i,j])
            ch[i][j]=1
while q:
    for _ in range(len(q)):
        r,c = q.popleft()
        for i in range(4):
            nr,nc = r+dx[i], c+dy[i]
            if 0<=nr<a and 0<=nc<b and ch[nr][nc]==0 and campus[nr][nc]!="X":
                if campus[nr][nc] == "P":
                    result+=1
                ch[nr][nc]=1
                q.append([nr, nc])
if result:
    print(result)
else:
    print("TT")