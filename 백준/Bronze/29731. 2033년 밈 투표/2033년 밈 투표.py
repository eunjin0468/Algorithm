str = ["Never gonna give you up","Never gonna let you down","Never gonna run around and desert you","Never gonna make you cry","Never gonna say goodbye","Never gonna tell a lie and hurt you","Never gonna stop"]
t = int(input())
flag = False
for _ in range(t):
    s = input()
    if s not in str:
        flag = True
if flag == True:
    print("Yes")
else:
    print("No")