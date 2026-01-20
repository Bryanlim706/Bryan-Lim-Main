cases = int(input())
for case in range(cases):
    number = int(input())
    arr = list(map(int, input().split()))
    x = int(input())
    arr.sort()
    if x <= arr[number - 1] and x >= arr[0]:
        print("YES")
    else:
        print("NO")