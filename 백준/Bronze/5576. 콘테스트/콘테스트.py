arr1, arr2 = [],[]
for i in range(1, 21):
    if i<11:
        arr1.append(int(input()))
    else:
        arr2.append(int(input()))
arr1.sort(reverse=True)
arr2.sort(reverse=True)
print((arr1[0]+arr1[1]+arr1[2]), (arr2[0]+arr2[1]+arr2[2]))