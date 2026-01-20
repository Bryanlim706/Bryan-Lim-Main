cases = int(input())
for _ in range(cases):
    numbers = list(map(int, input().split()))
    collateral_constant = int(numbers[1])
    binary = str(input())
    slept_classes = int(0)
    collateral_count = int(0)
    for digit in binary:
        if int(digit) == 1:
            collateral_count = collateral_constant
        elif int(digit) == 0 and collateral_count != 0:
            collateral_count -= 1
        else:
            slept_classes += 1
    print(slept_classes)