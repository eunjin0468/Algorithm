n = list(map(int, input()))
l = len(n)//2
if sum(n[l:]) == sum(n[:l]):
    print("LUCKY")
else:
    print("READY")