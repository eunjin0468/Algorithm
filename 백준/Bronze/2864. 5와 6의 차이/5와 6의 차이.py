a,b = input().split()
max_num = int(a.replace('5', '6')) + int(b.replace('5', '6'))
min_num = int(a.replace('6', '5')) + int(b.replace('6', '5')) 
print(min_num, max_num)