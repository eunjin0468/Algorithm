n = int(input())
arr = sorted(list(set(map(int, input().split()))))
print(' '.join(map(str, arr)))