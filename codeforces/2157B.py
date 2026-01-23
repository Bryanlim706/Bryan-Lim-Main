cases = int(input())
for case in range(cases):
    n, x, y = map(int, input().split())
    arr = list(map(int, list(input())))
    x, y = abs(x), abs(y)
    points_needed = x + y
    points_present = 0
    sides, diags = 0, 0
    for operation in range(len(arr)):
        if arr[operation] == 4:
            sides += 1
        else:
            diags += 1
    diags_needed = min(x, y)
    sides_needed = abs(x - y)
    if diags > diags_needed:
        sides += diags - diags_needed
        if sides >= sides_needed:
            print("YES")
        else: 
            print("NO")
    else:
        sides -= 2 * (diags_needed - diags)
        if sides >= sides_needed:
            print("YES")
        else:
            print("NO")
    
