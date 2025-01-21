n = int(input())
line = list(map(int, input().split())) #인접한 도시의 길이
oil = list(map(int, input().split())) #도시당 주유소의 리터당 가격
min_price = oil[0]
total = 0
for i in range(n-1): #n이 4면, i는 0~2 최종목적지에서는 주유x
    if min_price > oil[i]:
        min_price = oil[i]
    total += (min_price*line[i])
print(total)