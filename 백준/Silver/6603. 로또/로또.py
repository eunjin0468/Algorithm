import itertools

while True:
    arr = list(map(int, input().split()))
    k = arr[0]
    s = arr[1:]
    if k==0:
        exit()
    for i in itertools.combinations(s, 6):
        print(*i)
    print()