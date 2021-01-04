def sum_list(numlist):

    if numlist == []:
        return 0
    if isinstance(numlist[0],list):
        return sum_list(numlist[0]) + sum_list(numlist[1:])

    return numlist[0] + sum_list(numlist[1:])

a_list = [3,12,76,[4,56,43],[2,8],81,75]

print(sum_list(a_list))