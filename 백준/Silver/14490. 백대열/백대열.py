n,m = map(int, input().split(':'))
def gcd(n,m):
    while m>0:
        tmp = n
        n = m
        m = tmp%m
    return n
a = gcd(n,m)
print('%d:%d' %(n//a, m//a))