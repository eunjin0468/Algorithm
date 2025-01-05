n,m = map(int, input().split())
result,arr = [],[]
for _ in range(n):
    arr.append(input())

for i in range(n-7):
    for j in range(m-7):
        w_draw = 0
        b_draw = 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b)%2==0:
                    if arr[a][b]!='B':
                        w_draw+=1
                    else:
                        b_draw+=1
                else:
                    if arr[a][b]!='W':
                        w_draw+=1
                    else:
                        b_draw+=1
        result.append(w_draw)
        result.append(b_draw)
print(min(result))