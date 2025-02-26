from collections import deque
a,b,c = map(int, input().split())
q = deque()
q.append((0,0))

visited = [[0]*(b+1) for _ in range(a+1)] #a,b 방문 여부 저장
visited[0][0] = 1 #시작점 방문 처리
ans = [] #a가 비어있을 때 c물통의 가능한 물의 양 저장

def pour(x,y): #새로운 상태를 큐에 추가
    if visited[x][y]==0:
        visited[x][y]=1
        q.append((x,y))
def bfs():
    while q:
        x,y = q.popleft()
        z = c-x-y #c물통에 남아있는 물의 양 계산
        
        if x==0: #a물통이 비어있을 때, c물통의 물 저장
            ans.append(z)
            
        #6가지 물 옮기기(각 물통에서 다른 물통으로 이동)
        water = min(x, b-y) #a->b
        pour(x-water, y+water)
            
        water = min(x, c-z) #a->c
        pour(x-water, y)
            
        water = min(y, c-z) #b->c
        pour(x,y-water)
            
        water = min(y, a-x) #b->a
        pour(x+water, y-water)
            
        water = min(z, a-x) #c->a
        pour(x+water, y)
            
        water = min(z, b-y) #c->b
        pour(x, y+water)
bfs()
ans.sort()
for i in ans:
    print(i, end=' ')