n = int(input())
first_str = list(input())
len_first_str = len(first_str)

for i in range(n-1):
    str = list(input())
    for j in range(len(first_str)):
        if first_str[j]!=str[j]:
            first_str[j] = '?'
print(''.join(first_str))