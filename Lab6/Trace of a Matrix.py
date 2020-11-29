n = int(input("Matrix number: "))
string = ''
sum_list = []

for i in range(n):
    for j in range(n):
        number = int(input("Input number: "))

        if i == j:
            sum_list.append(number)
sum = 0
for i in sum_list:
    sum += i

print("Output: ", sum)
