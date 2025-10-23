sample_amt = int(input())
j = 0
for j in range(sample_amt):
    #main: for each sample
    no_of_elements = int(input())
    original_numbers_array = (input()).split()
    numbers_array = [(int(x)) for x in original_numbers_array]

    #initializing variables for main
    smallest_end_state = numbers_array[0] + min(numbers_array[0], numbers_array[1])

    continuous_variable = numbers_array[0]
    smallest_numbers_index = 0

    unincluded_element = 1

    for i, number in enumerate(numbers_array[1:], start=1):
        #if operate, compare end_state with smallest end_state, if smaller replace.
        end_number = continuous_variable + (number * unincluded_element)
        if end_number < smallest_end_state:
            smallest_end_state = end_number

            #update smallest_numbers_index
        if numbers_array[smallest_numbers_index] > number:
            smallest_numbers_index = i
        else:
            unincluded_element = 0
        #if continue, update continuous_variable
        continuous_variable = continuous_variable + min(numbers_array[smallest_numbers_index], number)
    print(smallest_end_state)
    
    