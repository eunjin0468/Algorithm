n = int(input())
cnt, result = 0,0
while True:
    cnt+=1
    result+=cnt
    if result>n:
        break
    
print(cnt-1)