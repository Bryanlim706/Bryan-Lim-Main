from cs50 import get_int
from sys import exit


def main():
    # get and save number info
    cc_number_str = str(get_int("Number: "))
    length_cc = int(len(cc_number_str))

    # checks
    length_check(length_cc)
    checksum(length_cc, cc_number_str)
    card_type(cc_number_str, length_cc)


# checks length valid
def length_check(length_cc):
    if (length_cc < 13 or length_cc > 16):
        print("INVALID")
        exit(1)
    else:
        return 0


# checks checksum valid
def checksum(length_cc, cc_number_str):
    checksum_count = 0

    # if cc number is even (first 3 steps)
    if (length_cc % 2 == 0):
        for i in range(int(length_cc / 2)):
            if (len(str(2 * (int(cc_number_str[2 * i])))) == 1):
                checksum_count += 2 * (int(cc_number_str[2 * i]))
            else:
                buffer = int(str(2 * (int(cc_number_str[2 * i])))[0]) + \
                    int(str(2 * (int(cc_number_str[2 * i])))[1])
                checksum_count += buffer
        for i in range(int(length_cc / 2)):
            checksum_count += int(cc_number_str[(2 * i) + 1])

    # if cc number is odd (first 3 steps)
    else:
        for i in range(int((length_cc - 1) / 2)):
            if (len(str(2 * (int(cc_number_str[(2 * i) + 1])))) == 1):
                checksum_count += (2 * int(cc_number_str[(2 * i) + 1]))
            else:
                buffer = int(str(2 * (int(cc_number_str[(2 * i) + 1])))[0]) + \
                    int(str(2 * (int(cc_number_str[(2 * i) + 1])))[1])
                checksum_count += buffer
        for i in range(int((length_cc + 1) / 2)):
            checksum_count += int(cc_number_str[2 * i])

    # last step
    if (checksum_count % 10 == 0):
        return 0
    else:
        print("INVALID")
        exit(1)


# checks type of card
def card_type(cc_number_str, length_cc):
    if (length_cc == 15 and int(cc_number_str[0]) == 3 and int(cc_number_str[1]) in (4, 7)):
        print("AMEX")
        exit(0)

    elif (length_cc == 16 and int(cc_number_str[0]) == 5 and int(cc_number_str[1]) in range(1, 6)):
        print("MASTERCARD")
        exit(0)

    elif (length_cc in range(13, 17) and int(cc_number_str[0]) == 4):
        print("VISA")
        exit(0)

    else:
        print("INVALID")


main()
