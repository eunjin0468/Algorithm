t = int(input())
for i in range(1,t+1):
    n = int(input())
    if n>4500:
        print(f"Case #{i}: Round 1")
    elif n>1000:
        print(f"Case #{i}: Round 2")
    elif n>25:
        print(f"Case #{i}: Round 3")
    else:
        print(f"Case #{i}: World Finals")