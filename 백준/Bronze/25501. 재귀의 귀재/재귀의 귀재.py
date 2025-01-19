def recursion(str, l, r, cnt):
    if l>=r:
        return (1, cnt)
    elif str[l] != str[r]:
        return (0, cnt)
    else:
        return recursion(str, l+1, r-1, cnt+1)

def isPalindrome(str, cnt):
    return(recursion(str, 0, len(str)-1, cnt))

n = int(input())
for _ in range(n):
    str = input()
    print(*isPalindrome(str, 1))