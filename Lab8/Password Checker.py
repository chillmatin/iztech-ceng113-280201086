def password_level(password):

    level = 0

    if len(password) < 8:
        return level

    space_exists = False
    alpha_exists = False
    special_exists = False
    numeric_exists = False

    for char in password:

        if char == " ":
            level = 0
            return level

        elif char.isnumeric() and numeric_exists == False:
            numeric_exists = True
            level += 1

        elif char.isalpha() and alpha_exists == False:
            alpha_exists = True
            level += 1

        elif not (char.isnumeric() or char.isalpha()) and special_exists == False:
            special_exists = True
            level += 1

    return level


print(password_level("abcde12345--"))
print(password_level("ab de12345--"))
print(password_level("abc12--"))
print(password_level("234567893"))
print(password_level("abc1234567"))
