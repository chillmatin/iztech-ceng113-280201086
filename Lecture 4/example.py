inputs = input("Please, input values separated by commas: ")
x1,x2,x3 = inputs.split(",")
x1,x2,x3 = int(x1),int(x2),int(x3)

if x1 >= x2 >= x3:
    maximum = x1
elif x2 >= x3:
    maximum = x2
else:
    maximum = x3

print("The largest value is", maximum)