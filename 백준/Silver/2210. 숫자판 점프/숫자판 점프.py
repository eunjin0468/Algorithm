arr = [list(input().split()) for _ in range(5)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]
visited = [[0]*5 for _ in range(5)]
str = []

def dfs(i,j, num):
    if len(num)==6:
        if num not in str:
            str.append(num)
        return
    for k in range(4):
        x,y = dx[k]+i, dy[k]+j
        if 0<=x<5 and 0<=y<5:
            dfs(x,y, num+arr[x][y])
    

for i in range(5):
    for j in range(5):
        dfs(i,j,arr[i][j])
print(len(str))