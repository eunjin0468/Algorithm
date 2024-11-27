str = input()
new_str = ''
for s in str:
    if s.isupper() == True:
        s = s.lower()
        new_str += s
    else:
        s = s.upper()
        new_str += s
print(new_str)
