def cut(a, n):
    if n==1:
        return
    for i in range(a+n//3, a+(n//3)*2):
        res[i] = ' '
    cut(a, n//3) #왼쪽 자르기
    cut(a+(n//3)*2, n//3) #오른쪽 자르기

while True:
    try:
        n = int(input())
        res = ['-']*(3**n) #'-'가 3^n개 문자열 리스트
        cut(0, 3**n)
        print(''.join(res))
    except:
        break