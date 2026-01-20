cases = int(input())
for case in range(cases):
    number = int(input())
    arr = list(map(int, input().split()))
    haveeven = False
    haveodd = False
    for i in arr:
        if i % 2 == 0:
            haveeven = True
        else:
            haveodd = True
    if haveodd == True and haveeven == True:
        arr.sort()
        result = " ".join(map(str, arr))
        print(result)
    else:
        result = " ".join(map(str, arr))
        print(result)