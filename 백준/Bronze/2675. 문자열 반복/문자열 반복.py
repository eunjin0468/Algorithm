t = int(input())
for _ in range(t):
    n, str = input().split()
    for i in range(len(str)):
        print(str[i]*int(n), end='')
    print("")
    