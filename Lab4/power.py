a = int(input("Input a: "))
b = int(input("Input b: "))
powerizer = a
for i in range(b-1):
 a *= powerizer

print(a)