data_array = []
while True:
    try: 
        number_of_entries = int(input())
        if 1 <= number_of_entries <= 5940:
            break
    except ValueError:
        print("input integer between 1 and 5940")

for _ in range(number_of_entries):
    data_array.append(input())

for case in data_array:
    numbers = case.split()
    #fix numbers 1 and 2
    if int(numbers[0]) > int(numbers[1]):
        bigger = int(numbers[0])
        smaller = int(numbers[1])
    else: 
        bigger = int(numbers[1])
        smaller = int(numbers[0])
    if smaller < int(numbers[2]) < bigger and smaller < int(numbers[3]) < bigger:
        print("NO")
    elif (0 < int(numbers[2]) < smaller or bigger < int(numbers[2]) < 13) and (0 < int(numbers[3]) < smaller or bigger < int(numbers[3]) < 13):
        print("NO")
    else:
        print("YES")


