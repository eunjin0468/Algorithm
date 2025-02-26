n,k = map(int, input().split())
tmp = 0 
prime = [1]*(n+1)

for i in range(2, n+1): 
    for j in range(i, n+1, i):
        if prime[j]==1:
            prime[j]=0
            tmp+=1
            if tmp==k:
                print(j)