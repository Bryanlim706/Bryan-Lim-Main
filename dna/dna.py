import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("invalid number of command-line arguments")
        sys.exit(1)

    # TODO: Read database file into a variable
    with open(sys.argv[1]) as file:
        database = csv.DictReader(file)
        first_row = next(database)

    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2]) as file2:
        sequence = file2.read()

    # TODO: Find longest match of each STR in DNA sequence
    keys = list(first_row.keys())
    keys.pop(0)

    STR_counts = 0
    for STRs in keys:
        if STR_counts == 0:
            STR_counts = {STRs: longest_match(sequence, STRs)}
        else:
            STR_counts[STRs] = longest_match(sequence, STRs)

    # TODO: Check database for matching profiles
    no_match_check = True
    with open(sys.argv[1]) as file:
        database = csv.DictReader(file)
        for row in database:
            counter = 0
            for STR_type in keys:
                if int(row[STR_type]) == int(STR_counts[STR_type]):
                    counter += 1
            if counter == len(keys):
                print(row["name"])
                no_match_check = False

    if no_match_check:
        print("No match")

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
