count = 0
base = int(input("Please, input base: "))
power = int(input("Please, input power: "))
result = 1
while (count < power):
  result = result * base
  count += 1

print(result)