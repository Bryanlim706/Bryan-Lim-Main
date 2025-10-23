amt_test_samples = int(input())
for i in range(amt_test_samples):
    array = input().split()
    t_counter = 0
    f_counter = 0
    n_counter = 0
    others = []
    for j in array:
        if str(j).strip().upper() == str("T"):
            t_counter += 1
        elif str(j).strip().upper() == str("F"):
            f_counter += 1
        elif str(j).strip().upper() == str("N"):
            n_counter += 1
        else:
            others.append(j)
    final_str = "T"*t_counter + "F"*f_counter + "N"*n_counter + "".join(others)
        
    print(final_str)

