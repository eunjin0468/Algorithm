import sys
input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(5)]
r,c = map(int, input().split())
cnt,apple = 0,0 #이동거리, 사과갯수
d = [(-1,0),(0,-1),(0,1),(1,0)]
ans = []
def dfs(r,c):
    global cnt, apple
    if apple==3:
        ans.append(cnt)
    for i,j in d:
        y,x = i+r, j+c
        if 0<=y<5 and 0<=x<5 and arr[y][x]!=-1:
            if arr[y][x]==1:
                apple+=1
                
            tmp = arr[r][c]
            arr[r][c]=-1 #방문처리 (장애물)
            cnt+=1
            dfs(y,x)
            cnt-=1
            arr[r][c]=tmp
            
            if arr[y][x]==1: # 백트래킹 시 사과 개수 복구
                apple-=1
    return ans
dfs(r,c)

if len(ans)!=0:
    print(min(ans))
else:
    print(-1)