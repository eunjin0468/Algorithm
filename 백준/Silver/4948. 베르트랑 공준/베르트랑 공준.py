import math
import sys
input = sys.stdin.readline

num = 123456*2+1
num_list=[1]*num

for i in range(1, num):
    if i==1:
        continue
    for j in range(2, int(i**0.5)+1):
        if i%j==0:
            num_list[i]=0
            break

while True:
    num = int(input().rstrip())
    if num == 0:
        break
    cnt = 0
    for i in range(num+1, 2*num+1):
        cnt+=num_list[i]
    print(cnt)