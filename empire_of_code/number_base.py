# You are given a positive number as a string along with the radix for it.
# Your function should convert it into decimal form.
# The radix is less than 37 and greater than 1.
# The task uses digits and the letters A-Z for the strings.
#
# Watch out for cases when the number cannot be converted.
# For example: "1A" cannot be converted with radix 9.
# For these cases your function should return -1.


def convert(str_number, radix):
    # Exception handler
    try:
        if 2 <= radix <= 36 and 0 < len(str_number) <= 10:
            converted_number = int(str_number, radix)
            print(converted_number)
            return converted_number
        else:
            print('Out of range.')
    except:
        print(-1)
        return -1


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert convert("AF", 16) == 175, "Hex"
    assert convert("101", 2) == 5, "Bin"
    assert convert("101", 5) == 26, "5 base"
    assert convert("Z", 36) == 35, "Z base"
    assert convert("AB", 10) == -1, "B > A > 10"

    print("Use 'Check' to earn sweet rewards!")
