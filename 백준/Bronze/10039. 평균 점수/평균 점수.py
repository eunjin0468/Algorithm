avg = 0
for _ in range(5):
    a = int(input())
    if a<=40:
        a = 40
    avg+=a
print(avg//5)