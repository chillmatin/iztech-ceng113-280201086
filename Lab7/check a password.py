def is_valid(password):
    validity = True
    upper_exist = False
    lower_exist = False
    number_exist = False

    if len(password) < 8:
        validity = False
        return validity

    for char in password:
        if char.isalpha():
            if char == char.upper():
                upper_exist = True
            elif char == char.lower():
                lower_exist = True

        elif char.isnumeric():
            number_exist = True

    validity = number_exist and lower_exist and upper_exist
    return validity


a = input("Please input a pass: ")

print(is_valid(a))
