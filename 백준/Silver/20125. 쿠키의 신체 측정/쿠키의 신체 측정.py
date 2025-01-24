n = int(input())
arr = [input() for _ in range(n)]
heart = [0,0]
body = [0]*5 #왼팔, 오른팔, 허리, 왼다리, 오른다리
for i in range(n):
    for j in range(n):
        if arr[i][j] == '*':
            if arr[i][j] == '*' and heart == [0,0]:
                    heart = (i+1, j) #심장
            elif i == heart[0]: #팔
                if j<heart[1]:
                    body[0]+=1
                elif j>heart[1]:
                    body[1]+=1
            elif j==heart[1]: #허리
                body[2]+=1
            elif j==heart[1]-1: #다리
                body[3]+=1
            elif j==heart[1]+1:
                body[4]+=1
print(heart[0]+1, heart[1]+1)
print(*body)