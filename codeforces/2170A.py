cases = int(input())
for case in range(cases):
    n = int(input())
    max_number = n ** 2
    if n == 1:
        print("1")
    elif n == 2:
        print("9")
    else:
        x = int((max_number * 3 - 3) + (max_number - (n - 1) - 2))
        central_number = max_number - (n - 1) - 2
        y = int((central_number * 3) + max_number - 1 + (central_number - (n - 2) - 2))
        if x > y:
            print(x)
        else:
            print(y)