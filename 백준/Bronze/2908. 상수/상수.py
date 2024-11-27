a,b = input().split()
num_a, num_b = '', ''
for i in range(len(a)-1, -1,-1):
    num_a+=a[i]
    num_b+=b[i]
print(max(num_a, num_b))