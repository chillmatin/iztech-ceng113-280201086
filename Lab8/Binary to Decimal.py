def binary_to_dec(binary):

    reversed_binary = binary[::-1]
    binary = ''
    decimal = 0
    counter = 0
    for i in reversed_binary:
        if i == "1":
            decimal = decimal + 2 ** counter
        counter += 1

    return decimal


def dec_to_binary(decimal):
    if decimal == 0:
        return '0'

    reversed_binary = ''
    r = 0

    while decimal != 0:
        r = decimal % 2
        decimal = decimal // 2
        reversed_binary += str(r)
    binary = reversed_binary[::-1]
    return binary


print(binary_to_dec("10010"))
print(dec_to_binary(18))