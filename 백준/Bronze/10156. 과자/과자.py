#과자 한개 가격:K, 사려는 갯수:N, 현재 가진 돈:M
k,n,m = map(int, input().split())
if k*n>m:
    print(k*n-m)
else:
    print(0)