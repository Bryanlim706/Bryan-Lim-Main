while True:
    try:
        n = int(input("Height: "))
        if (n > 0 and n < 9):
            break
        else:
            print("Height must be between 1 and 8 inclusive")

    except ValueError:
        print("not an integer")

for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
    for j in range(i + 1):
        print("#", end="")
    print("  ", end="")
    for j in range(i + 1):
        print("#", end="")
    print()
