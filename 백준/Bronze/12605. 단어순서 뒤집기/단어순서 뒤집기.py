t = int(input())
for k in range(1,t+1):
    print(f'Case #{k}: ', end='')
    str = list(input().split())
    l = len(str)
    for i in range(l-1, -1,-1):
        print(str[i], end=' ')
    print('')