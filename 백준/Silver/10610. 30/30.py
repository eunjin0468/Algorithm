from itertools import combinations
import sys
input = sys.stdin.readline

n = input().strip()

if '0' not in n:
    print(int(-1))
else:
    num_sum = 0
    for i in range(len(n)):
        num_sum += int(n[i])
    if num_sum%3!=0:
        print(int(-1))
    else:
        sorted_num = sorted(n, reverse=True)
        ans = ''.join(sorted_num)
        print(int(ans))