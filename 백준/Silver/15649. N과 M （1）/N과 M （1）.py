n, m = map(int, input().split())
ans = []

def solve():
    if len(ans) == m:
        print(' '.join(map(str, ans)))
        return
    
    for i in range(1, n+1):
        if i not in ans:
            ans.append(i)
            solve()
            ans.pop() 

solve()