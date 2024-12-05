i = int(input())
done = 0
while i > 1:
    if i%2==1:
        done = 1
        break
    i//=2
if done==1:
        print(0)
else: 
    print(1)