n1 = int(input("Enter the number pls : "))
n2 = int(input("Enter the number pls : "))
same = 0
while n1 > 0 and n2 > 0:
    if n1 % 10 == n2 % 10:
        same += 1
    n1 //= 10
    n2 //= 10
print(same)