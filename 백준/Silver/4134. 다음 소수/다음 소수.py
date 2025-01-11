import math
n = int(input())

def prime(num): #소수 판별하는 함수
    if num==0 or num==1:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num%i==0:
            return False
    return True 

for _ in range(n):
    num = int(input())
    while True:
        if prime(num): #소수일 경우 num출력
            print(num)
            break
        else: #소수가 아닐 경우 num 증가
            num+=1