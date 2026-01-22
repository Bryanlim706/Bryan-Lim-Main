import math
cases = int(input())
for case in range(cases):
    data = list(map(int, input().split()))
    length = data[0]
    alice_number = data[1]
    arr = list(map(int, input().split()))
    counter = 0
    # counter = number of elements strictly less than alice: if alice = 40, counter = 3
    for i in range(length):
        if arr[i] >= alice_number:
            break
        else:
            counter += 1
    #splice elements which = alice number
    new_arr = []
    for i in range(length):
        if arr[i] != alice_number:
            new_arr.append(arr[i])
    new_length = len(new_arr)
    if counter <= math.floor(new_length / 2):
        b = alice_number + 1
    else:
        b = alice_number - 1
    print(b)