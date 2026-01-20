cases = int(input())
for case in range(cases):
    len = list(map(int, input().split()))
    if len[0] == len[1] and len[0] == len[2] and len[0] == len[3]:
        print("YES")
    else:
        print("NO")