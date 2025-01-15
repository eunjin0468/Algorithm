n = int(input())
line = list(map(int, input().split()))

i=1 #대기열에서 기대하는 번호표
stack = []
for num in line:
    stack.append(num)
    while stack and stack[-1]==i: #stack은 후입선출방식
        stack.pop()
        i+=1
if not stack:
    print("Nice")
else:
    print("Sad")