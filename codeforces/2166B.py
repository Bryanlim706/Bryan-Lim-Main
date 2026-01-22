
from fractions import Fraction

def recursion(lst):
    m = len(lst)
    #base case
    if m <= 1:
        return lst
    
    duplicate_lst = []
    #recursion
    for i in range(m - 1):
        if (lst[0]["amt"] * lst[0]["size"]) % lst[i + 1]["size"] != 0:
            duplicate_lst.append(lst[i + 1])
    return ([lst[0]] + recursion(duplicate_lst))


cases = int(input())
for case in range(cases):

    #find all possible len
    data = list(map(int, input().split()))
    a, b, n = data[0], data[1], data[2]
    len_arr = []
    length = len(len_arr)
    for i in range(n):
        if a / (i + 1) > b:
            len_arr.append(b)
        else:
            len_arr.append(Fraction(a, (i + 1)))
    #pop all len = b
    y = 0
    new_dict = []
    for j in range(n):
        if len_arr[j] == b:
            y = j + 1
        else:
            new_dict.append({"amt": j + 1, "size": len_arr[j]})

    if y != 0:
        new_dict = [{"amt": 1, "size": b}] + new_dict

    ans = recursion(new_dict)

    print(len(ans))
   


    
        