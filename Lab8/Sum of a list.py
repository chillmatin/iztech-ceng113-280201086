def sum_list(numbers):
    sum = 0
    for i in numbers:
        sum += i
    
    sum = sum**2
    return sum

a_list = [12, -7, 5, -89.4, 3, 27, 56, 57.3]
number = sum_list(a_list)
print(number)