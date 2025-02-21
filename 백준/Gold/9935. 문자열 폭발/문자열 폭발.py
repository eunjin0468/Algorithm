str = input()
p = input()
l = len(p)

stack = []
for s in str:
    stack.append(s)
    if ''.join(stack[-l:]) == p:
        for j in range(l):
            stack.pop()
if stack:
    print(''.join(stack[:]))
else:
    print("FRULA")