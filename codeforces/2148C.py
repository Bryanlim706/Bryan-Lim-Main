cases = int(input())
for case in range(cases):
    n, m = list(map(int, input().split()))
    points = m
    lst = True # even true
    for i in range(n):
        place = list(map(int, input().split()))
        if (int(place[0]) - int(place[1])) % 2 == 0:
            new = True
        else:
            new = False
        if lst != new:
            lst = new
            points -= 1
    
    print(points) 
        
        