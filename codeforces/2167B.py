import sys
cases = int(input())
for case in range(cases):
    len = int(input())
    arr = list(input().split())
    letters = sorted(arr[0])
    name = sorted(arr[1])
    l = 0
    n = 0
    while l < len and n < len:
        if letters[l] == name[n]:
            l += 1
            n += 1
        else:
            print("NO")
            break
        if l == len and n == len:
            print("YES")


