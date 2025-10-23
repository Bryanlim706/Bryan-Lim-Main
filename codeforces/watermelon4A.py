while True:
    try:
        weight = int(input())
        if 1 <= weight <= 100:
            break
        else:
            print("Weight of watermelon to be 1-100kg")
    except ValueError:
        print("invalid. input an integer from 1-100.")

if weight % 2 == 0 and weight != 2:
    print("YES")
else:
    print("NO")
    
