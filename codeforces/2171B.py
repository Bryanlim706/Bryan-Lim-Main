cases = int(input())
for case in range(cases):
    length = int(input())
    arr = list(map(int, input().split()))
    new_arr = [None] * (length)
    for i in range(length):
        if (i == 0 or i == length - 1) and arr[i] == -1:
            new_arr[i] == None
        else:
            if arr[i] != -1:
                new_arr[i] = arr[i]
            else: 
                new_arr[i] = 0
    if new_arr[-1] == None and new_arr[0] != None:
        sum = 0
        for j in range(length - 2):
            sum += new_arr[j + 1] - new_arr[j]
        sum -= new_arr[length - 2]
        if sum <= 0:
            new_arr[-1] = -1 * sum
        else:
            new_arr[-1] = 0
    elif new_arr[-1] != None and new_arr[0] == None:
        sum = 0
        for j in range(length - 2):
            sum += new_arr[j + 2] - new_arr[j + 1]
        sum += new_arr[1]
        if sum >= 0:
            new_arr[0] = sum
        else:
            new_arr[0] = 0
    elif new_arr[-1] == None and new_arr[0] == None:
        sum = 0
        for j in range(length - 3):
            sum += new_arr[j + 2] - new_arr[j + 1]
        sum += new_arr[1]
        sum -= new_arr[length - 2]
        if sum > 0:
            new_arr[0] = sum
            new_arr[-1] = 0
        else:
            new_arr[0] = 0
            new_arr[-1] = -1 * sum
    final_sum = 0
    for k in range(length - 1):
        final_sum += new_arr[k + 1] - new_arr[k]
    print(abs(final_sum))
    ans = " ".join(map(str, new_arr))
    print(ans)