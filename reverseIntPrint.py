def print_digits(num):
    """Given int, print digits in reverse order, starting with the ones place (using math, not reverse"""

    # # non-mathy way
    # string_num = str(num)
    # list_num = list(string_num)

    # while list_num:
    #     print list_num.pop()

    # mathy way
    divisor = 1

    while num:
        digit = num % (divisor * 10)
        num = num - digit
        digit = digit / divisor
        print digit
        divisor = divisor * 10

    # # published soultion
    # while not num % 10 == num:

    #     next_digit = num % 10
    #     print next_digit
    #     num = (num - next_digit) / 10

    # print num


print_digits(314)