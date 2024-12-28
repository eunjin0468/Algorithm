while True:
    n = int(input())
    if n==-1:
        break
    else:
        arr = [1]
        for i in range(2, n):
            if n%i==0:
                arr.append(i)
        cnt = sum(arr)
        if cnt==n:
            print(f"{n} = ", end='')
            for i in range(len(arr)):
                if i==0:
                    print(f"{arr[i]} ", end='')
                else:
                    print(f"+ {arr[i]} ",end='')
            print("")
        else:
            print(f"{n} is NOT perfect.")
