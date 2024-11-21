n = int(input())
nth = 666
cnt=0
while True:
    if '666' in str(nth):
        cnt +=1
    if cnt==n:
        break
    nth += 1
print(nth)