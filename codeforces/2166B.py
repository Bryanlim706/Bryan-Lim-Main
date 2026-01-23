
cases = int(input())
for case in range(cases):

    #find all possible len
    data = list(map(int, input().split()))
    a, b, n = data[0], data[1], data[2]
    len_arr = []
    length = len(len_arr)
    if b >= a or b * n <= a:
        print("1")
    else:
        print("2")



   


    
        