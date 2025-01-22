n = int(input())
def factorial(n):
    if n<=1:
        return 1
    else:
        ans = n*factorial(n-1)
    return ans
print(factorial(n))