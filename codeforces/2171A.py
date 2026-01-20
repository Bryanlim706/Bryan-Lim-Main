cases = int(input())
for case in range(cases):
    count = int(input())
    if count % 2 != 0:
        print("0")
    else:
        number = int(count/2)
        if number % 2 == 0:
            x = int(number/2 + 1)
            print(x)
        else:
            x = int(number - 1)
            x = int(x/2 + 1)
            print(x)