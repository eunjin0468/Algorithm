n = int(input())
a = [[0]*10 for _ in range(n)] #DP테이블 초기화
a[0] = [0,1,1,1,1,1,1,1,1,1] #1의 자릿수 초기 설정

#점화식 구현
for m in range(1, n): 
    a[m][0] = a[m-1][1] #끝자리가 0
    a[m][9] = a[m-1][8] #끝자리가 9

    #길이가 n-1인 계단 수 중, 끝자리가 k-1과 k+1인 수의 합
    for i in range(1, 9): #끝자리 0,9제외
        a[m][i] = a[m-1][i-1] + a[m-1][i+1]
print(sum(a[n-1])%1000000000)