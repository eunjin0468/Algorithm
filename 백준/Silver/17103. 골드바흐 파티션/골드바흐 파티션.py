import math

n = int(input())
primeNum = [False, False] + [True]*999999

for i in range(2, 999999): #i의 배수는 배수 처리
    if primeNum[i]:
        for j in range(i*2, 999999, i):
            primeNum[j] = False

for _ in range(n):
    cnt = 0
    m = int(input())
    for j in range(2, m//2+1):
        if primeNum[j] and primeNum[m-j]:
            cnt+=1
    print(cnt)