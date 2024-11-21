while True:
    triangle = list(map(int, input().split()))
    if triangle[0] ==0:
        break
    triangle.sort()
    if triangle[0]**2 + triangle[1]**2 == triangle[2]**2:
        print("right")
    else:
        print("wrong")