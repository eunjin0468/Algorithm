a,b,c,d = map(int, input().split()) 
throughput, tired = 0,0
for i in range(24):
    if tired+a <= d:
        tired+=a
        throughput+=b
    else:
        if tired-c>=0:
            tired-=c
        else:
            tired = 0
print(throughput)