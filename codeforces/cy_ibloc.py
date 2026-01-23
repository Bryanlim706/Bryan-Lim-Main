def f(n):
    if n < 3:
        return n
    else:
        third_last, second_last, last = 0, 1, 2
        for _ in range(n - 2):
            new = last + 2 * second_last + 3 * third_last
            third_last, second_last, last = second_last, last, new
    return(new)
            
print(f(int(input())))